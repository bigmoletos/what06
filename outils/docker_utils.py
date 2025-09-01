"""
docker_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Ce module fournit des utilitaires et fonctions communes pour Cyber Protection Personnalité. Il contient des helpers réutilisables, des fonctions de validation, de formatage et de traitement des données.

Classes principales : DockerManager, DockerComposeManager, DeploymentManager
Fonctions principales : create_docker_compose_file, validate_docker_installation, get_container_health

Exemples d'utilisation :
    - Import : from outils.docker_utils import function_name
    - Utilisation : result = function_name(param1, param2)
    - Intégration : Importé automatiquement par les autres modules
    - Tests : Tests unitaires pour chaque fonction utilitaire

Dépendances :
    - Imports : os, json, time, subprocess, logging, typing.Dict, typing.Any, typing.List, typing.Optional, typing.Tuple

Intégration dans l'architecture :
    - Réutilisabilité : Fonctions partagées entre modules
    - Performance : Optimisations communes
    - Maintenance : Code centralisé et maintenu
    - Tests : Tests unitaires pour chaque utilitaire

Ce fichier fait partie intégrante de l'écosystème Cyber Protection Personnalité
et contribue à la sécurité et au monitoring des identités numériques.
"""

"""
docker_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Configuration Docker
"""

# Import du module os
import os
# Import du module json
import json
# Import du module time
import time
# Import du module subprocess
import subprocess
# Import du module logging
import logging
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
# Import du module yaml
import yaml
from pathlib import Path

logger = logging.getLogger(__name__)

