<!--
README.md

Date de création : 2025-07-05
Version : 1.0.0
Créateur : bigmoletos

Description :
    Documentation principale du projet
-->

# Outils réutilisables

Ce dossier contient tous les utilitaires réutilisables dans les microservices.

## Modules disponibles

### logger.py
- `get_logger(name)`: Retourne un logger configuré
- Utilisation: `from outils.logger import get_logger`

### security_utils.py
- `validate_email(email)`: Valide le format d'un email
- `hash_sensitive_data(data)`: Hache les données sensibles
- `generate_secure_token(length)`: Génère un token sécurisé
- `sanitize_input(input_str)`: Nettoie les entrées utilisateur

### api_utils.py
- `api_success_response(data, message, status_code)`: Réponse API de succès
- `api_error_response(message, errors, status_code)`: Réponse API d'erreur
- `validate_required_fields(data, required_fields)`: Valide les champs requis

### database_utils.py
- `get_database_config()`: Configuration DB depuis env vars
- `create_fake_data(model_class, data_list)`: Crée des données fictives
- `bulk_create_or_update(model_class, data_list, unique_fields)`: Création/mise à jour en lot

### docker_utils.py
- `get_docker_env_vars()`: Variables d'environnement Docker
- `get_docker_volumes(service_name)`: Volumes Docker standardisés
- `get_docker_ports(service_name, default_port)`: Mapping de ports
- `get_docker_command(service_name)`: Commande Docker standardisée

## Philosophie as-code
Tous ces outils sont versionnés et réutilisables, évitant la duplication de code entre microservices.