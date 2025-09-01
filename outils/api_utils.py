"""
api_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Ce module fournit des utilitaires et fonctions communes pour Cyber Protection Personnalité. Il contient des helpers réutilisables, des fonctions de validation, de formatage et de traitement des données.

Classes principales : APIError, APIClient, ServiceRegistry, APIMonitor
Fonctions principales : api_success_response, api_error_response, validate_required_fields, get_service_registry, make_api_request, validate_api_response, get_service_url, health_check_services

Exemples d'utilisation :
    - Import : from outils.api_utils import function_name
    - Utilisation : result = function_name(param1, param2)
    - Intégration : Importé automatiquement par les autres modules
    - Tests : Tests unitaires pour chaque fonction utilitaire

Dépendances :
    - Imports : typing.Any, typing.Dict, typing.Optional, rest_framework.response.Response, rest_framework.status, json, logging, requests, typing.Dict, typing.Any

Intégration dans l'architecture :
    - Réutilisabilité : Fonctions partagées entre modules
    - Performance : Optimisations communes
    - Maintenance : Code centralisé et maintenu
    - Tests : Tests unitaires pour chaque utilitaire

Ce fichier fait partie intégrante de l'écosystème Cyber Protection Personnalité
et contribue à la sécurité et au monitoring des identités numériques.
"""

"""
api_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    API REST avec endpoints standardisés
"""

from typing import Any, Dict, Optional
from rest_framework.response import Response
from rest_framework import status

# Import du module json
import json
# Import du module logging
import logging
# Import du module requests
import requests
from typing import Dict, Any, Optional, Union
from urllib.parse import urljoin
# Import du module time
import time
from functools import wraps
import threading
from datetime import datetime, timedelta


def api_success_response(data, message="Success", status_code=200):
    """
    Retourne une réponse API de succès standardisée.
    """
    return {
        "success": True,
        "message": message,
        "data": data,
        "status_code": status_code
    }


def api_error_response(message: str,
                       status_code: int = 500,
                       response_data: Dict = None):
    """
    Retourne une réponse API d'erreur standardisée.

    Date de création: 2024
    Créateur: bigmoletos

    Cette fonction génère une réponse API standardisée avec un format
    cohérent pour tous les microservices.

    Args:
        message (str): Message d'erreur descriptif
        status_code (int): Code de statut HTTP (optionnel)
        response_data (Dict): Données de réponse associées (optionnel)

    Returns:
        Dict: Réponse API standardisée avec format JSON

    Exemples:
        >>> response = api_error_response("Erreur lors de la récupération des données")
    """
    return {
        "success": False,
        "message": message,
        "status_code": status_code,
        "response_data": response_data or {}
    }


class APIError(Exception):
    """
    Exception personnalisée pour les erreurs API.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe permet de gérer les erreurs spécifiques aux API.

    Attributs:
        message (str): Message d'erreur descriptif
        status_code (int): Code de statut HTTP (optionnel)
        response (requests.Response): Réponse de l'API (optionnel)
    """

    def __init__(self,
                 message: str,
                 status_code: int = None,
                 response: Response = None):
        """
        Initialiser une exception API.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            message (str): Message d'erreur descriptif
            status_code (int): Code de statut HTTP (optionnel)
            response (requests.Response): Réponse de l'API (optionnel)
        """
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

