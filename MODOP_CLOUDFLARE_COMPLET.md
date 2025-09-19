# 🚀 **GUIDE COMPLET CLOUDFLARE - TECH4ELLES**

## 📋 **TABLE DES MATIÈRES**
1. [Inscription et Configuration Compte](#inscription)
2. [Configuration DNS et Domaine](#dns)
3. [Création des Tokens API](#tokens)
4. [Configuration Cloudflare Pages](#pages)
5. [Connexion GitHub](#github)
6. [Configuration des Workflows](#workflows)
7. [Configuration Firebase](#firebase)
8. [Tests et Validation](#tests)
9. [Monitoring et Maintenance](#monitoring)
10. [Troubleshooting](#troubleshooting)

---

## **1. 🔐 INSCRIPTION ET CONFIGURATION COMPTE**

### **Étape 1.1 : Créer un Compte Cloudflare**
1. Aller sur [cloudflare.com](https://cloudflare.com)
2. Cliquer sur **"Sign Up"**
3. Entrer votre email et mot de passe
4. Vérifier votre email

### **Étape 1.2 : Ajouter votre Domaine**
1. Dans le dashboard, cliquer **"Add a Site"**
2. Entrer **`tech4elles.com`**
3. Choisir le plan **Free** (suffisant pour commencer)
4. Cloudflare va scanner vos DNS existants

### **Étape 1.3 : Configuration Initiale**
1. **Choisir le plan** : Free (0€/mois)
2. **Scanner DNS** : Cloudflare détecte automatiquement
3. **Changer les nameservers** : Suivre les instructions
4. **Activer Cloudflare** : Cliquer sur "Continue"

---

## **2. 🌐 CONFIGURATION DNS ET DOMAINE**

### **Étape 2.1 : Configuration DNS de Base**
```
Type    Name                    Content                 TTL     Proxy
A       tech4elles.com          [IP_SERVEUR]            Auto    ✅
CNAME   www.tech4elles.com      tech4elles.com          Auto    ✅
CNAME   api.tech4elles.com      [IP_API]                Auto    ✅
CNAME   admin.tech4elles.com    tech4elles.com          Auto    ✅
```

### **Étape 2.2 : Configuration SSL**
1. Aller dans **SSL/TLS** → **Overview**
2. Choisir **"Full (strict)"** pour la sécurité maximale
3. Activer **"Always Use HTTPS"**
4. Configurer **"Edge Certificates"** :
   - Activer **"Always Use HTTPS"**
   - Activer **"HTTP Strict Transport Security (HSTS)"**
   - Activer **"Minimum TLS Version"** : 1.2

### **Étape 2.3 : Configuration Caching**
1. Aller dans **Caching** → **Configuration**
2. Activer **"Browser Cache TTL"** : 1 mois
3. Activer **"Caching Level"** : Standard
4. Configurer **"Page Rules"** :
   ```
   tech4elles.com/api/*
   - Cache Level: Bypass
   - Edge Cache TTL: 2 hours
   ```

### **Étape 2.4 : Configuration Security**
1. Aller dans **Security** → **WAF**
2. Activer **"Web Application Firewall"**
3. Configurer **"Rate Limiting"** :
   - 1000 requests per minute per IP
4. Activer **"Bot Fight Mode"**

---

## **3. 🔑 CRÉATION DES TOKENS API**

### **Étape 3.1 : Créer un Token API Global**
1. Aller dans **My Profile** → **API Tokens**
2. Cliquer **"Create Token"**
3. Choisir **"Custom token"**
4. Configuration :
   ```
   Token name: Tech4Elles-Global

   Permissions:
   - Zone:Zone:Read
   - Zone:Zone Settings:Edit
   - Account:Cloudflare Pages:Edit
   - Account:Account Settings:Read

   Zone Resources:
   - Include: Specific zone: tech4elles.com

   Account Resources:
   - Include: All accounts
   ```

### **Étape 3.2 : Récupérer l'Account ID**
1. Aller dans **My Profile** → **API Tokens**
2. Cliquer **"View"** sur "Global API Key"
3. Noter l'**Account ID** affiché
4. **Exemple** : `1234567890abcdef1234567890abcdef`

### **Étape 3.3 : Créer un Token Spécifique Pages**
1. Cliquer **"Create Token"**
2. Choisir **"Cloudflare Pages:Edit"**
3. Configuration :
   ```
   Token name: Tech4Elles-Pages

   Permissions:
   - Account:Cloudflare Pages:Edit
   - Zone:Zone:Read

   Account Resources:
   - Include: All accounts

   Zone Resources:
   - Include: Specific zone: tech4elles.com
   ```

### **Étape 3.4 : Sauvegarder les Tokens**
⚠️ **IMPORTANT** : Sauvegarder immédiatement les tokens, ils ne sont affichés qu'une fois !

---

## **4. 📦 CONFIGURATION CLOUDFLARE PAGES**

### **Étape 4.1 : Créer le Projet User**
1. Aller dans **Pages** → **Create a project**
2. Choisir **"Connect to Git"**
3. Sélectionner votre repository **Tech4Elles**
4. Configuration :
   ```
   Project name: tech4elles
   Production branch: main
   Build command: cd apps/user && npm install && npm run build
   Build output directory: apps/user/build
   Root directory: apps/user
   Environment variables:
   - NODE_VERSION: 18
   - PUBLIC_API_URL: https://api.tech4elles.com
   ```

### **Étape 4.2 : Créer le Projet Admin**
1. Cliquer **"Create a project"**
2. Choisir **"Connect to Git"**
3. Sélectionner le même repository **Tech4Elles**
4. Configuration :
   ```
   Project name: tech4elles-admin
   Production branch: main
   Build command: cd apps/admin && npm install && npm run build
   Build output directory: apps/admin/build
   Root directory: apps/admin
   Environment variables:
   - NODE_VERSION: 18
   - PUBLIC_API_URL: https://api.tech4elles.com
   ```

### **Étape 4.3 : Configuration des Domaines Personnalisés**
1. Dans le projet **tech4elles** :
   - Aller dans **Custom domains**
   - Ajouter **`tech4elles.com`**
   - Ajouter **`www.tech4elles.com`**
   - Configurer **SSL/TLS** : Full (strict)

2. Dans le projet **tech4elles-admin** :
   - Aller dans **Custom domains**
   - Ajouter **`admin.tech4elles.com`**
   - Configurer **SSL/TLS** : Full (strict)

### **Étape 4.4 : Configuration des Variables d'Environnement**
1. **Production** :
   ```
   NODE_ENV: production
   PUBLIC_API_URL: https://api.tech4elles.com
   FIREBASE_PROJECT_ID: tech4elles-xxxxx
   ```

2. **Preview** :
   ```
   NODE_ENV: development
   PUBLIC_API_URL: https://api-dev.tech4elles.com
   FIREBASE_PROJECT_ID: tech4elles-dev-xxxxx
   ```

---

## **5. 🔗 CONNEXION GITHUB**

### **Étape 5.1 : Autoriser Cloudflare**
1. Dans **Pages** → **Create a project**
2. Cliquer **"Connect to Git"**
3. Choisir **"GitHub"**
4. Autoriser l'accès à votre repository **Tech4Elles**
5. Sélectionner **"All repositories"** ou **"Selected repositories"**

### **Étape 5.2 : Configuration des Branches**
1. **Production** : `main`
2. **Preview** : `develop` (optionnel)
3. **Build settings** : Automatiques
4. **Deploy hooks** : Configurer si nécessaire

### **Étape 5.3 : Configuration des Webhooks**
1. Aller dans **Settings** → **Webhooks**
2. Créer un webhook pour les déploiements automatiques
3. URL : `https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_id}/deployments`

---

## **6. ⚙️ CONFIGURATION DES WORKFLOWS**

### **Étape 6.1 : Secrets GitHub**
1. Aller dans votre repository **Tech4Elles**
2. **Settings** → **Secrets and variables** → **Actions**
3. Ajouter les secrets :
   ```
   CF_API_TOKEN: [votre_token_api_global]
   CF_ACCOUNT_ID: [votre_account_id]
   CLOUDFLARE_API_TOKEN: [votre_token_pages]
   CLOUDFLARE_ACCOUNT_ID: [votre_account_id]
   ```

### **Étape 6.2 : Configuration du Workflow**
Le workflow est déjà configuré dans `.github/workflows/build-and-deploy.yml` :

```yaml
name: Build and Deploy

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        default: 'staging'
        type: choice
        options:
        - staging
        - production

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
        cache: 'npm'

    - name: Install dependencies
      run: |
        cd apps/user
        npm ci
        cd ../admin
        npm ci

    - name: Build User App
      run: |
        cd apps/user
        npm run build

    - name: Build Admin App
      run: |
        cd apps/admin
        npm run build

    - name: Deploy User to Cloudflare Pages
      if: github.ref == 'refs/heads/main' || (github.event_name == 'workflow_dispatch' && inputs.environment == 'production')
      env:
        CLOUDFLARE_API_TOKEN: ${{ secrets.CF_API_TOKEN }}
        CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CF_ACCOUNT_ID }}
      run: |
        cd apps/user
        npx wrangler@latest pages publish build --project-name=tech4elles

    - name: Deploy Admin to Cloudflare Pages
      if: github.ref == 'refs/heads/main' || (github.event_name == 'workflow_dispatch' && inputs.environment == 'production')
      env:
        CLOUDFLARE_API_TOKEN: ${{ secrets.CF_API_TOKEN }}
        CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CF_ACCOUNT_ID }}
      run: |
        cd apps/admin
        npx wrangler@latest pages publish build --project-name=tech4elles-admin
```

---

## **7. 🔥 CONFIGURATION FIREBASE**

### **Étape 7.1 : Projet Firebase**
1. Aller sur [console.firebase.google.com](https://console.firebase.google.com)
2. Créer un nouveau projet **Tech4Elles**
3. Activer **Authentication** et **Firestore**

### **Étape 7.2 : Configuration des Services**
1. **Authentication** :
   - Activer **Email/Password**
   - Configurer les domaines autorisés :
     - `tech4elles.com`
     - `admin.tech4elles.com`
     - `localhost:5180` (développement)

2. **Firestore** :
   - Créer une base de données
   - Configurer les règles de sécurité :
   ```javascript
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /{document=**} {
         allow read, write: if request.auth != null;
       }
     }
   }
   ```

### **Étape 7.3 : Récupérer les Clés**
1. **Project Settings** → **Service accounts**
2. Générer une nouvelle clé privée
3. Noter :
   - `FIREBASE_PROJECT_ID`
   - `FIREBASE_CLIENT_EMAIL`
   - `FIREBASE_PRIVATE_KEY`

### **Étape 7.4 : Configuration des Notifications**
1. Aller dans **Cloud Messaging**
2. Configurer les **Server Key**
3. Tester l'envoi de notifications

---

## **8. 🧪 TESTS ET VALIDATION**

### **Étape 8.1 : Test Local**
```bash
# Démarrer l'API
cd apps/api
npm run dev

# Démarrer le frontend
cd apps/user
npm run dev
```

### **Étape 8.2 : Test de Déploiement**
1. Faire un commit sur la branche `main`
2. Vérifier que le workflow GitHub Actions se lance
3. Vérifier les déploiements dans Cloudflare Pages

### **Étape 8.3 : Test des Domaines**
1. **`tech4elles.com`** → Application User
2. **`admin.tech4elles.com`** → Application Admin
3. **`api.tech4elles.com`** → API (si configuré)

### **Étape 8.4 : Test des Performances**
1. Aller sur [PageSpeed Insights](https://pagespeed.web.dev/)
2. Tester `tech4elles.com`
3. Vérifier les scores de performance

---

## **9. 📊 MONITORING ET MAINTENANCE**

### **Étape 9.1 : Analytics Cloudflare**
1. Aller dans **Analytics** → **Web Analytics**
2. Activer le tracking pour vos domaines
3. Configurer les alertes :
   - Uptime monitoring
   - Performance alerts
   - Security alerts

### **Étape 9.2 : Monitoring des Performances**
1. **Speed** → **Insights** pour analyser les performances
2. **Caching** → **Purge Cache** si nécessaire
3. **Security** → **WAF** pour la sécurité

### **Étape 9.3 : Maintenance Régulière**
1. **Mise à jour des tokens** (tous les 6 mois)
2. **Vérification des certificats SSL**
3. **Monitoring des erreurs** dans les logs
4. **Sauvegarde des configurations**

---

## **10. 🔧 TROUBLESHOOTING**

### **Problème 1 : Déploiement échoue**
```bash
# Vérifier les logs
wrangler pages deployment list --project-name=tech4elles

# Vérifier les variables d'environnement
wrangler pages env list --project-name=tech4elles
```

### **Problème 2 : SSL ne fonctionne pas**
1. Vérifier la configuration DNS
2. Attendre la propagation (jusqu'à 24h)
3. Vérifier les certificats dans SSL/TLS

### **Problème 3 : Performance lente**
1. Vérifier la configuration de cache
2. Optimiser les images
3. Activer la compression

### **Problème 4 : Erreurs 404**
1. Vérifier la configuration des routes
2. Vérifier les redirections
3. Vérifier les Page Rules

---

## **🔧 CONFIGURATION FINALE RECOMMANDÉE**

### **📁 Structure des Domaines :**
```
tech4elles.com          → Frontend User (SvelteKit)
www.tech4elles.com      → Redirection vers tech4elles.com
admin.tech4elles.com    → Frontend Admin (SvelteKit)
api.tech4elles.com      → API AdonisJS (optionnel)
```

### **🔑 Variables d'Environnement :**
```bash
# Cloudflare
CF_API_TOKEN=your_global_api_token
CF_ACCOUNT_ID=your_account_id

# Firebase
FIREBASE_PROJECT_ID=tech4elles-xxxxx
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@tech4elles-xxxxx.iam.gserviceaccount.com
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
```

### **🚀 Workflow de Déploiement :**
1. **Commit** sur `main`
2. **GitHub Actions** se lance automatiquement
3. **Build** des applications frontend
4. **Déploiement** sur Cloudflare Pages
5. **Propagation** sur le CDN global

---

## **✅ CHECKLIST FINALE**

- [ ] Compte Cloudflare créé
- [ ] Domaine `tech4elles.com` ajouté
- [ ] DNS configuré
- [ ] SSL activé
- [ ] Tokens API créés
- [ ] Projets Pages créés
- [ ] GitHub connecté
- [ ] Secrets configurés
- [ ] Workflows testés
- [ ] Firebase configuré
- [ ] Domaines personnalisés ajoutés
- [ ] Tests de déploiement réussis
- [ ] Monitoring configuré
- [ ] Documentation mise à jour

---

## **📞 SUPPORT ET RESSOURCES**

### **Documentation Officielle :**
- [Cloudflare Pages](https://developers.cloudflare.com/pages/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)
- [Cloudflare API](https://developers.cloudflare.com/api/)

### **Communauté :**
- [Cloudflare Community](https://community.cloudflare.com/)
- [GitHub Discussions](https://github.com/cloudflare/workers/discussions)

### **Support :**
- **Free Plan** : Community support
- **Pro Plan** : Email support
- **Business Plan** : Phone support

---

**🎯 Votre infrastructure Cloudflare est maintenant prête pour Tech4Elles !**

*Dernière mise à jour : 18 septembre 2025*