class DockerManager:
    """
    Gestionnaire de conteneurs Docker.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe gère les opérations sur les conteneurs Docker
    avec gestion d'erreurs et monitoring automatique.

    Attributs:
        docker_host (str): Hôte Docker (défaut: unix:///var/run/docker.sock)
        docker_cmd (List[str]): Commande Docker de base

    Méthodes principales:
        - build_image: Construire une image Docker
        - run_container: Lancer un conteneur Docker
        - stop_container: Arrêter un conteneur
        - remove_container: Supprimer un conteneur
        - get_container_status: Obtenir le statut d'un conteneur
        - get_container_logs: Obtenir les logs d'un conteneur
        - list_containers: Lister les conteneurs
        - list_images: Lister les images Docker
    """
    pass

    pass

    def __init__(self, docker_host: str = None):
        """
        Initialiser le gestionnaire Docker.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            docker_host (str): Hôte Docker (optionnel, utilise la variable d'environnement par défaut)
        """
        self.docker_host = docker_host or os.getenv(
            'DOCKER_HOST', 'unix:///var/run/docker.sock')
        self.docker_cmd = ['docker']

        if self.docker_host != 'unix:///var/run/docker.sock':
            self.docker_cmd.extend(['-H', self.docker_host])

    def _run_command(self,
                     cmd: List[str],
                     capture_output: bool = True) -> Tuple[int, str, str]:
        """
        Exécuter une commande Docker.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode exécute une commande Docker avec gestion des erreurs
        et des timeouts.

        Args:
            cmd (List[str]): Commande à exécuter
            capture_output (bool): Capturer la sortie (défaut: True)

        Returns:
            Tuple[int, str, str]: (code_retour, stdout, stderr)

        Raises:
            subprocess.TimeoutExpired: En cas de timeout
            Exception: En cas d'erreur d'exécution
        """
        full_cmd = self.docker_cmd + cmd

        try:
            if capture_output:
                result = subprocess.run(
                    full_cmd,
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minutes timeout
                )
                return result.returncode, result.stdout, result.stderr
            else:
                result = subprocess.run(full_cmd, timeout=300)
                return result.returncode, "", ""
        except subprocess.TimeoutExpired:
            logger.error(
                f"Timeout lors de l'exécution de la commande: {' '.join(full_cmd)}"
            )
            return -1, "", "Timeout"
        except Exception as e:
            logger.error(f"Erreur lors de l'exécution de la commande: {e}")
            return -1, "", str(e)

    def build_image(self,
                    dockerfile_path: str,
                    image_name: str,
                    tag: str = "latest",
                    build_args: Dict[str, str] = None) -> bool:
        """
        Construire une image Docker.

        Args:
            dockerfile_path: Chemin vers le Dockerfile
            image_name: Nom de l'image
            tag: Tag de l'image
            build_args: Arguments de build

        Returns:
            True si succès
        """
        cmd = ['build', '-t', f"{image_name}:{tag}"]

        if build_args:
            for key, value in build_args.items():
                cmd.extend(['--build-arg', f"{key}={value}"])

        cmd.append(dockerfile_path)

        logger.info(f"Construction de l'image {image_name}:{tag}")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info(f"Image {image_name}:{tag} construite avec succès")
            return True
        else:
            logger.error(f"Erreur lors de la construction: {stderr}")
            return False

    def run_container(self,
                      image: str,
                      container_name: str = None,
                      ports: Dict[str, str] = None,
                      volumes: Dict[str, str] = None,
                      environment: Dict[str, str] = None,
                      detach: bool = True) -> str:
        """
        Lancer un conteneur Docker.

        Args:
            image: Image à utiliser
            container_name: Nom du conteneur
            ports: Mapping des ports (host:container)
            volumes: Mapping des volumes (host:container)
            environment: Variables d'environnement
            detach: Lancer en arrière-plan

        Returns:
            ID du conteneur
        """
        cmd = ['run']

        if detach:
            cmd.append('-d')

        if container_name:
            cmd.extend(['--name', container_name])

        if ports:
            for host_port, container_port in ports.items():
                cmd.extend(['-p', f"{host_port}:{container_port}"])

        if volumes:
            for host_path, container_path in volumes.items():
                cmd.extend(['-v', f"{host_path}:{container_path}"])

        if environment:
            for key, value in environment.items():
                cmd.extend(['-e', f"{key}={value}"])

        cmd.append(image)

        logger.info(f"Lancement du conteneur {container_name or image}")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            container_id = stdout.strip()
            logger.info(f"Conteneur lancé: {container_id}")
            return container_id
        else:
            logger.error(f"Erreur lors du lancement: {stderr}")
            return ""

    def stop_container(self, container_id: str) -> bool:
        """
        Arrêter un conteneur.

        Args:
            container_id: ID ou nom du conteneur

        Returns:
            True si succès
        """
        cmd = ['stop', container_id]

        logger.info(f"Arrêt du conteneur {container_id}")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info(f"Conteneur {container_id} arrêté")
            return True
        else:
            logger.error(f"Erreur lors de l'arrêt: {stderr}")
            return False

    def remove_container(self, container_id: str, force: bool = False) -> bool:
        """
        Supprimer un conteneur.

        Args:
            container_id: ID ou nom du conteneur
            force: Forcer la suppression

        Returns:
            True si succès
        """
        cmd = ['rm']
        if force:
            cmd.append('-f')
        cmd.append(container_id)

        logger.info(f"Suppression du conteneur {container_id}")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info(f"Conteneur {container_id} supprimé")
            return True
        else:
            logger.error(f"Erreur lors de la suppression: {stderr}")
            return False

    def get_container_status(self, container_id: str) -> Dict[str, Any]:
        """
        Obtenir le statut d'un conteneur.

        Args:
            container_id: ID ou nom du conteneur

        Returns:
            Informations sur le conteneur
        """
        cmd = ['inspect', container_id]

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            try:
                container_info = json.loads(stdout)
                if container_info:
                    return container_info[0]
            except json.JSONDecodeError:
                logger.error(
                    "Erreur lors du parsing des informations du conteneur")

        return {}

    def get_container_logs(self, container_id: str, tail: int = 100) -> str:
        """
        Obtenir les logs d'un conteneur.

        Args:
            container_id: ID ou nom du conteneur
            tail: Nombre de lignes à récupérer

        Returns:
            Logs du conteneur
        """
        cmd = ['logs', '--tail', str(tail), container_id]

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            return stdout
        else:
            logger.error(f"Erreur lors de la récupération des logs: {stderr}")
            return ""

    def list_containers(self,
                        all_containers: bool = False) -> List[Dict[str, Any]]:
        """
        Lister les conteneurs.

        Args:
            all_containers: Inclure les conteneurs arrêtés

        Returns:
            Liste des conteneurs
        """
        cmd = ['ps', '--format', 'json']
        if all_containers:
            cmd.append('-a')

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            try:
                containers = []
                for line in stdout.strip().split('\n'):
                    if line:
                        containers.append(json.loads(line))
                return containers
            except json.JSONDecodeError:
                logger.error(
                    "Erreur lors du parsing de la liste des conteneurs")

        return []

    def list_images(self) -> List[Dict[str, Any]]:
        """
        Lister les images Docker.

        Returns:
            Liste des images
        """
        cmd = ['images', '--format', 'json']

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            try:
                images = []
                for line in stdout.strip().split('\n'):
                    if line:
                        images.append(json.loads(line))
                return images
            except json.JSONDecodeError:
                logger.error("Erreur lors du parsing de la liste des images")

        return []

