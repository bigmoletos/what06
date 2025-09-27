# 🚀 **MODOP TECH4ELLES - GUIDE UNIFIÉ**

## 📋 **Vue d'Ensemble du Projet**

**Tech4Elles** est une plateforme de mentoring qui connecte des mentees avec des mentors expérimentés. Le projet utilise une architecture moderne avec AdonisJS (backend) et Svelte (frontend).

---

## 🏗️ **Architecture Technique**

### **Stack Technologique**
- **Backend** : AdonisJS v6+ (Node.js)
- **Frontend** : Svelte (monorepo avec pnpm)
- **Base de données** : PostgreSQL (Docker)
- **Authentification** : Firebase
- **Gestionnaire de paquets** : pnpm

### **Structure du Projet**
```
Tech4Elles/
├── apps/
│   ├── api/          # Backend AdonisJS
│   ├── user/         # App utilisateur Svelte
│   └── admin/        # App admin Svelte
├── packages/
│   ├── ui/           # Composants partagés
│   └── core/         # Types et interfaces
├── docker-compose.dev.yml
└── package.json
```

---

## 🛠️ **Installation et Configuration**

### **Prérequis Système**
- **Windows** : PowerShell 5.1+, Docker Desktop
- **Linux/macOS** : Bash 4.0+, Docker
- **Node.js** : v20.19.4 (Windows) ou v18.19.0 (Linux/macOS)
- **pnpm** : Version 10.15.0+

### **Installation Automatisée**

#### **Windows (PowerShell)**
```powershell
# 1. Installation des outils (en tant qu'administrateur)
.\outils\install_tools.ps1

# 2. Test rapide de l'environnement
.\outils\test_quick.ps1

# 3. Vérification complète
.\outils\check_setup.ps1

# 4. Création du fichier .env
.\outils\create_env_complete.ps1

# 5. Démarrage automatique
.\outils\start_tech4elles.ps1
```

#### **Linux/macOS (Bash)**
```bash
# 1. Installation des outils
chmod +x outils/setup_tech4elles_dev.sh
./outils/setup_tech4elles_dev.sh

# 2. Test rapide
./outils/test_quick.sh

# 3. Démarrage
./outils/start_tech4elles.sh
```

---

## 🚀 **Démarrage de l'Application**

### **Démarrage Automatique (Recommandé)**
```bash
# Depuis le dossier what06
.\outils\start_tech4elles.ps1
```

### **Démarrage Manuel**
```bash
# 1. Démarrer PostgreSQL
cd Tech4Elles
docker compose -f docker-compose.dev.yml up -d

# 2. Lancer l'application
pnpm dev
```

### **URLs de Développement**
- **API Backend** : http://localhost:3333
- **App Utilisateur** : http://localhost:3000
- **App Admin** : http://localhost:3001
- **Base de données** : localhost:5435 (PostgreSQL)

---

## 🔄 **Gestion des Migrations et Seeds**

### **Commandes Essentielles**
```bash
# Naviguer vers l'API
cd Tech4Elles/apps/api

# Vérifier le statut des migrations
node ace migration:status

# Exécuter les migrations en attente
node ace migration:run

# Appliquer les seeds
node ace db:seed

# Annuler la dernière migration
node ace migration:rollback --batch=1
```

### **Quand Relancer les Migrations ?**
- ✅ **Après modification de `admin_seeder.ts`** (changement de mot de passe)
- ✅ **Après ajout de nouvelles migrations**
- ✅ **Après modification du schéma de base**
- ❌ **Pas à chaque démarrage** (risque de perte de données)

### **Workflow de Migration Sécurisé**
```bash
# 1. Vérifier l'état actuel
node ace migration:status

# 2. Si des migrations en attente
node ace migration:run

# 3. Si modification des seeds
node ace db:seed

# 4. Vérifier que tout fonctionne
node ace migration:status
```

---

## 🔐 **Authentification et Accès**

### **Compte Admin par Défaut**
```
Email: admin@yopmail.com
Mot de passe: admin1234 (modifié dans admin_seeder.ts)
```

### **Modification du Mot de Passe Admin**
1. **Éditer** `Tech4Elles/apps/api/database/seeders/admin_seeder.ts`
2. **Changer** la valeur de `password`
3. **Relancer** les seeds : `node ace db:seed`

---

## 🧪 **Tests et Validation**

### **Test Rapide de l'Environnement**
```bash
# Test en 30 secondes
.\outils\test_quick.ps1
```

### **Vérification Complète**
```bash
# Vérification détaillée
.\outils\check_setup.ps1
```

