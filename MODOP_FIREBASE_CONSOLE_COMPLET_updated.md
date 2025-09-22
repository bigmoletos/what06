# 🔥 MODOP Firebase Console - Configuration Complète Tech4Elles

## 📋 Variables de Configuration

```javascript
// Configuration du Projet
const PROJECT_NAME = "tech4elles";
const PROJECT_ID = "tech4elles-1b393";
const DEFAULT_REGION = "us-central1";
const FIREBASE_CONSOLE_URL = "https://console.firebase.google.com/";
const API_KEY = "votre_api_key";
const AUTH_DOMAIN = "votre_auth_domain";
const DATABASE_URL = "votre_database_url";
const STORAGE_BUCKET = "votre_storage_bucket";
const MESSAGING_SENDER_ID = "votre_messaging_sender_id";
const APP_ID = "votre_app_id";
const MEASUREMENT_ID = "votre_measurement_id";
const CLOUDFLARE_DOMAIN = "votre_domaine_cloudflare";
const VAPID_KEY = "votre_vapid_key";
```

## 📋 Table des Matières

1. [🚀 Accès à Firebase Console](#-accès-à-firebase-console)
2. [⚙️ Configuration du Projet](#️-configuration-du-projet)
3. [🔐 Configuration de l'Authentification](#-configuration-de-lauthentification)
4. [📱 Configuration de Cloud Messaging](#-configuration-de-cloud-messaging)
5. [🌐 Configuration des Applications Web](#-configuration-des-applications-web)
6. [🤖 Configuration des Applications Android](#-configuration-des-applications-android)
7. [🍎 Configuration des Applications iOS](#-configuration-des-applications-ios)
8. [🔔 Configuration des Notifications Push](#-configuration-des-notifications-push)
9. [🔧 Configuration des Service Workers](#-configuration-des-service-workers)
10. [🔑 Configuration des Clés API](#-configuration-des-clés-api)
11. [🌍 Configuration des Domaines Autorisés](#-configuration-des-domaines-autorisés)
12. [🛡️ Configuration des Règles de Sécurité](#️-configuration-des-règles-de-sécurité)
13. [🔗 Configuration des Webhooks](#-configuration-des-webhooks)
14. [☁️ Intégration avec Cloudflare](#️-intégration-avec-cloudflare)
15. [🧪 Tests et Validation](#-tests-et-validation)
16. [📊 Monitoring et Analytics](#-monitoring-et-analytics)
17. [🔧 Dépannage](#-dépannage)
18. [📝 Checklist de Configuration](#-checklist-de-configuration)
19. [🎯 Résumé de la Configuration](#-résumé-de-la-configuration)
20. [🚀 Prochaines Étapes](#-prochaines-étapes)

---

## 🚀 Accès à Firebase Console

### 1. Connexion à Firebase

1. **Ouvrir le navigateur** : Aller sur https://console.firebase.google.com/
2. **Se connecter** : Utiliser le compte Google associé au projet
3. **Sélectionner le projet** : `{PROJECT_NAME}`

### 2. Vérification du Projet

- **Nom du projet** : `{PROJECT_NAME}`
- **ID du projet** : `{PROJECT_ID}`
- **Région** : `{DEFAULT_REGION}` (par défaut)

---

## ⚙️ Configuration du Projet

### 1. Paramètres Généraux

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Onglet** : Général
3. **Vérifier** :
   - Nom du projet : `{PROJECT_NAME}`
   - ID du projet : `{PROJECT_ID}`
   - Région par défaut : `{DEFAULT_REGION}`

### 2. Activation des Services Firebase

Les services Firebase s'activent automatiquement lors de leur première utilisation. Voici comment les activer :

#### A. Authentication
1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/authentication
2. **Cliquer** : "Get started" ou "Commencer"
3. **Sélectionner** : Méthodes de connexion (Email/Password, etc.)

#### B. Firestore Database
1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/firestore
2. **Cliquer** : "Create database" ou "Créer une base de données"
3. **Choisir** : Mode de production ou test
4. **Sélectionner** : Région (us-central1 par défaut)

#### C. Cloud Storage (optionnel)
Note: Service payant au-delà du quota gratuit (plan Spark suffisant pour tests). Si vous n'avez pas de fichiers à stocker (images, PDFs, pièces jointes), ignorez cette section.

- Cas d'usage: stockage d'images utilisateurs, documents, pièces jointes, exports.
- Alternatives: Cloudflare Pages/R2, Cloudinary, hébergement statique de fichiers publics.

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/storage
2. **Cliquer** : "Get started" ou "Commencer"
3. **Accepter** : Les règles de sécurité par défaut

#### D. Cloud Messaging (FCM)
1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification
2. **Le service** : S'active automatiquement

#### E. Hosting (optionnel)
1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/hosting
2. **Cliquer** : "Get started" ou "Commencer"
3. **Suivre** : Les instructions d'installation

---

## 🔐 Configuration de l'Authentification

### 1. Activer l'Authentification

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/authentication
2. **Onglet** : Sign-in method
3. **Activer** :
   - ✅ Email/Password (pour les comptes admin/mentor/mentee)
   - ✅ Anonymous (optionnel)

### 2. Configuration des Domaines Autorisés

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/authentication/settings
2. **Section** : Authorized domains
3. **Ajouter** :
   - `localhost` (développement)
   - `{CLOUDFLARE_DOMAIN}` (production)
   - `{CLOUDFLARE_DOMAIN}.pages.dev` (Cloudflare Pages)

---

## 📱 Configuration de Cloud Messaging

### 1. Accès à Cloud Messaging

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification
2. **Vérifier** : Le service est activé

### 2. Configuration des Applications

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/settings
2. **Onglet** : Cloud Messaging API
3. **Vérifier** : L'API est activée

---

## 🌐 Configuration des Applications Web

### 1. Ajouter une Application Web Admin

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : `</>` (Ajouter une application web)
4. **Nom** : Tech4Elles Admin
5. **Cocher** : Configurer Firebase Hosting (optionnel)
6. **Cliquer** : Enregistrer l'application

### 2. Ajouter une Application Web User

1. **Cliquer** : `</>` (Ajouter une autre application web)
2. **Nom** : Tech4Elles User
3. **Cocher** : Configurer Firebase Hosting (optionnel)
4. **Cliquer** : Enregistrer l'application

### 3. Configuration des Applications

Pour chaque application (Admin et User) :

#### A. Configuration Générale

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : Sur la carte de l'application (Admin ou User)
4. **Ouvrir** : "Configurer le SDK" / "SDK setup and configuration"
5. **Onglet** : Général

#### B. Configuration des Clés

1. **Onglet** : Configuration
2. **Copier** :

```javascript
const firebaseConfig = {
  apiKey: "{API_KEY}",
  authDomain: "{AUTH_DOMAIN}",
  projectId: "{PROJECT_ID}",
  storageBucket: "{STORAGE_BUCKET}",
  messagingSenderId: "{MESSAGING_SENDER_ID}",
  appId: "{APP_ID}"
};
```

---

## 🤖 Configuration des Applications Android

### 1. Ajouter une Application Android

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : Android (Ajouter une application Android)
4. **Nom** : Tech4Elles Android
5. **Package Name** : com.tech4elles
6. **SHA-1** : votre_sha1
7. **Cliquer** : Enregistrer l'application

### 2. Configuration des Clés

1. **Télécharger** : Le fichier `google-services.json`
2. **Placer** : Dans le répertoire `app` de votre projet Android

---

## 🍎 Configuration des Applications iOS

### 1. Ajouter une Application iOS

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : iOS (Ajouter une application iOS)
4. **Nom** : Tech4Elles iOS
5. **Bundle ID** : com.tech4elles
6. **App Store ID** : votre_app_store_id (optionnel)
7. **Cliquer** : Enregistrer l'application

### 2. Configuration des Clés

1. **Télécharger** : Le fichier `GoogleService-Info.plist`
2. **Placer** : Dans le répertoire racine de votre projet iOS

---

## 🔔 Configuration des Notifications Push

### 1. Configuration des Clés VAPID

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/settings
2. **Onglet** : Cloud Messaging API
3. **Section** : Web Push certificates
4. **Cliquer** : Generate key pair (si pas déjà fait)
5. **Copier** : La clé publique VAPID

```javascript
{VAPID_KEY}
```

### 2. Configuration des Tokens de Notification

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/settings
2. **Onglet** : Cloud Messaging API
3. **Section** : Server key
4. **Copier** : La clé serveur (pour l'API backend)

---

## 🔧 Configuration des Service Workers

### 1. Configuration des Service Workers

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/settings
2. **Onglet** : Cloud Messaging API
3. **Section** : Web Push certificates
4. **Vérifier** : Le service worker est configuré

### 2. Configuration des Manifestes

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : Sur la carte de l'application
4. **Ouvrir** : "Configurer le SDK" / "SDK setup and configuration"
5. **Onglet** : Configuration
5. **Section** : Web Push certificates
6. **Vérifier** : Les clés VAPID sont configurées

---

## 🔑 Configuration des Clés API

### 1. Clés API Firebase

Les clés API Firebase sont automatiquement générées lors de la création d'une application web. Elles se trouvent dans la configuration de l'application :

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/settings/general
2. **Section** : Vos applications
3. **Cliquer** : Sur la carte de votre application web
4. **Ouvrir** : "Configurer le SDK" / "SDK setup and configuration"
5. **Onglet** : Configuration
5. **Copier** : Les clés de configuration Firebase

### 2. Configuration des Restrictions (Google Cloud Console)

⚠️ **Note** : Les restrictions d'API se configurent dans Google Cloud Console, pas dans Firebase Console.

1. **Aller dans** : https://console.cloud.google.com/apis/credentials?project=tech4elles-1b393
2. **Sélectionner** : La clé API Firebase
3. **Cliquer** : "Restrictions"
4. **Type** : HTTP referrers (web sites)
5. **Ajouter** :
   - `http://localhost:*` (développement)
   - `https://{CLOUDFLARE_DOMAIN}/*` (production)
   - `https://{CLOUDFLARE_DOMAIN}.pages.dev/*` (Cloudflare Pages)

---

## 🌍 Configuration des Domaines Autorisés

### 1. Domaines de Développement

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/authentication/settings
2. **Onglet** : Authorized domains
3. **Ajouter** :
   - `localhost`
   - `127.0.0.1`
   - `localhost:5181` (User)
   - `localhost:5182` (Admin)

### 2. Domaines de Production

**Ajouter** :
- `{CLOUDFLARE_DOMAIN}`
- `www.{CLOUDFLARE_DOMAIN}`
- `{CLOUDFLARE_DOMAIN}.pages.dev`
- `*.{CLOUDFLARE_DOMAIN}.pages.dev`

---

## 🛡️ Configuration des Règles de Sécurité

### 1. Règles Firestore

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/database/firestore/rules
2. **Configuration** :

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Règles pour les notifications
    match /notifications/{document} {
      allow read, write: if request.auth != null;
    }
    // Règles pour les tokens
    match /tokens/{document} {
      allow read, write: if request.auth != null;
    }
  }
}
```

### 2. Règles Storage (si activé)

Si vous n'utilisez pas Cloud Storage, ignorez cette section.

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/storage/rules
2. **Configuration** :

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

---

## 🔗 Configuration des Webhooks

### 1. Configuration des Webhooks

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/settings
2. **Onglet** : Cloud Messaging API
3. **Section** : Webhooks
4. **Ajouter** :
   - **URL** : `https://{CLOUDFLARE_DOMAIN}/api/webhooks/firebase`
   - **Événements** : message_sent, message_delivered

---

## ☁️ Intégration avec Cloudflare

### 1. Configuration DNS

1. **Aller dans** : Cloudflare Dashboard
2. **Section** : DNS
3. **Ajouter un enregistrement** :
   - **Type** : CNAME
   - **Name** : firebase
   - **Target** : `{PROJECT_ID}.firebaseapp.com`

### 2. Configuration SSL/TLS

1. **Aller dans** : Cloudflare Dashboard → SSL/TLS
2. **Onglet** : Overview
3. **Mode SSL** : Full (Strict)

---

## 🧪 Tests et Validation

### 1. Test des Notifications

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/compose
2. **Créer** : Une notification de test
   - **Titre** : Test Tech4Elles
   - **Texte** : Notification de test
   - **Cibler** : All users ou Specific users
3. **Envoyer** : La notification

### 2. Test des Service Workers

1. **Ouvrir** : http://localhost:5181/ (User)
2. **Ouvrir** : http://localhost:5182/ (Admin)
3. **Console** : Vérifier les logs
4. **Vérifier** : Service Worker Firebase enregistré

### 3. Test des Tokens

1. **Console** : `navigator.serviceWorker.ready`
2. **Vérifier** : Le service worker est actif
3. **Vérifier** : Les notifications sont autorisées

---

## 📊 Monitoring et Analytics

### 1. Analytics Firebase

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/analytics/dashboard
2. **Vérifier** : Les événements sont trackés
3. **Onglet** : Events
4. **Vérifier** : notification_received, notification_clicked

### 2. Cloud Messaging Analytics

1. **Aller dans** : https://console.firebase.google.com/project/tech4elles-1b393/notification/analytics
2. **Vérifier** : Les métriques de notification
3. **Onglet** : Delivery
4. **Vérifier** : Le taux de livraison

---

## 🔧 Dépannage

### 1. Erreurs Courantes

#### A. Service Worker non enregistré

**Erreur** :
```
Service Worker Firebase enregistré: undefined
```

**Solution** :
- Vérifier que le fichier `firebase-messaging-sw.js` existe
- Vérifier les permissions du navigateur
- Vérifier la configuration VAPID

#### B. Notifications non reçues

**Erreur** :
```
Notifications non reçues
```

**Solution** :
- Vérifier les permissions de notification
- Vérifier la configuration des clés VAPID
- Vérifier les domaines autorisés

#### C. Erreur 404 firebase-messaging-sw.js

**Erreur** :
```
[404] GET /firebase-messaging-sw.js
```

**Solution** :
- Vérifier que le fichier existe dans `public/`
- Vérifier la configuration du service worker
- Redémarrer l'application

### 2. Logs de Débogage

1. **Console** : `firebase.messaging()`
2. **Vérifier** : Les tokens sont générés
3. **Vérifier** : Les permissions sont accordées

### 3. Validation de la Configuration

- **Vérifier** : Toutes les clés API sont correctes
- **Vérifier** : Les domaines sont autorisés
- **Vérifier** : Les service workers sont enregistrés

---

## 📝 Checklist de Configuration

### ✅ Configuration de Base

- [ ] Projet Firebase créé (`{PROJECT_NAME}`)
- [ ] Services activés (Authentication, Cloud Messaging, Firestore)
- [ ] Applications web ajoutées (Admin et User)
- [ ] Applications Android et iOS ajoutées

### ✅ Configuration des Notifications

- [ ] Clés VAPID générées
- [ ] Service workers configurés
- [ ] Tokens de notification testés

### ✅ Configuration de Sécurité

- [ ] Domaines autorisés configurés
- [ ] Règles de sécurité définies
- [ ] Clés API restreintes

### ✅ Tests et Validation

- [ ] Notifications de test envoyées
- [ ] Service workers fonctionnels
- [ ] Erreurs 404 résolues

---

## 🎯 Résumé de la Configuration

### Informations du Projet

- **Nom** : `{PROJECT_NAME}`
- **ID** : `{PROJECT_ID}`
- **Région** : `{DEFAULT_REGION}`

### Clés de Configuration

```javascript
// Configuration Firebase
const firebaseConfig = {
  apiKey: "{API_KEY}",
  authDomain: "{AUTH_DOMAIN}",
  projectId: "{PROJECT_ID}",
  storageBucket: "{STORAGE_BUCKET}",
  messagingSenderId: "{MESSAGING_SENDER_ID}",
  appId: "{APP_ID}",
  vapidKey: "{VAPID_KEY}"
};
```

### URLs de Test

- **User** : http://localhost:5181/
- **Admin** : http://localhost:5182/
- **Production** : https://{CLOUDFLARE_DOMAIN}/

---

## 🚀 Prochaines Étapes

1. Suivre ce guide étape par étape
2. Tester chaque configuration
3. Valider que les notifications fonctionnent
4. Déployer en production
5. Monitorer les performances

---

**📖 Documentation mise à jour pour Tech4Elles - Configuration Firebase Console complète**