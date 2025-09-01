"""
database_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Ce module contient les tests unitaires et d'intégration pour Cyber Protection Personnalité. Il assure la qualité du code, la couverture de test et la validation des fonctionnalités critiques de cybersécurité.

Classes principales : DatabaseConfig, PostgreSQLManager, RedisManager, DatabaseMonitor, DatabaseBackup
Fonctions principales : monitor_query, get_database_manager, test_database_connection, cleanup_old_backups, wrapper

Exemples d'utilisation :
    - Exécution : python manage.py test outils
    - Test spécifique : python manage.py test database_utils.TestClass.test_method
    - Couverture : coverage run --source='.' manage.py test
    - Rapport : coverage report --html

Dépendances :
    - Imports : os, logging, json, time, typing.Dict, typing.Any, typing.Optional, typing.List, typing.Union, contextlib.contextmanager

Intégration dans l'architecture :
    - CI/CD : Intégration dans le pipeline de déploiement
    - Qualité : Assurance qualité du code
    - Couverture : Métriques de couverture de test
    - Documentation : Tests comme documentation vivante

Ce fichier fait partie intégrante de l'écosystème Cyber Protection Personnalité
et contribue à la sécurité et au monitoring des identités numériques.
"""

"""
database_utils.py

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Gestion des bases de données et connexions
"""

# Import du module os
import os
# Import du module logging
import logging
# Import du module json
import json
# Import du module time
import time
from typing import Dict, Any, Optional, List, Union
from contextlib import contextmanager
from datetime import datetime, timedelta
# Import du module psycopg2
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
# Import du module sqlite3
import sqlite3
# Import du module mysql
import mysql.connector
from mysql.connector import pooling
# Import du module redis
import redis
from redis import ConnectionPool
# Import du module pymongo
import pymongo
from pymongo import MongoClient
# Import du module threading
import threading
from functools import wraps
from pathlib import Path
# Import du module subprocess
import subprocess

logger = logging.getLogger(__name__)

class DatabaseConfig:
    """
    Configuration pour une base de données.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe gère la configuration des différentes bases de données
    utilisées dans l'écosystème Cyber Protection Personnalité.

    Attributs:
        configs (Dict): Dictionnaire des configurations par type de DB
            - postgresql: Configuration PostgreSQL
            - mysql: Configuration MySQL
            - redis: Configuration Redis
            - mongodb: Configuration MongoDB
            - sqlite: Configuration SQLite

    Variables d'environnement supportées:
        - POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
        - MYSQL_HOST, MYSQL_PORT, MYSQL_DB, MYSQL_USER, MYSQL_PASSWORD
        - REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB
        - MONGO_HOST, MONGO_PORT, MONGO_DB, MONGO_USER, MONGO_PASSWORD
        - SQLITE_DB, SQLITE_TIMEOUT
    """
    pass

    pass

    def __init__(self, **kwargs):
        """
        Initialiser la configuration depuis les variables d'environnement.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            **kwargs: Paramètres de configuration optionnels
        """
        self.configs = {
            'postgresql': {
                'host':
                kwargs.get('host', os.getenv('POSTGRES_HOST', 'localhost')),
                'port':
                kwargs.get('port', int(os.getenv('POSTGRES_PORT', 5432))),
                'database':
                kwargs.get('database',
                           os.getenv('POSTGRES_DB', 'cyber_protection')),
                'user':
                kwargs.get('username', os.getenv('POSTGRES_USER', 'postgres')),
                'password':
                kwargs.get('password', os.getenv('POSTGRES_PASSWORD', '')),
                'min_connections':
                int(os.getenv('POSTGRES_MIN_CONN', 1)),
                'max_connections':
                int(os.getenv('POSTGRES_MAX_CONN', 10)),
            },
            'mysql': {
                'host':
                kwargs.get('host', os.getenv('MYSQL_HOST', 'localhost')),
                'port':
                kwargs.get('port', int(os.getenv('MYSQL_PORT', 3306))),
                'database':
                kwargs.get('database', os.getenv('MYSQL_DB',
                                                 'cyber_protection')),
                'user':
                kwargs.get('username', os.getenv('MYSQL_USER', 'root')),
                'password':
                kwargs.get('password', os.getenv('MYSQL_PASSWORD', '')),
                'pool_size':
                int(os.getenv('MYSQL_POOL_SIZE', 5)),
            },
            'redis': {
                'host':
                kwargs.get('host', os.getenv('REDIS_HOST', 'localhost')),
                'port':
                kwargs.get('port', int(os.getenv('REDIS_PORT', 6379))),
                'password':
                kwargs.get('password', os.getenv('REDIS_PASSWORD', None)),
                'db':
                int(os.getenv('REDIS_DB', 0)),
                'max_connections':
                int(os.getenv('REDIS_MAX_CONN', 10)),
            },
            'mongodb': {
                'host':
                kwargs.get('host', os.getenv('MONGO_HOST', 'localhost')),
                'port':
                kwargs.get('port', int(os.getenv('MONGO_PORT', 27017))),
                'database':
                kwargs.get('database', os.getenv('MONGO_DB',
                                                 'cyber_protection')),
                'username':
                kwargs.get('username', os.getenv('MONGO_USER', '')),
                'password':
                kwargs.get('password', os.getenv('MONGO_PASSWORD', '')),
                'max_pool_size':
                int(os.getenv('MONGO_MAX_POOL', 10)),
            },
            'sqlite': {
                'database':
                kwargs.get('database',
                           os.getenv('SQLITE_DB', 'cyber_protection.db')),
                'timeout':
                int(os.getenv('SQLITE_TIMEOUT', 30)),
            }
        }

