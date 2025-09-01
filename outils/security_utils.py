"""
security_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Utilitaires de sécurité et validation
"""
# Import du module hashlib
import hashlib
# Import du module hmac
import hmac
# Import du module secrets
import secrets
# Import du module string
import string
# Import du module re
import re
# Import du module json
import json
# Import du module base64
import base64
from typing import Dict, Any, Optional, List, Union
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# Import du module os
import os
# Import du module logging
import logging

logger = logging.getLogger(__name__)

class SecurityValidator:
    """
    Validateur de sécurité pour les entrées utilisateur.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe fournit des méthodes pour valider et sanitiser les données
    entrées par les utilisateurs afin de prévenir les attaques par injection
    et les vulnérabilités de sécurité.

    Méthodes principales:
    - validate_email: Validation d'adresses email
    - validate_ip_address: Validation d'adresses IP
    - validate_url: Validation d'URLs
    - validate_phone: Validation de numéros de téléphone
    - sanitize_input: Sanitisation de texte
    - validate_json_schema: Validation selon un schéma JSON

    Attributs:
        EMAIL_PATTERN: Regex pour validation email
        IP_PATTERN: Regex pour validation IP
        URL_PATTERN: Regex pour validation URL
        PHONE_PATTERN: Regex pour validation téléphone
        DANGEROUS_CHARS: Liste des caractères dangereux
    """
    pass

    pass

    # Patterns de validation pour les différents types de données
    EMAIL_PATTERN = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    IP_PATTERN = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    URL_PATTERN = re.compile(r'^https?://[^\s/$.?#].[^\s]*$')
    PHONE_PATTERN = re.compile(r'^\+?[1-9]\d{1,14}$')

    # Caractères dangereux à échapper pour prévenir les injections
    DANGEROUS_CHARS = [
        '<', '>', '"', "'", '&', ';', '(', ')', '{', '}', '[', ']'
    ]

    @classmethod
    def validate_email(cls, email: str) -> bool:
        """
        Valider une adresse email selon les standards RFC.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode vérifie qu'une adresse email respecte le format standard
        avec un nom d'utilisateur, un @ et un domaine valide.

        Args:
            email (str): Adresse email à valider

        Returns:
            bool: True si l'email est valide, False sinon

        Exemples:
            >>> SecurityValidator.validate_email("user@example.com")
            True
            >>> SecurityValidator.validate_email("invalid-email")
            False
        """
        if not email or not isinstance(email, str):
            return False

        # Normaliser l'email (minuscules et suppression des espaces)
        email = email.strip().lower()
        return bool(cls.EMAIL_PATTERN.match(email))

    @classmethod
    def validate_ip_address(cls, ip: str) -> bool:
        """
        Valider une adresse IPv4.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode vérifie qu'une adresse IP respecte le format IPv4
        avec 4 octets entre 0 et 255.

        Args:
            ip (str): Adresse IP à valider

        Returns:
            bool: True si l'IP est valide, False sinon

        Exemples:
            >>> SecurityValidator.validate_ip_address("192.168.1.1")
            True
            >>> SecurityValidator.validate_ip_address("256.1.2.3")
            False
        """
        if not ip or not isinstance(ip, str):
            return False

        return bool(cls.IP_PATTERN.match(ip))

    @classmethod
    def validate_url(cls, url: str) -> bool:
        """
        Valider une URL HTTP/HTTPS.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode vérifie qu'une URL respecte le format HTTP/HTTPS
        avec un protocole, un domaine et un chemin valides.

        Args:
            url (str): URL à valider

        Returns:
            bool: True si l'URL est valide, False sinon

        Exemples:
            >>> SecurityValidator.validate_url("https://example.com")
            True
            >>> SecurityValidator.validate_url("ftp://example.com")
            False
        """
        if not url or not isinstance(url, str):
            return False

        return bool(cls.URL_PATTERN.match(url))

    @classmethod
    def validate_phone(cls, phone: str) -> bool:
        """
        Valider un numéro de téléphone international.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode vérifie qu'un numéro de téléphone respecte le format
        international E.164 avec un code pays et un numéro valide.

        Args:
            phone (str): Numéro de téléphone à valider

        Returns:
            bool: True si le numéro est valide, False sinon

        Exemples:
            >>> SecurityValidator.validate_phone("+33123456789")
            True
            >>> SecurityValidator.validate_phone("0123456789")
            True
        """
        if not phone or not isinstance(phone, str):
            return False

        # Nettoyer le numéro en supprimant espaces, tirets et parenthèses
        clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
        return bool(cls.PHONE_PATTERN.match(clean_phone))

    @classmethod
    def sanitize_input(cls, text: str, max_length: int = 1000) -> str:
        """
        Sanitiser une entrée texte pour prévenir les injections.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode nettoie un texte en échappant les caractères dangereux,
        limitant la longueur et supprimant les caractères de contrôle.

        Args:
            text (str): Texte à sanitiser
            max_length (int): Longueur maximale autorisée (défaut: 1000)

        Returns:
            str: Texte sanitisé et sécurisé

        Exemples:
            >>> SecurityValidator.sanitize_input("<script>alert('xss')</script>")
            "\\<script\\>alert('xss')\\</script\\>"
        """
        if not text or not isinstance(text, str):
            return ""

        # Limiter la longueur pour prévenir les attaques par débordement
        if len(text) > max_length:
            text = text[:max_length]

        # Échapper les caractères dangereux pour prévenir les injections
        for char in cls.DANGEROUS_CHARS:
            text = text.replace(char, f'\\{char}')

        # Supprimer les caractères de contrôle (ASCII < 32)
        text = ''.join(char for char in text if ord(char) >= 32)

        return text.strip()

    @classmethod
    def validate_json_schema(cls, data: Dict[str, Any],
    """
    Valider json schema

    Date de création: 2024
    Créateur: bigmoletos

    Cette fonction effectue les opérations nécessaires pour validate_json_schema.

    Args:
        # Paramètres à documenter

    Returns:
        # Valeur de retour à documenter

    Exemples:
        # Exemples d'utilisation
    """
                             schema: Dict[str, Any]) -> bool:
        """
        Valider des données selon un schéma JSON personnalisé.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode valide un dictionnaire de données selon un schéma
        défini avec types, contraintes et champs requis.

        Args:
            data (Dict[str, Any]): Données à valider
            schema (Dict[str, Any]): Schéma de validation

        Returns:
            bool: True si les données sont valides selon le schéma

        Exemples:
            >>> schema = {
            ...     'email': {'type': 'email', 'required': True},
            ...     'age': {'type': 'integer', 'min': 18, 'max': 100}
            ... }
            >>> data = {'email': 'user@example.com', 'age': 25}
            >>> SecurityValidator.validate_json_schema(data, schema)
            True
        """
        try:
            # Validation basique des types et contraintes
            for field, field_schema in schema.items():
                # Vérifier si le champ est présent
                if field not in data:
                    if field_schema.get('required', False):
                        return False
                    continue

                value = data[field]
                expected_type = field_schema.get('type')

                # Validation selon le type attendu
                if expected_type == 'string':
                    if not isinstance(value, str):
                        return False
                    # Vérifier les contraintes de longueur
                    if 'min_length' in field_schema and len(
                            value) < field_schema['min_length']:
                        return False
                    if 'max_length' in field_schema and len(
                            value) > field_schema['max_length']:
                        return False

                elif expected_type == 'integer':
                    if not isinstance(value, int):
                        return False
                    # Vérifier les contraintes numériques
                    if 'min' in field_schema and value < field_schema['min']:
                        return False
                    if 'max' in field_schema and value > field_schema['max']:
                        return False

                elif expected_type == 'email':
                    if not cls.validate_email(value):
                        return False

                elif expected_type == 'url':
                    if not cls.validate_url(value):
                        return False

            return True

        except Exception as e:
            logger.error(f"Erreur lors de la validation JSON: {e}")
            return False