class DockerComposeManager:
    """Gestionnaire pour Docker Compose."""
    pass

    pass

    def __init__(self, compose_file: str = "docker-compose.yml"):
        """
        Initialiser le gestionnaire Docker Compose.

        Args:
            compose_file: Fichier docker-compose.yml
        """
        self.compose_file = compose_file
        self.compose_cmd = ['docker-compose', '-f', compose_file]

    def _run_command(self,
                     cmd: List[str],
                     capture_output: bool = True) -> Tuple[int, str, str]:
        """
        Exécuter une commande Docker Compose.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode exécute une commande Docker Compose avec gestion des erreurs
        et des timeouts.

        Args:
            cmd (List[str]): Commande à exécuter
            capture_output (bool): Capturer la sortie (défaut: True)

        Returns:
            Tuple[int, str, str]: (code_retour, stdout, stderr)

        Raises:
            subprocess.TimeoutExpired: En cas de timeout
            Exception: En cas d'erreur d'exécution
        """
        full_cmd = self.compose_cmd + cmd

        try:
            if capture_output:
                result = subprocess.run(
                    full_cmd,
                    capture_output=True,
                    text=True,
                    timeout=600  # 10 minutes timeout
                )
                return result.returncode, result.stdout, result.stderr
            else:
                result = subprocess.run(full_cmd, timeout=600)
                return result.returncode, "", ""
        except subprocess.TimeoutExpired:
            logger.error(
                f"Timeout lors de l'exécution de la commande: {' '.join(full_cmd)}"
            )
            return -1, "", "Timeout"
        except Exception as e:
            logger.error(f"Erreur lors de l'exécution de la commande: {e}")
            return -1, "", str(e)

    def up(self,
           services: List[str] = None,
           detach: bool = True,
           build: bool = False) -> bool:
        """
        Démarrer les services.

        Args:
            services: Services spécifiques à démarrer
            detach: Lancer en arrière-plan
            build: Reconstruire les images

        Returns:
            True si succès
        """
        cmd = ['up']

        if detach:
            cmd.append('-d')

        if build:
            cmd.append('--build')

        if services:
            cmd.extend(services)

        logger.info(f"Démarrage des services Docker Compose")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info("Services démarrés avec succès")
            return True
        else:
            logger.error(f"Erreur lors du démarrage: {stderr}")
            return False

    def down(self, remove_volumes: bool = False) -> bool:
        """
        Arrêter les services.

        Args:
            remove_volumes: Supprimer les volumes

        Returns:
            True si succès
        """
        cmd = ['down']

        if remove_volumes:
            cmd.append('-v')

        logger.info("Arrêt des services Docker Compose")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info("Services arrêtés avec succès")
            return True
        else:
            logger.error(f"Erreur lors de l'arrêt: {stderr}")
            return False

    def restart(self, services: List[str] = None) -> bool:
        """
        Redémarrer les services.

        Args:
            services: Services spécifiques à redémarrer

        Returns:
            True si succès
        """
        cmd = ['restart']

        if services:
            cmd.extend(services)

        logger.info("Redémarrage des services Docker Compose")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info("Services redémarrés avec succès")
            return True
        else:
            logger.error(f"Erreur lors du redémarrage: {stderr}")
            return False

    def logs(self,
             services: List[str] = None,
             tail: int = 100,
             follow: bool = False) -> str:
        """
        Obtenir les logs des services.

        Args:
            services: Services spécifiques
            tail: Nombre de lignes à récupérer
            follow: Suivre les logs en temps réel

        Returns:
            Logs des services
        """
        cmd = ['logs', '--tail', str(tail)]

        if follow:
            cmd.append('-f')

        if services:
            cmd.extend(services)

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            return stdout
        else:
            logger.error(f"Erreur lors de la récupération des logs: {stderr}")
            return ""

    def ps(self) -> List[Dict[str, Any]]:
        """
        Obtenir le statut des services.

        Returns:
            Statut des services
        """
        cmd = ['ps', '--format', 'json']

        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            try:
                services = []
                for line in stdout.strip().split('\n'):
                    if line:
                        services.append(json.loads(line))
                return services
            except json.JSONDecodeError:
                logger.error("Erreur lors du parsing du statut des services")

        return []

    def scale(self, service: str, replicas: int) -> bool:
        """
        Mettre à l'échelle un service.

        Args:
            service: Nom du service
            replicas: Nombre de réplicas

        Returns:
            True si succès
        """
        cmd = ['scale', f"{service}={replicas}"]

        logger.info(
            f"Mise à l'échelle du service {service} à {replicas} réplicas")
        returncode, stdout, stderr = self._run_command(cmd)

        if returncode == 0:
            logger.info(f"Service {service} mis à l'échelle avec succès")
            return True
        else:
            logger.error(f"Erreur lors de la mise à l'échelle: {stderr}")
            return False