class PostgreSQLManager:
    """
    Gestionnaire pour PostgreSQL avec pool de connexions.

    Date de création: 2024
    Créateur: bigmoletos

    Cette classe gère les connexions PostgreSQL avec un pool de connexions
    pour optimiser les performances et la gestion des ressources.

    Attributs:
        config (Dict): Configuration de la base de données
        connection_pool (ThreadedConnectionPool): Pool de connexions PostgreSQL

    Méthodes principales:
        - get_connection: Obtenir une connexion du pool
        - execute_query: Exécuter une requête SELECT
        - execute_command: Exécuter une commande INSERT/UPDATE/DELETE
        - execute_many: Exécuter une commande avec plusieurs paramètres
        - close: Fermer le pool de connexions
    """
    pass

    pass

    def __init__(self, config: Dict[str, Any]):
        """
        Initialiser le gestionnaire PostgreSQL.

        Date de création: 2024
        Créateur: bigmoletos

        Args:
            config (Dict[str, Any]): Configuration de la base de données
        """
        self.config = config
        self.connection_pool = None
        self._setup_pool()

    def _setup_pool(self):
        """
        Configurer le pool de connexions PostgreSQL.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode initialise le pool de connexions avec les paramètres
        de configuration spécifiés.
        """
        try:
            self.connection_pool = pool.ThreadedConnectionPool(
                minconn=self.config['min_connections'],
                maxconn=self.config['max_connections'],
                host=self.config['host'],
                port=self.config['port'],
                database=self.config['database'],
                user=self.config['user'],
                password=self.config['password'],
                cursor_factory=RealDictCursor)
            logger.info("Pool de connexions PostgreSQL configuré avec succès")
        except Exception as e:
            logger.error(
                f"Erreur lors de la configuration du pool PostgreSQL: {e}")
            raise

    @contextmanager
    def get_connection(self):
        """
        Obtenir une connexion du pool avec gestion automatique.

        Date de création: 2024
        Créateur: bigmoletos

        Cette méthode utilise un context manager pour gérer automatiquement
        l'obtention et la libération des connexions du pool.

        Yields:
            psycopg2.connection: Connexion PostgreSQL

        Raises:
            Exception: En cas d'erreur de connexion
        """
        conn = None
        try:
            conn = self.connection_pool.getconn()
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Erreur de connexion PostgreSQL: {e}")
            raise
        finally:
            if conn:
                self.connection_pool.putconn(conn)

    def execute_query(self,
                      query: str,
                      params: tuple = None) -> List[Dict[str, Any]]:
        """
        Exécuter une requête SELECT.

        Args:
            query: Requête SQL
            params: Paramètres de la requête

        Returns:
            Résultats de la requête
        """
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return [dict(row) for row in cursor.fetchall()]

    def execute_command(self, command: str, params: tuple = None) -> int:
        """
        Exécuter une commande INSERT/UPDATE/DELETE.
        """
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(command, params)
                conn.commit()
                return cursor.rowcount

    def execute_many(self, command: str, params_list: List[tuple]) -> int:
        """
        Exécuter une commande avec plusieurs paramètres.

        Args:
            command: Commande SQL
            params_list: Liste de paramètres

        Returns:
            Nombre total de lignes affectées
        """
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.executemany(command, params_list)
                conn.commit()
                return cursor.rowcount

    def close(self):
        """Fermer le pool de connexions."""
        if self.connection_pool:
            self.connection_pool.closeall()
            logger.info("Pool de connexions PostgreSQL fermé")