class CryptoManager:
    """
    Gestionnaire de chiffrement pour les données sensibles.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe utilise Fernet (AES-128) pour le chiffrement symétrique
    et PBKDF2 pour la dérivation de clés sécurisées.

    Attributs:
        cipher (Fernet): Instance Fernet pour le chiffrement/déchiffrement

    Méthodes principales:
        - encrypt: Chiffrer des données
        - decrypt: Déchiffrer des données
        - encrypt_dict: Chiffrer un dictionnaire
        - decrypt_dict: Déchiffrer un dictionnaire

    Exemples:
        >>> crypto = CryptoManager("ma-cle-secrete")
        >>> encrypted = crypto.encrypt("données sensibles")
        >>> decrypted = crypto.decrypt(encrypted)
    """
    pass

        if secret_key is None:
            secret_key = os.getenv('TOKEN_SECRET_KEY', 'default-secret-key')

        self.secret_key = secret_key.encode()

    def generate_token(self,
    """
    Fonction generate_token

    Date de création: 2024
    Créateur: bigmoletos

    Cette fonction effectue les opérations nécessaires pour generate_token.

    Args:
        # Paramètres à documenter

    Returns:
        # Valeur de retour à documenter

    Exemples:
        # Exemples d'utilisation
    """
                       data: Dict[str, Any],
                       expires_in: int = 3600) -> str:
        """
        Générer un token sécurisé.

        Args:
            data: Données à inclure dans le token
            expires_in: Durée de validité en secondes

        Returns:
            Token sécurisé
        """
        # Ajouter l'expiration
        payload = {
            **data, 'exp': datetime.utcnow().timestamp() + expires_in,
            'iat': datetime.utcnow().timestamp()
        }

        # Encoder en base64
        payload_str = json.dumps(payload, ensure_ascii=False)
        payload_b64 = base64.urlsafe_b64encode(payload_str.encode()).decode()

        # Générer la signature
        signature = hmac.new(self.secret_key, payload_b64.encode(),
                             hashlib.sha256).hexdigest()

        return f"{payload_b64}.{signature}"

    def validate_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Valider un token.

        Args:
            token: Token à valider

        Returns:
            Données du token si valide, None sinon
        """
        try:
            if '.' not in token:
                return None

            payload_b64, signature = token.split('.', 1)

            # Vérifier la signature
            expected_signature = hmac.new(self.secret_key,
                                          payload_b64.encode(),
                                          hashlib.sha256).hexdigest()

            if not hmac.compare_digest(signature, expected_signature):
                return None

            # Décoder le payload
            payload_str = base64.urlsafe_b64decode(payload_b64).decode()
            payload = json.loads(payload_str)

            # Vérifier l'expiration
            if 'exp' in payload and payload['exp'] < datetime.utcnow(
            ).timestamp():
                return None

            return payload

        except Exception as e:
            logger.error(f"Erreur lors de la validation du token: {e}")
            return None

    def generate_api_key(self,
    """
    Fonction generate_api_key

    Date de création: 2024
    Créateur: bigmoletos

    Cette fonction effectue les opérations nécessaires pour generate_api_key.

    Args:
        # Paramètres à documenter

    Returns:
        # Valeur de retour à documenter

    Exemples:
        # Exemples d'utilisation
    """
                         user_id: str,
                         permissions: List[str] = None) -> str:
        """
        Générer une clé API.

        Args:
            user_id: ID de l'utilisateur
            permissions: Permissions de la clé API

        Returns:
            Clé API sécurisée
        """
        data = {
            'user_id': user_id,
            'type': 'api_key',
            'permissions': permissions or ['read']
        }

        return self.generate_token(data, expires_in=365 * 24 * 3600)  # 1 an

    def generate_password_reset_token(self, user_id: str) -> str:
        """
        Générer un token de réinitialisation de mot de passe.

        Args:
        """
        __init__

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode effectue les opérations pour __init__.

        Returns:
            # Valeur de retour à documenter
        """
            user_id: ID de l'utilisateur

        Returns:
            Token de réinitialisation
        """
        data = {'user_id': user_id, 'type': 'password_reset'}

        return self.generate_token(data, expires_in=3600)  # 1 heure

class SecurityMonitor:
    """
    Moniteur de sécurité pour détecter les activités suspectes.

    Surveille les tentatives d'accès, les patterns suspects
    et déclenche des alertes si nécessaire.
    """
    pass

    pass

    def __init__(self):
        """Initialiser le moniteur de sécurité."""
        self.failed_attempts = {}  # IP -> [timestamps]
        self.suspicious_ips = set()
        self.rate_limits = {
            'login': {
                'max_attempts': 5,
                'window': 300
            },  # 5 tentatives en 5 minutes
            'api': {
                'max_attempts': 100,
                'window': 3600
            },  # 100 appels en 1 heure
            'scan': {
                'max_attempts': 10,
                'window': 3600
            },  # 10 scans en 1 heure
        }

    def check_rate_limit(self, ip: str, action: str) -> bool:
        """
        Vérifier la limite de taux pour une action.

        Args:
            ip: Adresse IP
            action: Type d'action

        Returns:
            True si l'action est autorisée
        """
        """
        record_attempt

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode effectue les opérations pour record_attempt.

        Returns:
            # Valeur de retour à documenter
        """
        if action not in self.rate_limits:
            return True

        limit = self.rate_limits[action]
        now = datetime.utcnow().timestamp()

        if ip not in self.failed_attempts:
            self.failed_attempts[ip] = []

        # Nettoyer les anciennes tentatives
        self.failed_attempts[ip] = [
            ts for ts in self.failed_attempts[ip] if now - ts < limit['window']
        ]

        # Vérifier la limite
        if len(self.failed_attempts[ip]) >= limit['max_attempts']:
            self.suspicious_ips.add(ip)
            logger.warning(f"Rate limit dépassé pour {ip} - Action: {action}")
            return False

        return True

    def record_attempt(self, ip: str, success: bool, action: str = 'login'):
        """
        Enregistrer une tentative d'accès.

        Args:
            ip: Adresse IP
            success: Succès de la tentative
            action: Type d'action
        """
        if not success:
            if ip not in self.failed_attempts:
                self.failed_attempts[ip] = []

            self.failed_attempts[ip].append(datetime.utcnow().timestamp())

            # Vérifier si l'IP devient suspecte
            if len(self.failed_attempts[ip]) >= 10:
                self.suspicious_ips.add(ip)
                logger.warning(f"IP suspecte détectée: {ip}")

    def is_suspicious_ip(self, ip: str) -> bool:
        """
        Vérifier si une IP est suspecte.

        Args:
            ip: Adresse IP à vérifier

        Returns:
            True si l'IP est suspecte
        """
        return ip in self.suspicious_ips

    def get_security_report(self) -> Dict[str, Any]:
        """
        Générer un rapport de sécurité.

        Returns:
            Rapport de sécurité
        """
        now = datetime.utcnow().timestamp()

        # Nettoyer les anciennes tentatives
        for ip in list(self.failed_attempts.keys()):
            self.failed_attempts[ip] = [
                ts for ts in self.failed_attempts[ip]
                if now - ts < 3600  # Garder 1 heure
            ]
            if not self.failed_attempts[ip]:
                del self.failed_attempts[ip]

        return {
            'suspicious_ips_count':
            len(self.suspicious_ips),
            'suspicious_ips':
            list(self.suspicious_ips),
            'failed_attempts_count':
            len(self.failed_attempts),
            'rate_limited_ips': [
                ip for ip, attempts in self.failed_attempts.items()
                if len(attempts) >= 5
            ]
        }

# Instances globales
security_validator = SecurityValidator()
crypto_manager = CryptoManager()
token_manager = TokenManager()
security_monitor = SecurityMonitor()

# Fonctions utilitaires
def generate_secure_password(length: int = 16) -> str:
    """
    Générer un mot de passe sécurisé.

    Args:
        length: Longueur du mot de passe

    Returns:
        Mot de passe sécurisé
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(length))