class DeploymentManager:
    """Gestionnaire de déploiement automatique."""
    pass

    pass

    def __init__(self, project_root: str):
        """
        Initialiser le gestionnaire de déploiement.

        Args:
            project_root: Racine du projet
        """
        self.project_root = Path(project_root)
        self.docker_manager = DockerManager()
        self.services = {}
        self._load_services()

    def _load_services(self):
        """Charger la configuration des services."""
        services_dir = self.project_root / "services"

        if services_dir.exists():
            for service_dir in services_dir.iterdir():
                if service_dir.is_dir():
                    dockerfile = service_dir / "Dockerfile"
                    compose_file = service_dir / "docker-compose.yml"

                    if dockerfile.exists():
                        self.services[service_dir.name] = {
                            'path':
                            service_dir,
                            'dockerfile':
                            dockerfile,
                            'compose_file':
                            compose_file if compose_file.exists() else None
                        }

    def build_all_services(self, tag: str = "latest") -> Dict[str, bool]:
        """
        Construire toutes les images des services.

        Args:
            tag: Tag des images

        Returns:
            Résultats de construction par service
        """
        results = {}

        for service_name, service_config in self.services.items():
            logger.info(f"Construction du service {service_name}")

            success = self.docker_manager.build_image(
                str(service_config['dockerfile'].parent),
                f"cyber-protection-{service_name}", tag)

            results[service_name] = success

        return results

    def deploy_service(self,
                       service_name: str,
                       environment: str = "development") -> bool:
        """
        Déployer un service spécifique.

        Args:
            service_name: Nom du service
            environment: Environnement de déploiement

        Returns:
            True si succès
        """
        if service_name not in self.services:
            logger.error(f"Service {service_name} non trouvé")
            return False

        service_config = self.services[service_name]

        # Construire l'image
        image_name = f"cyber-protection-{service_name}"
        if not self.docker_manager.build_image(
                str(service_config['dockerfile'].parent), image_name,
                environment):
            return False

        # Lancer le conteneur
        container_name = f"{service_name}-{environment}"

        # Configuration par défaut
        ports = {f"800{self._get_service_port(service_name)}": "8000"}
        volumes = {
            str(service_config['path'] / "logs"): "/app/logs",
            str(self.project_root / ".env"): "/app/.env"
        }
        environment_vars = {
            "DJANGO_ENV": environment,
            "SERVICE_NAME": service_name
        }

        container_id = self.docker_manager.run_container(
            f"{image_name}:{environment}", container_name, ports, volumes,
            environment_vars)

        return bool(container_id)

    def _get_service_port(self, service_name: str) -> int:
        """Obtenir le port par défaut d'un service."""
        port_mapping = {
            'darkweb_checker': 1,
            'social_analyzer': 2,
            'network_scanner': 3,
            'identity_guard': 4,
            'scoring_engine': 5
        }
        return port_mapping.get(service_name, 0)

    def deploy_all_services(self,
                            environment: str = "development"
                            ) -> Dict[str, bool]:
        """
        Déployer tous les services.

        Args:
            environment: Environnement de déploiement

        Returns:
            Résultats de déploiement par service
        """
        results = {}

        for service_name in self.services:
            results[service_name] = self.deploy_service(
                service_name, environment)

        return results

    def get_deployment_status(self) -> Dict[str, Any]:
        """
        Obtenir le statut du déploiement.

        Returns:
            Statut des services déployés
        """
        containers = self.docker_manager.list_containers(all_containers=True)
        status = {}

        for container in containers:
            container_name = container.get('Names', [''])[0]
            for service_name in self.services:
                if service_name in container_name:
                    status[service_name] = {
                        'container_id': container.get('ID'),
                        'status': container.get('Status'),
                        'ports': container.get('Ports', ''),
                        'created': container.get('CreatedAt')
                    }

        return status

    def cleanup_old_images(self, keep_tags: List[str] = None) -> bool:
        """
        Nettoyer les anciennes images.

        Args:
            keep_tags: Tags à conserver

        Returns:
            True si succès
        """
        if keep_tags is None:
            keep_tags = ['latest', 'development', 'staging', 'production']

        images = self.docker_manager.list_images()

        for image in images:
            image_name = image.get('Repository', '')
            image_tag = image.get('Tag', '')

            # Nettoyer les images du projet
            if image_name.startswith('cyber-protection-'):
                if image_tag not in keep_tags:
                    logger.info(
                        f"Suppression de l'image {image_name}:{image_tag}")
                    # Implémenter la suppression d'image

        return True