class RedisManager:
    """Gestionnaire pour Redis avec pool de connexions."""
    pass

    pass

    def __init__(self, config: Dict[str, Any]):
        """
        Initialiser le gestionnaire Redis.

        Args:
            config: Configuration Redis
        """
        self.config = config
        self.connection_pool = ConnectionPool(
            host=config['host'],
            port=config['port'],
            password=config['password'],
            db=config['db'],
            max_connections=config['max_connections'])
        self.redis_client = redis.Redis(connection_pool=self.connection_pool)

    def set(self, key: str, value: Any, expire: int = None) -> bool:
        """
        Définir une valeur dans Redis.

        Args:
            key: Clé
            value: Valeur (sera sérialisée en JSON)
            expire: Durée d'expiration en secondes

        Returns:
            True si succès
        """
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            return self.redis_client.set(key, value, ex=expire)
        except Exception as e:
            logger.error(f"Erreur Redis SET: {e}")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """
        Récupérer une valeur depuis Redis.

        Args:
            key: Clé
            default: Valeur par défaut

        Returns:
            Valeur récupérée
        """
        try:
            value = self.redis_client.get(key)
            if value is None:
                return default

            # Essayer de désérialiser en JSON
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value.decode('utf-8')
        except Exception as e:
            logger.error(f"Erreur Redis GET: {e}")
            return default

    def delete(self, key: str) -> bool:
        """
        Supprimer une clé.

        Args:
            key: Clé à supprimer

        Returns:
            True si supprimé
        """
        try:
            return bool(self.redis_client.delete(key))
        except Exception as e:
            logger.error(f"Erreur Redis DELETE: {e}")
            return False

    def exists(self, key: str) -> bool:
        """
        Vérifier si une clé existe.

        Args:
            key: Clé à vérifier

        Returns:
            True si la clé existe
        """
        try:
            return bool(self.redis_client.exists(key))
        except Exception as e:
            logger.error(f"Erreur Redis EXISTS: {e}")
            return False

    def expire(self, key: str, seconds: int) -> bool:
        """
        Définir l'expiration d'une clé.

        Args:
            key: Clé
            seconds: Durée en secondes

        Returns:
            True si succès
        """
        try:
            return bool(self.redis_client.expire(key, seconds))
        except Exception as e:
            logger.error(f"Erreur Redis EXPIRE: {e}")
            return False

class DatabaseMonitor:
    """Moniteur de performance des bases de données."""
    pass

    pass

    def __init__(self):
        """Initialiser le moniteur."""
        self.query_stats = {}
        self.slow_queries = []
        self.connection_stats = {
            'total_connections': 0,
            'active_connections': 0,
            'failed_connections': 0
        }
        self.lock = threading.Lock()

    def record_query(self, query: str, duration: float, success: bool):
        """
        Enregistrer une requête pour les statistiques.

        Args:
            query: Requête SQL
            duration: Durée d'exécution
            success: Succès de la requête
        """
        with self.lock:
            # Statistiques générales
            if query not in self.query_stats:
                self.query_stats[query] = {
                    'count': 0,
                    'total_time': 0,
                    'avg_time': 0,
                    'min_time': float('inf'),
                    'max_time': 0,
                    'errors': 0
                }

            stats = self.query_stats[query]
            stats['count'] += 1
            stats['total_time'] += duration
            stats['avg_time'] = stats['total_time'] / stats['count']
            stats['min_time'] = min(stats['min_time'], duration)
            stats['max_time'] = max(stats['max_time'], duration)

            if not success:
                stats['errors'] += 1

            # Requêtes lentes (> 1 seconde)
            if duration > 1.0:
                self.slow_queries.append({
                    'query':
                    query,
                    'duration':
                    duration,
                    'timestamp':
                    datetime.utcnow().isoformat()
                })

                # Garder seulement les 100 dernières requêtes lentes
                if len(self.slow_queries) > 100:
                    self.slow_queries = self.slow_queries[-100:]

    def record_connection(self, success: bool):
        """
        Enregistrer une tentative de connexion.

        Args:
            success: Succès de la connexion
        """
        with self.lock:
            self.connection_stats['total_connections'] += 1
            if success:
                self.connection_stats['active_connections'] += 1
            else:
                self.connection_stats['failed_connections'] += 1

    def get_performance_report(self) -> Dict[str, Any]:
        """
        Générer un rapport de performance.

        Returns:
            Rapport de performance
        """
        with self.lock:
    return {
                'query_stats': self.query_stats,
                'slow_queries':
                self.slow_queries[-10:],  # 10 dernières requêtes lentes
                'connection_stats': self.connection_stats.copy(),
                'timestamp': datetime.utcnow().isoformat()
            }

# Instance globale du moniteur
db_monitor = DatabaseMonitor()

def monitor_query(func):
    """
    Décorateur pour monitorer les requêtes de base de données.

    Args:
        func: Fonction à décorer

    Returns:
        Fonction décorée avec monitoring
    """
    pass

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        success = False

        try:
            result = func(*args, **kwargs)
            success = True
            return result
        except Exception as e:
            logger.error(f"Erreur de requête dans {func.__name__}: {e}")
            raise
        finally:
            duration = time.time() - start_time
            db_monitor.record_query(func.__name__, duration, success)

    return wrapper