def hash_password(password: str) -> str:
    """
    Hasher un mot de passe avec salt.

    Args:
        password: Mot de passe en clair

    Returns:
        Hash du mot de passe
    """
    salt = secrets.token_hex(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(),
                                   100000)
    return f"{salt}${hash_obj.hex()}"

def verify_password(password: str, hashed: str) -> bool:
    """
    Vérifier un mot de passe.

    Args:
        password: Mot de passe en clair
        hashed: Hash du mot de passe

    Returns:
        True si le mot de passe est correct
    """
    try:
        salt, hash_hex = hashed.split('$', 1)
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(),
                                       salt.encode(), 100000)
        return hmac.compare_digest(hash_obj.hex(), hash_hex)
    except Exception:
        return False

def sanitize_filename(filename: str) -> str:
    """
    Sanitiser un nom de fichier.

    Args:
        filename: Nom de fichier à sanitiser

    Returns:
        Nom de fichier sanitisé
    """
    # Supprimer les caractères dangereux
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)

    # Limiter la longueur
    if len(filename) > 255:
        name, ext = os.path.splitext(filename)
        filename = name[:255 - len(ext)] + ext

    return filename

def validate_file_upload(file_data: bytes,
    """
    Valider file upload

    Date de création: 2024
    Créateur: bigmoletos

    Cette fonction effectue les opérations nécessaires pour validate_file_upload.

    Args:
        # Paramètres à documenter

    Returns:
        # Valeur de retour à documenter

    Exemples:
        # Exemples d'utilisation
    """
                         max_size: int = 10 * 1024 * 1024,
                         allowed_extensions: List[str] = None) -> bool:
    """
    Valider un upload de fichier.

    Args:
        file_data: Données du fichier
        max_size: Taille maximale en bytes
        allowed_extensions: Extensions autorisées

    Returns:
        True si le fichier est valide
    """
    # Vérifier la taille
    if len(file_data) > max_size:
        return False

    # Vérifier les signatures de fichiers (magic bytes)
    # Cette fonction peut être étendue pour vérifier les types MIME

    return True
