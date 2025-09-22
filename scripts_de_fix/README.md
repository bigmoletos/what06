# 🔧 Scripts de Fix et Test - Tech4Elles

## 📁 Dossier des Scripts de Diagnostic et Correction

Ce dossier contient tous les scripts de test, diagnostic, fix et debug créés pour le projet Tech4Elles.

## 📝 Convention de Nommage

Les scripts suivent la convention :
```
[type]_[fonctionnalité]_[timestamp].ps1
```

### Types de Scripts :
- **test_** : Scripts de test API, fonctionnalités, données
- **fix_** : Scripts de correction et réparation
- **debug_** : Scripts de diagnostic et debug
- **diagnostic_** : Scripts d'analyse système
- **setup_** : Scripts de configuration et installation

### Exemples :
- `test_api_complete_2025-09-21_182400.ps1`
- `fix_notifications_sync_2025-09-21_182400.ps1`
- `debug_chatrooms_messages_2025-09-21_182400.ps1`

## 📊 Scripts Disponibles

### Scripts de Test API
- `test_api_complete_2025-09-21_182400.ps1` - Test complet de l'API avec authentification
- `test_notifications_clean.ps1` - Test des notifications sans emojis
- `test_mentor_specific.ps1` - Test des données mentor spécifiques
- `test_login_simple.ps1` - Test de connexion simple

### Scripts de Test Fonctionnalités
- `test_connexion.ps1` - Test de connexion utilisateurs
- `test_logout_redirect.ps1` - Test de redirection logout
- `test_landing_access.ps1` - Test d'accès page landing

### Scripts de Test Données
- `test_create_mentee.ps1` - Test création mentee
- `test_registration_correct.ps1` - Test inscription corrigé
- `test_admin_postgres.ps1` - Test admin et PostgreSQL

### Scripts de Diagnostic
- `test_kabia_access.html` - Interface de diagnostic base Kabia

## 🚀 Utilisation

### Prérequis
- PowerShell 5.0 ou supérieur
- API Tech4Elles démarrée sur localhost:3333
- PostgreSQL en fonctionnement

### Exécution
```powershell
# Depuis le dossier what06
PowerShell -ExecutionPolicy Bypass -File ".\scripts_de_fix\[nom_du_script].ps1"

# Exemple
PowerShell -ExecutionPolicy Bypass -File ".\scripts_de_fix\test_api_complete_2025-09-21_182400.ps1"
```

### Logs
Tous les scripts génèrent automatiquement des logs dans :
```
C:\programmation\Projets_python\what06\syntheses_analyses_cursor\
```

## 📋 Règles de Création

### 1. En-tête Obligatoire
Chaque script doit contenir :
```powershell
# =============================================================================
# [TYPE] [DESCRIPTION] - Tech4Elles
# =============================================================================
# Objectif : [Description claire]
# Date     : [Date de création]
# Auteur   : Assistant IA Cursor
# Usage    : [Commande d'exécution]
# =============================================================================
```

### 2. Logging Automatique
```powershell
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$logFile = "C:\programmation\Projets_python\what06\syntheses_analyses_cursor\[nom]_results_${timestamp}.txt"
Start-Transcript -Path $logFile -Append
```

### 3. Gestion d'Erreurs
```powershell
function Test-ApiEndpoint {
    param([string]$Name, [string]$Method, [string]$Url, [hashtable]$Headers = @{}, [string]$Body = $null)
    try {
        # Code de test
        Write-Host "✅ SUCCESS: $Name" -ForegroundColor Green
        return $response
    }
    catch {
        Write-Host "❌ ERREUR: $Name - $($_.Exception.Message)" -ForegroundColor Red
        return $null
    }
}
```

### 4. Code de Sortie
```powershell
if ($success) {
    exit 0  # Succès
} else {
    exit 1  # Échec
}
```

## 🎯 Maintenance

### Nettoyage Périodique
- Archiver les scripts de plus de 30 jours
- Supprimer les scripts obsolètes
- Mettre à jour les scripts avec de nouvelles fonctionnalités

### Versionning
- Conserver toujours la version la plus récente
- Archiver les versions importantes
- Documenter les changements majeurs

## 📞 Support

Pour toute question sur l'utilisation des scripts :
1. Vérifier les logs générés automatiquement
2. Consulter la documentation dans les en-têtes
3. Vérifier les prérequis (API, PostgreSQL, etc.)

---
*Dernière mise à jour : 21/09/2025 18:24:00*


