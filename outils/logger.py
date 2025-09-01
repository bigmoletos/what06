"""
logger.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Système de logging centralisé pour CyberProtect360
"""

import logging
import logging.handlers
import os
import sys
import json
import re
from datetime import datetime
from typing import Optional, Dict, Any
from pathlib import Path
from functools import wraps


class SecurityFormatter(logging.Formatter):
    """Formateur sécurisé pour les logs de sécurité"""

    def format(self, record):
        """Formate le record en masquant les données sensibles"""
        message = record.getMessage()

        # Masquer les données sensibles de manière simple
        sensitive_patterns = [(r'password[=:]\s*\S+', 'password=***MASKED***'),
                              (r'api_key[=:]\s*\S+', 'api_key=***MASKED***'),
                              (r'token[=:]\s*\S+', 'token=***MASKED***'),
                              (r'secret[=:]\s*\S+', 'secret=***MASKED***')]

        for pattern, replacement in sensitive_patterns:
            message = re.sub(pattern,
                             replacement,
                             message,
                             flags=re.IGNORECASE)

        record.msg = message
        return super().format(record)


class JsonFormatter(logging.Formatter):
    """Formateur JSON pour les logs structurés"""

    def format(self, record):
        """Formate le record en JSON"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage()
        }
        return json.dumps(log_entry, ensure_ascii=False)


def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    """
    Obtient un logger configuré.

    Args:
        name: Nom du logger
        level: Niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
        Logger configuré
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # Éviter les handlers dupliqués
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = SecurityFormatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_database_operation(operation: str):
    """
    Décorateur pour logger les opérations de base de données.

    Args:
        operation: Type d'opération (SELECT, INSERT, UPDATE, DELETE)
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = get_logger(f"{func.__module__}.database")

            # Log de début d'opération
            start_time = datetime.now()
            logger.debug(
                f"DB {operation.upper()}: {func.__name__} avec args={args}")

            try:
                # Exécuter l'opération
                result = func(*args, **kwargs)

                # Log de fin d'opération
                duration = (datetime.now() - start_time).total_seconds()
                logger.info(
                    f"DB {operation.upper()} réussi: {func.__name__} en {duration:.3f}s"
                )

                return result

            except Exception as e:
                # Log d'erreur
                duration = (datetime.now() - start_time).total_seconds()
                logger.error(
                    f"DB {operation.upper()} échoué: {func.__name__} après {duration:.3f}s"
                )
                logger.error(f"Erreur: {str(e)}")
                raise

        return wrapper

    return decorator


def setup_django_logging():
    """
    Configurer le logging pour Django.

    Cette fonction configure le logging Django pour utiliser
    le système de logging centralisé avec formatage sécurisé.
    """
    # Configuration du logging Django
    django_logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'security': {
                '()': SecurityFormatter,
                'format':
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'json': {
                '()': JsonFormatter,
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'logs/django.log',
                'maxBytes': 10 * 1024 * 1024,  # 10 MB
                'backupCount': 5,
                'formatter': 'security',
                'encoding': 'utf-8',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'json',
            },
            'security_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'logs/django_security.log',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 5,
                'formatter': 'security',
                'encoding': 'utf-8',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['security_file'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }

    # Appliquer la configuration
    logging.config.dictConfig(django_logging_config)