class APIClient:
    """
    Client API unifié avec gestion d'erreurs et retry automatique.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe fournit un client API robuste avec gestion automatique
    des erreurs, retry en cas d'échec, et monitoring des performances.

    Attributs:
        config (APIConfig): Configuration du client API
        session (requests.Session): Session HTTP réutilisable
        cache (Dict): Cache des réponses API
        _lock (threading.Lock): Verrou pour les opérations thread-safe

    Méthodes principales:
        - get: Effectuer une requête GET
        - post: Effectuer une requête POST
        - put: Effectuer une requête PUT
        - delete: Effectuer une requête DELETE
        - health_check: Vérifier la santé de l'API
    """
    pass

    pass

    def __init__(self, config: APIConfig):
        """
        Initialiser le client API.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            config (APIConfig): Configuration du client API
        """
        self.config = config
        self.session = requests.Session()
        self.cache = {}
        self._lock = threading.Lock()

        # Configurer la session
        self._setup_session()

    def _setup_session(self):
        """
        Configurer la session HTTP avec les paramètres par défaut.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode configure les en-têtes par défaut, le timeout,
        et les paramètres SSL de la session HTTP.
        """
        # En-têtes par défaut
        default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'CyberProtection-APIClient/1.0'
        }

        # Fusionner avec les en-têtes personnalisés
        if self.config.headers:
            default_headers.update(self.config.headers)

        self.session.headers.update(default_headers)

        # Configurer l'authentification si un token est fourni
        if self.config.auth_token:
            self.session.headers[
                'Authorization'] = f'Bearer {self.config.auth_token}'

        # Configurer le timeout et la vérification SSL
        self.session.verify = self.config.verify_ssl

    def _make_request(self,
                      method: str,
                      endpoint: str,
                      data: Dict[str, Any] = None,
                      params: Dict[str, Any] = None,
                      headers: Dict[str, str] = None,
                      use_cache: bool = False) -> Dict[str, Any]:
        """
        Effectuer une requête HTTP avec retry automatique.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            method (str): Méthode HTTP (GET, POST, PUT, DELETE)
            endpoint (str): Endpoint de l'API
            data (Dict[str, Any]): Données à envoyer (optionnel)
            params (Dict[str, Any]): Paramètres de requête (optionnel)
            headers (Dict[str, str]): En-têtes supplémentaires (optionnel)
            use_cache (bool): Utiliser le cache pour les requêtes GET

        Returns:
            Dict[str, Any]: Réponse de l'API

        Raises:
            APIError: En cas d'erreur après tous les retry

        Exemples:
            >>> response = client._make_request("GET", "/users", use_cache=True)
            >>> response = client._make_request("POST", "/users", data={"name": "John"})
        """
        # Construire l'URL complète
        url = f"{self.config.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        # Vérifier le cache pour les requêtes GET
        if use_cache and method.upper() == 'GET':
            cache_key = f"{method}:{url}:{hash(str(params))}"
            cached_response = self._get_from_cache(cache_key)
            if cached_response:
                logger.debug(f"Réponse récupérée du cache: {endpoint}")
                return cached_response

        # Fusionner les en-têtes
        request_headers = {}
        if headers:
            request_headers.update(headers)

        # Tentatives avec retry
        last_exception = None

        for attempt in range(self.config.retry_attempts + 1):
            try:
                # Préparer les données de la requête
                request_kwargs = {
                    'timeout': self.config.timeout,
                    'headers': request_headers,
                    'verify': self.config.verify_ssl
                }

                if params:
                    request_kwargs['params'] = params

                if data:
                    request_kwargs['json'] = data

                # Effectuer la requête
                start_time = time.time()
                response = self.session.request(method, url, **request_kwargs)
                duration = time.time() - start_time

                # Logger la requête
                logger.debug(
                    f"API {method} {endpoint} - {response.status_code} - {duration:.3f}s"
                )

                # Vérifier le code de statut
                if response.status_code < 400:
                    # Succès
                    result = {
                        'status_code': response.status_code,
                        'data': response.json() if response.content else None,
                        'headers': dict(response.headers),
                        'duration': duration
                    }

                    # Mettre en cache si demandé
                    if use_cache and method.upper() == 'GET':
                        self._set_cache(cache_key, result)

                    return result

                elif response.status_code in RETRY_STATUS_CODES and attempt < self.config.retry_attempts:
                    # Erreur temporaire, retry
                    logger.warning(
                        f"Erreur temporaire {response.status_code}, tentative {attempt + 1}/{self.config.retry_attempts}"
                    )
                    time.sleep(self.config.retry_delay * (attempt + 1))
                    continue

                else:
                    # Erreur permanente
                    raise APIError(
                        f"Erreur API {response.status_code}: {response.text}",
                        status_code=response.status_code,
                        response=response)

            except requests.exceptions.RequestException as e:
                last_exception = e
                if attempt < self.config.retry_attempts:
                    logger.warning(
                        f"Erreur de connexion, tentative {attempt + 1}/{self.config.retry_attempts}: {e}"
                    )
                    time.sleep(self.config.retry_delay * (attempt + 1))
                else:
                    break

        # Toutes les tentatives ont échoué
        raise APIError(
            f"Échec après {self.config.retry_attempts} tentatives: {last_exception}"
        )

    def get(self,
            endpoint: str,
            params: Dict[str, Any] = None,
            headers: Dict[str, str] = None,
            use_cache: bool = True) -> Dict[str, Any]:
        """
        Effectuer une requête GET.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            endpoint (str): Endpoint de l'API
            params (Dict[str, Any]): Paramètres de requête (optionnel)
            headers (Dict[str, str]): En-têtes supplémentaires (optionnel)
            use_cache (bool): Utiliser le cache (défaut: True)

        Returns:
            Dict[str, Any]: Réponse de l'API

        Exemples:
            >>> users = client.get("/users", params={"page": 1, "limit": 10})
            >>> user = client.get("/users/123")
        """
        return self._make_request("GET",
                                  endpoint,
                                  params=params,
                                  headers=headers,
                                  use_cache=use_cache)

    def post(self,
             endpoint: str,
             data: Dict[str, Any] = None,
             headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Effectuer une requête POST.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            endpoint (str): Endpoint de l'API
            data (Dict[str, Any]): Données à envoyer (optionnel)
            headers (Dict[str, str]): En-têtes supplémentaires (optionnel)

        Returns:
            Dict[str, Any]: Réponse de l'API

        Exemples:
            >>> new_user = client.post("/users", data={"name": "John", "email": "john@example.com"})
        """
        return self._make_request("POST", endpoint, data=data, headers=headers)

    def put(self,
            endpoint: str,
            data: Dict[str, Any] = None,
            headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Effectuer une requête PUT.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            endpoint (str): Endpoint de l'API
            data (Dict[str, Any]): Données à envoyer (optionnel)
            headers (Dict[str, str]): En-têtes supplémentaires (optionnel)

        Returns:
            Dict[str, Any]: Réponse de l'API

        Exemples:
            >>> updated_user = client.put("/users/123", data={"name": "John Updated"})
        """
        return self._make_request("PUT", endpoint, data=data, headers=headers)

    def delete(self,
               endpoint: str,
               headers: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Effectuer une requête DELETE.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            endpoint (str): Endpoint de l'API
            headers (Dict[str, str]): En-têtes supplémentaires (optionnel)

        Returns:
            Dict[str, Any]: Réponse de l'API

        Exemples:
            >>> result = client.delete("/users/123")
        """
        return self._make_request("DELETE", endpoint, headers=headers)

    def _get_from_cache(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Récupérer une valeur du cache.

        Args:
            key (str): Clé de cache

        Returns:
            Optional[Dict[str, Any]]: Valeur en cache ou None
        """
        with self._lock:
            if key in self.cache:
                cached_item = self.cache[key]
                if datetime.now() < cached_item['expires_at']:
                    return cached_item['data']
                else:
                    # Expiré, supprimer du cache
                    del self.cache[key]
            return None

    def _set_cache(self,
                   key: str,
                   data: Dict[str, Any],
                   ttl: int = DEFAULT_CACHE_TTL):
        """
        Mettre une valeur en cache.

        Args:
            key (str): Clé de cache
            data (Dict[str, Any]): Données à mettre en cache
            ttl (int): Durée de vie en secondes
        """
        with self._lock:
            self.cache[key] = {
                'data': data,
                'expires_at': datetime.now() + timedelta(seconds=ttl)
            }

    def clear_cache(self):
        """
        Vider le cache des requêtes API.

        Cette méthode supprime toutes les entrées du cache
        et libère la mémoire associée.
        """
        with self._lock:
            self.cache.clear()
            logger.info("Cache API vidé")

    def health_check(self) -> bool:
        """
        Vérifier la santé de l'API.
        """
        try:
            # Essayer une requête simple
            response = self.get("/health", use_cache=False)
            return response['status_code'] == 200
        except Exception as e:
            logger.error(f"Health check échoué: {e}")
            return False

class ServiceRegistry:
    """
    Registre des services disponibles dans l'écosystème.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe maintient un registre des services disponibles
    avec leurs URLs, configurations et statuts de santé.

    Attributs:
        services: Dictionnaire des services enregistrés
        health_check_interval: Intervalle de vérification de santé
        _lock: Verrou pour les opérations thread-safe
    """
    pass

    pass

    def __init__(self):
        """
        Initialiser le registre de services.
        """
        self.services = {}
        self.health_check_interval = 300  # 5 minutes
        self._lock = threading.Lock()

        # Services par défaut
        self._register_default_services()

    def _register_default_services(self):
        """
        Enregistrer les services par défaut de l'écosystème.

        Cette méthode enregistre automatiquement les services
        principaux avec leurs URLs par défaut.
        """
        default_services = {
            'network_scanner': {
                'url': 'http://localhost:8001',
                'description': 'Service de scan réseau',
                'version': '1.0.0',
                'health_endpoint': '/health'
            },
            'darkweb_checker': {
                'url': 'http://localhost:8002',
                'description': 'Service de vérification darkweb',
                'version': '1.0.0',
                'health_endpoint': '/health'
            },
            'social_analyzer': {
                'url': 'http://localhost:8003',
                'description': 'Service d\'analyse des réseaux sociaux',
                'version': '1.0.0',
                'health_endpoint': '/health'
            },
            'identity_guard': {
                'url': 'http://localhost:8004',
                'description': 'Service de protection d\'identité',
                'version': '1.0.0',
                'health_endpoint': '/health'
            },
            'scoring_engine': {
                'url': 'http://localhost:8005',
                'description': 'Moteur de scoring de risque',
                'version': '1.0.0',
                'health_endpoint': '/health'
            }
        }

        for service_name, config in default_services.items():
            self.register_service(service_name, config)

    def register_service(self, name: str, config: Dict[str, Any]):
        """
        Enregistrer un nouveau service.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            name (str): Nom du service
            config (Dict[str, Any]): Configuration du service

        Exemples:
            >>> registry.register_service("new_service", {
            ...     "url": "http://localhost:8006",
            ...     "description": "Nouveau service",
            ...     "version": "1.0.0"
            ... })
        """
        with self._lock:
            self.services[name] = {
                **config, 'registered_at': datetime.now().isoformat(),
                'last_health_check': None,
                'is_healthy': True
            }
            logger.info(
                f"Service enregistré: {name} ({config.get('url', 'N/A')})")

    def get_service(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Obtenir les informations d'un service.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            name (str): Nom du service

        Returns:
            Optional[Dict[str, Any]]: Configuration du service ou None

        Exemples:
            >>> service_config = registry.get_service("network_scanner")
            >>> if service_config:
            >>>     print(f"URL: {service_config['url']}")
        """
        with self._lock:
            return self.services.get(name)

    def get_service_url(self, name: str) -> Optional[str]:
        """
        Obtenir l'URL d'un service.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            name (str): Nom du service

        Returns:
            Optional[str]: URL du service ou None

        Exemples:
            >>> url = registry.get_service_url("network_scanner")
            >>> if url:
            >>>     print(f"Service disponible sur: {url}")
        """
        service = self.get_service(name)
        return service.get('url') if service else None

    def list_services(self) -> List[Dict[str, Any]]:
        """
        Lister tous les services enregistrés.

        Date de création: 2024
        Créateur: bigmoletos

        Returns:
            List[Dict[str, Any]]: Liste des services avec leurs informations

        Exemples:
        """
        with self._lock:
            return [{
                'name': name,
                **config
            } for name, config in self.services.items()]

    def update_service_health(self, name: str, is_healthy: bool):
        """
        Mettre à jour le statut de santé d'un service.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            name (str): Nom du service
            is_healthy (bool): Statut de santé du service

        Exemples:
            >>> registry.update_service_health("network_scanner", True)
        """
        with self._lock:
            if name in self.services:
                self.services[name]['is_healthy'] = is_healthy
                self.services[name]['last_health_check'] = datetime.now(
                ).isoformat()

                status = "en ligne" if is_healthy else "hors ligne"
                logger.info(f"Service {name} {status}")

    def get_healthy_services(self) -> List[str]:
        """
        Obtenir la liste des services en bonne santé.

        Date de création: 2024
        Créateur: bigmoletos

        Returns:
            List[str]: Noms des services en bonne santé

        Exemples:
            >>> healthy_services = registry.get_healthy_services()
            >>> print(f"Services disponibles: {healthy_services}")
        """
        with self._lock:
            return [
                name for name, config in self.services.items()
                if config.get('is_healthy', False)
            ]

class APIMonitor:
    """
    Moniteur de performances des API.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe collecte et analyse les métriques de performance
    des appels API pour identifier les goulots d'étranglement.

    Attributs:
        metrics: Métriques collectées
        slow_request_threshold: Seuil pour les requêtes lentes (secondes)
        _lock: Verrou pour les opérations thread-safe
    """
    pass

    pass

    def __init__(self):
        """
        Initialiser le moniteur API.
        """
        self.metrics = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'slow_requests': 0,
            'total_duration': 0.0,
            'avg_duration': 0.0,
            'max_duration': 0.0,
            'min_duration': float('inf'),
            'requests_by_endpoint': {},
            'requests_by_service': {},
            'error_counts': {}
        }
        self.slow_request_threshold = 2.0  # 2 secondes
        self._lock = threading.Lock()

    def record_request(self, service: str, endpoint: str, method: str,
                       duration: float, status_code: int, success: bool):
        """
        Enregistrer les métriques d'une requête API.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            service (str): Nom du service appelé
            endpoint (str): Endpoint appelé
            method (str): Méthode HTTP
            duration (float): Durée de la requête en secondes
            status_code (int): Code de statut HTTP
            success (bool): True si la requête a réussi

        Exemples:
            >>> monitor.record_request("network_scanner", "/scan", "POST", 1.5, 200, True)
        """
        with self._lock:
            # Métriques générales
            self.metrics['total_requests'] += 1
            self.metrics['total_duration'] += duration

            if success:
                self.metrics['successful_requests'] += 1
            else:
                self.metrics['failed_requests'] += 1

            # Métriques de durée
            if duration > self.metrics['max_duration']:
                self.metrics['max_duration'] = duration
            if duration < self.metrics['min_duration']:
                self.metrics['min_duration'] = duration

            # Calculer la durée moyenne
            self.metrics['avg_duration'] = (self.metrics['total_duration'] /
                                            self.metrics['total_requests'])

            # Compter les requêtes lentes
            if duration > self.slow_request_threshold:
                self.metrics['slow_requests'] += 1
                logger.warning(
                    f"Requête API lente: {service}{endpoint} - {duration:.3f}s"
                )

            # Métriques par endpoint
            endpoint_key = f"{method} {endpoint}"
            if endpoint_key not in self.metrics['requests_by_endpoint']:
                self.metrics['requests_by_endpoint'][endpoint_key] = {
                    'count': 0,
                    'total_duration': 0.0,
                    'errors': 0
                }

            self.metrics['requests_by_endpoint'][endpoint_key]['count'] += 1
            self.metrics['requests_by_endpoint'][endpoint_key][
                'total_duration'] += duration

            if not success:
                self.metrics['requests_by_endpoint'][endpoint_key][
                    'errors'] += 1

            # Métriques par service
            if service not in self.metrics['requests_by_service']:
                self.metrics['requests_by_service'][service] = {
                    'count': 0,
                    'total_duration': 0.0,
                    'errors': 0
                }

            self.metrics['requests_by_service'][service]['count'] += 1
            self.metrics['requests_by_service'][service][
                'total_duration'] += duration

            if not success:
                self.metrics['requests_by_service'][service]['errors'] += 1

            # Compter les erreurs par code de statut
            error_key = str(status_code)
            if error_key not in self.metrics['error_counts']:
                self.metrics['error_counts'][error_key] = 0
            self.metrics['error_counts'][error_key] += 1

    def get_performance_report(self) -> Dict[str, Any]:
        """
        Générer un rapport de performance des API.

        Date de création: 2024
        Créateur: bigmoletos

        Returns:
            Dict[str, Any]: Rapport détaillé des performances

        Exemples:
            >>> report = monitor.get_performance_report()
            >>> print(f"Taux de succès: {report['success_rate']:.2f}%")
        """
        with self._lock:
            total_requests = self.metrics['total_requests']

            return {
                'timestamp': datetime.now().isoformat(),
                'summary': {
                    'total_requests':
                    total_requests,
                    'successful_requests':
                    self.metrics['successful_requests'],
                    'failed_requests':
                    self.metrics['failed_requests'],
                    'success_rate': (self.metrics['successful_requests'] /
                                     max(total_requests, 1) * 100),
                    'avg_response_time':
                    self.metrics['avg_duration'],
                    'max_response_time':
                    self.metrics['max_duration'],
                    'min_response_time':
                    self.metrics['min_duration'],
                    'slow_requests':
                    self.metrics['slow_requests'],
                    'slow_request_rate': (self.metrics['slow_requests'] /
                                          max(total_requests, 1) * 100)
                },
                'by_endpoint': self.metrics['requests_by_endpoint'],
                'by_service': self.metrics['requests_by_service'],
                'error_distribution': self.metrics['error_counts']
            }

# Instance globale du registre de services
_service_registry = None

def get_service_registry() -> ServiceRegistry:
    """
    Obtenir l'instance globale du registre de services.

    Date de création: 2024
    Créateur: bigmoletos

    Returns:
        ServiceRegistry: Instance du registre de services

    Exemples:
        >>> registry = get_service_registry()
        >>> services = registry.list_services()
    """
    global _service_registry

    if _service_registry is None:
        _service_registry = ServiceRegistry()

    return _service_registry

def make_api_request(service_name: str,
                     endpoint: str,
                     method: str = "GET",
                     data: Dict[str, Any] = None,
                     params: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Faire une requête API simple vers un service.

    Date de création: 2024
    Créateur: bigmoletos

    Args:
        service_name (str): Nom du service à appeler
        endpoint (str): Endpoint de l'API
        method (str): Méthode HTTP (défaut: GET)
        data (Dict[str, Any]): Données à envoyer (optionnel)
        params (Dict[str, Any]): Paramètres de requête (optionnel)

    Returns:
        Dict[str, Any]: Réponse de l'API

    Raises:
        APIError: En cas d'erreur

    Exemples:
        >>> response = make_api_request("network_scanner", "/scan", "POST", {"target": "192.168.1.1"})
        >>> users = make_api_request("identity_guard", "/users", "GET", params={"page": 1})
    """
    # Obtenir l'URL du service
    registry = get_service_registry()
    service_url = registry.get_service_url(service_name)

    if not service_url:
        raise APIError(f"Service non trouvé: {service_name}")

    # Créer un client API temporaire
    config = APIConfig(base_url=service_url)
    client = APIClient(config)

    # Effectuer la requête
    if method.upper() == "GET":
        return client.get(endpoint, params=params)
    elif method.upper() == "POST":
        return client.post(endpoint, data=data)
    elif method.upper() == "PUT":
        return client.put(endpoint, data=data)
    elif method.upper() == "DELETE":
        return client.delete(endpoint)
    else:
        raise APIError(f"Méthode HTTP non supportée: {method}")

def validate_api_response(response: Dict[str, Any],
                          expected_status: int = 200,
                          required_fields: List[str] = None) -> bool:
    """
    Valider une réponse API.

    Date de création: 2024
    Créateur: bigmoletos

    Args:
        response (Dict[str, Any]): Réponse API à valider
        expected_status (int): Code de statut attendu (défaut: 200)
        required_fields (List[str]): Champs requis dans la réponse (optionnel)

    Returns:
        bool: True si la réponse est valide

    Exemples:
        >>> response = make_api_request("network_scanner", "/scan")
        >>> if validate_api_response(response, required_fields=["scan_id", "status"]):
        >>>     print("Réponse valide")
    """
    # Vérifier le code de statut
    if response.get('status_code') != expected_status:
        logger.error(
            f"Code de statut incorrect: {response.get('status_code')} != {expected_status}"
        )
        return False

    # Vérifier les champs requis
    if required_fields:
        data = response.get('data', {})
        for field in required_fields:
            if field not in data:
                logger.error(f"Champ requis manquant: {field}")
                return False

    return True

def get_service_url(service_name: str) -> Optional[str]:
    """
    Obtenir l'URL d'un service.

    Date de création: 2024
    Créateur: bigmoletos

    Args:
        service_name (str): Nom du service

    Returns:
        Optional[str]: URL du service ou None

    Exemples:
        >>> url = get_service_url("network_scanner")
        >>> if url:
        >>>     print(f"Service disponible sur: {url}")
    """
    registry = get_service_registry()
    return registry.get_service_url(service_name)

def health_check_services() -> Dict[str, bool]:
    """
    Vérifier la santé de tous les services.

    Date de création: 2024
    Créateur: bigmoletos

    Returns:
        Dict[str, bool]: Statut de santé de chaque service

    Exemples:
        >>> health_status = health_check_services()
        >>> for service, is_healthy in health_status.items():
        >>>     status = "OK" if is_healthy else "KO"
        >>>     print(f"{service}: {status}")
    """
    registry = get_service_registry()
    services = registry.list_services()
    health_status = {}

    for service in services:
        service_name = service['name']
        service_url = service['url']
        health_endpoint = service.get('health_endpoint', '/health')

        try:
            # Créer un client API temporaire
            config = APIConfig(base_url=service_url, timeout=5)
            client = APIClient(config)

            # Vérifier la santé
            response = client.get(health_endpoint, use_cache=False)
            is_healthy = response['status_code'] == 200

            # Mettre à jour le registre
            registry.update_service_health(service_name, is_healthy)
            health_status[service_name] = is_healthy

        except Exception as e:
            logger.error(f"Erreur lors du health check de {service_name}: {e}")
            registry.update_service_health(service_name, False)
            health_status[service_name] = False

    return health_status