### **Scénarios de Test Recommandés**

#### **1. Connexion Admin**
- Ouvrir http://localhost:3001
- Se connecter avec `admin@yopmail.com` / `admin1234`
- Vérifier l'accès au dashboard

#### **2. API Backend**
- Vérifier http://localhost:3333
- Tester les endpoints d'authentification
- Vérifier la base de données

#### **3. Application Utilisateur**
- Ouvrir http://localhost:3000
- Tester l'inscription/connexion
- Vérifier la navigation

---

## 🚨 **Résolution des Problèmes Courants**

### **Problème : "pnpm n'est pas reconnu"**
```bash
# Solution : Réinstaller pnpm
npm install -g pnpm
```

### **Problème : "Erreur de migration AdonisJS"**
```bash
# Solution : Utiliser Node.js v20+ et les commandes directes
nvm use 20.19.4
cd Tech4Elles/apps/api
node ace migration:run
```

### **Problème : "Base de données non accessible"**
```bash
# Solution : Démarrer PostgreSQL
docker compose -f Tech4Elles/docker-compose.dev.yml up -d
```

### **Problème : "Node.js version incompatible"**
```bash
# Windows
nvm use 20.19.4

# Linux/macOS
nvm use 18.19.0
```

### **Problème : "Mot de passe modifié dans admin_seeder.ts"**
```bash
# Solution : Relancer les seeds pour appliquer les changements
cd Tech4Elles/apps/api
nvm use 20.19.4
node ace db:seed
```

---

## 📁 **Structure des Scripts Outils**

```
outils/
├── 🚀 Scripts d'Installation
│   ├── install_tools.ps1          # Installation Windows
│   └── setup_tech4elles_dev.sh    # Installation Linux/macOS
├── 🔍 Scripts de Vérification
│   ├── check_setup.ps1            # Vérification complète
│   └── test_quick.ps1             # Test rapide
├── 🔧 Scripts de Configuration
│   ├── create_env_complete.ps1    # Création .env
│   └── firebase_setup.ps1         # Configuration Firebase
├── 🚀 Scripts de Démarrage
│   └── start_tech4elles.ps1       # Démarrage automatique
└── 📚 Documentation
    ├── MODOP_FIREBASE.md          # Guide Firebase
    └── GUIDE_FIREBASE_RAPIDE.md   # Guide rapide Firebase
```

---

## 🎯 **Workflow de Développement Recommandé**

```bash
# 1. Vérification rapide
.\outils\test_quick.ps1

# 2. Si des problèmes détectés, installation/réparation
.\outils\install_tools.ps1

# 3. Vérification complète
.\outils\check_setup.ps1

# 4. Configuration
.\outils\create_env_complete.ps1

# 5. Démarrage
.\outils\start_tech4elles.ps1

# 6. Développement !
# L'application est maintenant accessible sur http://localhost:3000
```

---

## 📋 **Checklist de Démarrage Rapide**

- [ ] **Outils installés** : `.\outils\install_tools.ps1` (Windows) ou `./outils/setup_tech4elles_dev.sh` (Linux/macOS)
- [ ] **Test rapide** : `.\outils\test_quick.ps1`
- [ ] **Vérification complète** : `.\outils\check_setup.ps1`
- [ ] **Fichier .env créé** : `.\outils\create_env_complete.ps1`
- [ ] **Application démarrée** : `.\outils\start_tech4elles.ps1`

---

## 💡 **Notes Importantes**

- **Tech4Elles utilise AdonisJS v6+** avec des modules ES6
- **Les commandes s'exécutent avec `node ace`** au lieu d'AdonisJS CLI
- **Node.js v20+ est recommandé** pour Windows (compatibilité optimale)
- **Node.js v18+ est suffisant** pour Linux/macOS
- **pnpm est le gestionnaire de paquets** recommandé pour ce projet
- **Aucun script redondant** - Chaque script a une fonction unique

---

## 🎉 **Résultats Attendus**

Après l'exécution de tous les scripts :
- ✅ **Node.js v20.19.4** (Windows) ou **v18.19.0** (Linux/macOS) actif et compatible
- ✅ **Base de données PostgreSQL** démarrée et accessible
- ✅ **Migrations exécutées** avec succès via `node ace`
- ✅ **Application Tech4Elles** opérationnelle sur http://localhost:3000
- ✅ **API Backend** accessible sur http://localhost:3333

---

**🚀 Prêt à développer avec Tech4Elles !**

---

*Document unifié créé le 29 août 2025 - Remplace tous les autres fichiers de documentation*