class DatabaseBackup:
    """Gestionnaire de sauvegarde et restauration."""
    pass

    pass

    def __init__(self, db_manager):
        """
        Initialiser le gestionnaire de sauvegarde.

        Args:
            db_manager: Gestionnaire de base de données
        """
        self.db_manager = db_manager
        self.backup_dir = os.getenv('BACKUP_DIR', 'backups')
        os.makedirs(self.backup_dir, exist_ok=True)

    def create_backup(self, backup_name: str = None) -> str:
        """
        Créer une sauvegarde.

        Args:
            backup_name: Nom de la sauvegarde

        Returns:
            Chemin du fichier de sauvegarde
        """
        if backup_name is None:
            backup_name = f"backup_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"

        backup_path = os.path.join(self.backup_dir, f"{backup_name}.sql")

        try:
            # Pour PostgreSQL
            if isinstance(self.db_manager, PostgreSQLManager):
                import subprocess
                cmd = [
                    'pg_dump', '-h', self.db_manager.config['host'], '-p',
                    str(self.db_manager.config['port']), '-U',
                    self.db_manager.config['user'], '-d',
                    self.db_manager.config['database'], '-f', backup_path
                ]

                env = os.environ.copy()
                env['PGPASSWORD'] = self.db_manager.config['password']

                subprocess.run(cmd, env=env, check=True)
                logger.info(f"Sauvegarde créée: {backup_path}")
                return backup_path

            # Pour SQLite
            elif hasattr(self.db_manager, 'database'):
                import shutil
                shutil.copy2(self.db_manager.database, backup_path)
                logger.info(f"Sauvegarde SQLite créée: {backup_path}")
                return backup_path

        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde: {e}")
            raise

        return None

    def restore_backup(self, backup_path: str) -> bool:
        """
        Restaurer une sauvegarde.

        Args:
            backup_path: Chemin du fichier de sauvegarde

        Returns:
            True si succès
        """
        try:
            # Pour PostgreSQL
            if isinstance(self.db_manager, PostgreSQLManager):
                import subprocess
                cmd = [
                    'psql', '-h', self.db_manager.config['host'], '-p',
                    str(self.db_manager.config['port']), '-U',
                    self.db_manager.config['user'], '-d',
                    self.db_manager.config['database'], '-f', backup_path
                ]

                env = os.environ.copy()
                env['PGPASSWORD'] = self.db_manager.config['password']

                subprocess.run(cmd, env=env, check=True)
                logger.info(f"Sauvegarde restaurée: {backup_path}")
                return True

            # Pour SQLite
            elif hasattr(self.db_manager, 'database'):
                import shutil
                shutil.copy2(backup_path, self.db_manager.database)
                logger.info(f"Sauvegarde SQLite restaurée: {backup_path}")
                return True

        except Exception as e:
            logger.error(f"Erreur lors de la restauration: {e}")
            return False

        return False

# Fonctions utilitaires
def get_database_manager(
        db_type: str = None) -> Union[PostgreSQLManager, RedisManager]:
    """
    Obtenir un gestionnaire de base de données.

    Args:
        db_type: Type de base de données (postgresql, redis, etc.)

    Returns:
        Gestionnaire de base de données
    """
    config = DatabaseConfig()

    if db_type == 'postgresql' or db_type is None:
        return PostgreSQLManager(config.configs['postgresql'])
    elif db_type == 'redis':
        return RedisManager(config.configs['redis'])
    else:
        raise ValueError(f"Type de base de données non supporté: {db_type}")

def test_database_connection(db_manager) -> bool:
    """
    Tester la connexion à une base de données.

    Args:
        db_manager: Gestionnaire de base de données

    Returns:
        True si la connexion fonctionne
    """
    try:
        if isinstance(db_manager, PostgreSQLManager):
            with db_manager.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    return True
        elif isinstance(db_manager, RedisManager):
            return db_manager.redis_client.ping()
        else:
            return False
    except Exception as e:
        logger.error(f"Erreur de test de connexion: {e}")
        return False

def cleanup_old_backups(backup_dir: str, days_to_keep: int = 7):
    """
    Nettoyer les anciennes sauvegardes.

    Args:
        backup_dir: Répertoire des sauvegardes
        days_to_keep: Nombre de jours à conserver
    """
    try:
        cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

        for filename in os.listdir(backup_dir):
            file_path = os.path.join(backup_dir, filename)
            if os.path.isfile(file_path):
                file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if file_time < cutoff_date:
                    os.remove(file_path)
                    logger.info(f"Sauvegarde supprimée: {filename}")
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage des sauvegardes: {e}")