# Fonctions utilitaires
def create_docker_compose_file(
        services: List[Dict[str, Any]],
        output_file: str = "docker-compose.yml") -> bool:
    """
    Créer un fichier docker-compose.yml.

    Args:
        services: Configuration des services
        output_file: Fichier de sortie

    Returns:
        True si succès
    """
    compose_config = {'version': '3.8', 'services': {}}

    for service in services:
        service_name = service['name']
        compose_config['services'][service_name] = {
            'build': {
                'context': f"./services/{service_name}",
                'dockerfile': 'Dockerfile'
            },
            'ports': [f"{service['port']}:8000"],
            'environment': service.get('environment', []),
            'volumes': service.get('volumes', []),
            'depends_on': service.get('depends_on', []),
            'restart': service.get('restart', 'unless-stopped')
        }

    try:
        with open(output_file, 'w') as f:
            yaml.dump(compose_config, f, default_flow_style=False)

        logger.info(f"Fichier docker-compose.yml créé: {output_file}")
        return True
    except Exception as e:
        logger.error(
            f"Erreur lors de la création du fichier docker-compose.yml: {e}")
        return False

def validate_docker_installation() -> bool:
    """
    Valider l'installation de Docker.

    Returns:
        True si Docker est installé et fonctionnel
    """
    try:
        result = subprocess.run(['docker', '--version'],
                                capture_output=True,
                                text=True)
        if result.returncode == 0:
            logger.info(f"Docker installé: {result.stdout.strip()}")
            return True
        else:
            logger.error("Docker non installé ou non accessible")
            return False
    except FileNotFoundError:
        logger.error("Docker non trouvé dans le PATH")
        return False

def get_container_health(container_id: str) -> Dict[str, Any]:
    """
    Obtenir l'état de santé d'un conteneur.

    Args:
        container_id: ID du conteneur

    Returns:
        Informations de santé
    """
    docker_manager = DockerManager()
    container_info = docker_manager.get_container_status(container_id)

    if not container_info:
        return {'status': 'unknown', 'healthy': False}

    state = container_info.get('State', {})
    health = state.get('Health', {})

    return {
        'status': state.get('Status', 'unknown'),
        'running': state.get('Running', False),
        'healthy': health.get('Status') == 'healthy',
        'restart_count': state.get('RestartCount', 0),
        'started_at': state.get('StartedAt'),
        'finished_at': state.get('FinishedAt')
    }
