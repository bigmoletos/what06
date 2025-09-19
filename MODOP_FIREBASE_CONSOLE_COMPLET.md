# 🔥 MODOP Firebase Console - Configuration Complète Tech4Elles

## 📋 Table des Matières
1. [Accès à Firebase Console](#accès-à-firebase-console)
2. [Configuration du Projet](#configuration-du-projet)
3. [Configuration de l'Authentification](#configuration-de-lauthentification)
4. [Configuration de Cloud Messaging](#configuration-de-cloud-messaging)
5. [Configuration des Applications Web](#configuration-des-applications-web)
6. [Configuration des Notifications Push](#configuration-des-notifications-push)
7. [Configuration des Service Workers](#configuration-des-service-workers)
8. [Configuration des Clés API](#configuration-des-clés-api)
9. [Configuration des Domaines Autorisés](#configuration-des-domaines-autorisés)
10. [Configuration des Règles de Sécurité](#configuration-des-règles-de-sécurité)
11. [Configuration des Webhooks](#configuration-des-webhooks)
12. [Tests et Validation](#tests-et-validation)
13. [Monitoring et Analytics](#monitoring-et-analytics)
14. [Dépannage](#dépannage)

---

## 🚀 Accès à Firebase Console

### **1. Connexion à Firebase**
1. **Ouvrir le navigateur** : Aller sur [https://console.firebase.google.com/](https://console.firebase.google.com/)
2. **Se connecter** : Utiliser le compte Google associé au projet
3. **Sélectionner le projet** : `tech-4-elles`

### **2. Vérification du Projet**
- **Nom du projet** : `tech-4-elles`
- **ID du projet** : `tech-4-elles`
- **Région** : `us-central1` (par défaut)

---

## ⚙️ Configuration du Projet

### **1. Paramètres Généraux**
1. **Aller dans** : `⚙️ Paramètres du projet` (en haut à gauche)
2. **Onglet** : `Général`
3. **Vérifier** :
   - **Nom du projet** : `tech-4-elles`
   - **ID du projet** : `tech-4-elles`
   - **Région par défaut** : `us-central1`

### **2. Configuration des Services**
1. **Aller dans** : `⚙️ Paramètres du projet`
2. **Onglet** : `Services`
3. **Activer** :
   - ✅ **Cloud Messaging** (FCM)
   - ✅ **Authentication**
   - ✅ **Firestore Database**
   - ✅ **Storage**
   - ✅ **Hosting** (optionnel)

---

## 🔐 Configuration de l'Authentification

### **1. Activer l'Authentification**
1. **Aller dans** : `Authentication` (menu gauche)
2. **Onglet** : `Sign-in method`
3. **Activer** :
   - ✅ **Email/Password** (pour les comptes admin/mentor/mentee)
   - ✅ **Anonymous** (optionnel)

### **2. Configuration des Domaines Autorisés**
1. **Aller dans** : `Authentication` → `Settings`
2. **Section** : `Authorized domains`
3. **Ajouter** :
   - `localhost` (développement)
   - `tech4elles.com` (production)
   - `tech4elles.pages.dev` (Cloudflare Pages)

---

## 📱 Configuration de Cloud Messaging

### **1. Accès à Cloud Messaging**
1. **Aller dans** : `Cloud Messaging` (menu gauche)
2. **Vérifier** : Le service est activé

### **2. Configuration des Applications**
1. **Aller dans** : `Cloud Messaging` → `Settings`
2. **Onglet** : `Cloud Messaging API`
3. **Vérifier** : L'API est activée

---

## 🌐 Configuration des Applications Web

### **1. Ajouter une Application Web Admin**
1. **Aller dans** : `⚙️ Paramètres du projet` → `Général`
2. **Section** : `Vos applications`
3. **Cliquer** : `</>` (Ajouter une application web)
4. **Nom** : `Tech4Elles Admin`
5. **Cocher** : `Configurer Firebase Hosting` (optionnel)
6. **Cliquer** : `Enregistrer l'application`

### **2. Ajouter une Application Web User**
1. **Cliquer** : `</>` (Ajouter une autre application web)
2. **Nom** : `Tech4Elles User`
3. **Cocher** : `Configurer Firebase Hosting` (optionnel)
4. **Cliquer** : `Enregistrer l'application`

### **3. Configuration des Applications**
Pour chaque application (Admin et User) :

#### **A. Configuration Générale**
1. **Aller dans** : `⚙️ Paramètres du projet` → `Général`
2. **Section** : `Vos applications`
3. **Cliquer** : Sur l'icône `⚙️` de l'application
4. **Onglet** : `Général`

#### **B. Configuration des Clés**
1. **Onglet** : `Configuration`
2. **Copier** :
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSyB9-8FFCs0VC2C0sbgtXh-09EKJTJpSUrE",
     authDomain: "tech-4-elles.firebaseapp.com",
     projectId: "tech-4-elles",
     storageBucket: "tech-4-elles.firebasestorage.app",
     messagingSenderId: "803392920579",
     appId: "1:803392920579:web:6c234d808f71c6ff214236"
   };
   ```

---

## 🔔 Configuration des Notifications Push

### **1. Configuration des Clés VAPID**
1. **Aller dans** : `Cloud Messaging` → `Settings`
2. **Onglet** : `Cloud Messaging API`
3. **Section** : `Web Push certificates`
4. **Cliquer** : `Generate key pair` (si pas déjà fait)
5. **Copier** : La clé publique VAPID
   ```
   BCZQgcI-TEz6_xkYH_mQ5UvQXRnVLL4qk3JtwPeBWPIO5twOK-NBWxKEuMC0KJiXz_nImQh8opLw1VFOQLPSZ0Q
   ```

### **2. Configuration des Tokens de Notification**
1. **Aller dans** : `Cloud Messaging` → `Settings`
2. **Onglet** : `Cloud Messaging API`
3. **Section** : `Server key`
4. **Copier** : La clé serveur (pour l'API backend)

---

## 🔧 Configuration des Service Workers

### **1. Configuration des Service Workers**
1. **Aller dans** : `Cloud Messaging` → `Settings`
2. **Onglet** : `Cloud Messaging API`
3. **Section** : `Web Push certificates`
4. **Vérifier** : Le service worker est configuré

### **2. Configuration des Manifestes**
1. **Aller dans** : `⚙️ Paramètres du projet` → `Général`
2. **Section** : `Vos applications`
3. **Cliquer** : Sur l'icône `⚙️` de l'application
4. **Onglet** : `Configuration`
5. **Section** : `Web Push certificates`
6. **Vérifier** : Les clés VAPID sont configurées

---

## 🔑 Configuration des Clés API

### **1. Clés API Firebase**
1. **Aller dans** : `⚙️ Paramètres du projet` → `Général`
2. **Onglet** : `Clés API`
3. **Vérifier** : Les clés API sont générées

### **2. Configuration des Restrictions**
1. **Cliquer** : Sur une clé API
2. **Onglet** : `Restrictions`
3. **Type** : `HTTP referrers (web sites)`
4. **Ajouter** :
   - `http://localhost:*` (développement)
   - `https://tech4elles.com/*` (production)
   - `https://tech4elles.pages.dev/*` (Cloudflare Pages)

---

## 🌍 Configuration des Domaines Autorisés

### **1. Domaines de Développement**
1. **Aller dans** : `Authentication` → `Settings`
2. **Onglet** : `Authorized domains`
3. **Ajouter** :
   - `localhost`
   - `127.0.0.1`
   - `localhost:5181` (User)
   - `localhost:5182` (Admin)

### **2. Domaines de Production**
1. **Ajouter** :
   - `tech4elles.com`
   - `www.tech4elles.com`
   - `tech4elles.pages.dev`
   - `*.tech4elles.pages.dev`

---

## 🛡️ Configuration des Règles de Sécurité

### **1. Règles Firestore**
1. **Aller dans** : `Firestore Database` → `Règles`
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

### **2. Règles Storage**
1. **Aller dans** : `Storage` → `Règles`
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

### **1. Configuration des Webhooks**
1. **Aller dans** : `Cloud Messaging` → `Settings`
2. **Onglet** : `Cloud Messaging API`
3. **Section** : `Webhooks`
4. **Ajouter** :
   - **URL** : `https://tech4elles.com/api/webhooks/firebase`
   - **Événements** : `message_sent`, `message_delivered`

---

## 🧪 Tests et Validation

### **1. Test des Notifications**
1. **Aller dans** : `Cloud Messaging` → `Composer`
2. **Créer** : Une notification de test
3. **Titre** : `Test Tech4Elles`
4. **Texte** : `Notification de test`
5. **Cibler** : `All users` ou `Specific users`
6. **Envoyer** : La notification

### **2. Test des Service Workers**
1. **Ouvrir** : `http://localhost:5181/` (User)
2. **Ouvrir** : `http://localhost:5182/` (Admin)
3. **Console** : Vérifier les logs
4. **Vérifier** : `Service Worker Firebase enregistré`

### **3. Test des Tokens**
1. **Console** : `navigator.serviceWorker.ready`
2. **Vérifier** : Le service worker est actif
3. **Vérifier** : Les notifications sont autorisées

---

## 📊 Monitoring et Analytics

### **1. Analytics Firebase**
1. **Aller dans** : `Analytics` → `Dashboard`
2. **Vérifier** : Les événements sont trackés
3. **Onglet** : `Events`
4. **Vérifier** : `notification_received`, `notification_clicked`

### **2. Cloud Messaging Analytics**
1. **Aller dans** : `Cloud Messaging` → `Analytics`
2. **Vérifier** : Les métriques de notification
3. **Onglet** : `Delivery`
4. **Vérifier** : Le taux de livraison

---

## 🔧 Dépannage

### **1. Erreurs Courantes**

#### **A. Service Worker non enregistré**
```
Erreur : Service Worker Firebase enregistré: undefined
```
**Solution** :
1. Vérifier que le fichier `firebase-messaging-sw.js` existe
2. Vérifier les permissions du navigateur
3. Vérifier la configuration VAPID

#### **B. Notifications non reçues**
```
Erreur : Notifications non reçues
```
**Solution** :
1. Vérifier les permissions de notification
2. Vérifier la configuration des clés VAPID
3. Vérifier les domaines autorisés

#### **C. Erreur 404 firebase-messaging-sw.js**
```
Erreur : [404] GET /firebase-messaging-sw.js
```
**Solution** :
1. Vérifier que le fichier existe dans `public/`
2. Vérifier la configuration du service worker
3. Redémarrer l'application

### **2. Logs de Débogage**
1. **Console** : `firebase.messaging()`
2. **Vérifier** : Les tokens sont générés
3. **Vérifier** : Les permissions sont accordées

### **3. Validation de la Configuration**
1. **Vérifier** : Toutes les clés API sont correctes
2. **Vérifier** : Les domaines sont autorisés
3. **Vérifier** : Les service workers sont enregistrés

---

## 📝 Checklist de Configuration

### **✅ Configuration de Base**
- [ ] Projet Firebase créé (`tech-4-elles`)
- [ ] Services activés (Authentication, Cloud Messaging, Firestore)
- [ ] Applications web ajoutées (Admin et User)

### **✅ Configuration des Notifications**
- [ ] Clés VAPID générées
- [ ] Service workers configurés
- [ ] Tokens de notification testés

### **✅ Configuration de Sécurité**
- [ ] Domaines autorisés configurés
- [ ] Règles de sécurité définies
- [ ] Clés API restreintes

### **✅ Tests et Validation**
- [ ] Notifications de test envoyées
- [ ] Service workers fonctionnels
- [ ] Erreurs 404 résolues

---

## 🎯 Résumé de la Configuration

### **Informations du Projet**
- **Nom** : `tech-4-elles`
- **ID** : `tech-4-elles`
- **Région** : `us-central1`

### **Clés de Configuration**
```javascript
// Configuration Firebase
const firebaseConfig = {
  apiKey: "AIzaSyB9-8FFCs0VC2C0sbgtXh-09EKJTJpSUrE",
  authDomain: "tech-4-elles.firebaseapp.com",
  projectId: "tech-4-elles",
  storageBucket: "tech-4-elles.firebasestorage.app",
  messagingSenderId: "803392920579",
  appId: "1:803392920579:web:6c234d808f71c6ff214236",
  vapidKey: "BCZQgcI-TEz6_xkYH_mQ5UvQXRnVLL4qk3JtwPeBWPIO5twOK-NBWxKEuMC0KJiXz_nImQh8opLw1VFOQLPSZ0Q"
};
```

### **URLs de Test**
- **User** : `http://localhost:5181/`
- **Admin** : `http://localhost:5182/`
- **Production** : `https://tech4elles.com/`

---

## 🚀 Prochaines Étapes

1. **Suivre ce guide** étape par étape
2. **Tester** chaque configuration
3. **Valider** que les notifications fonctionnent
4. **Déployer** en production
5. **Monitorer** les performances

---

*Ce guide couvre l'ensemble de la configuration Firebase Console pour Tech4Elles. Suivez chaque étape dans l'ordre pour une configuration complète et fonctionnelle.*
