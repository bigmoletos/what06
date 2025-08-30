# 🔥 MODOP FIREBASE - Tech4Elles

lien du projet firebase sur mon compte google

https://console.firebase.google.com/project/tech4elles-1b393/settings/serviceaccounts/adminsdk


https://console.firebase.google.com/project/tech4elles-1b393/settings/cloudmessaging

## 📋 **Vue d'Ensemble**

### **Qu'est-ce que Firebase ?**
Firebase est une plateforme de développement de Google qui fournit des services backend pour les applications web et mobiles.

### **Services Firebase utilisés dans Tech4Elles :**
- **Authentication** : Gestion des utilisateurs (connexion, inscription)
- **Firestore** : Base de données NoSQL en temps réel
- **Cloud Messaging** : Notifications push
- **Hosting** : Hébergement de l'application

---

## 🎯 **Objectifs du MODOP**

### **1. Créer un projet Firebase**
- Configuration de l'environnement de développement
- Sécurisation de l'application

### **2. Générer les clés d'API**
- Clé privée pour l'authentification serveur
- Configuration des variables d'environnement

### **3. Tester la configuration**
- Vérification de la connexion
- Test de l'authentification

---

## 🚀 **Étapes du MODOP**

### **Phase 1 : Création du Projet Firebase**

#### **1.1 Accès à Firebase Console**
- Aller sur [https://console.firebase.google.com/](https://console.firebase.google.com/)
- Se connecter avec un compte Google
- Cliquer sur "Créer un projet"

#### **1.2 Configuration du Projet**
- **Nom du projet** : `tech4elles-dev` (ou votre nom)
- **ID du projet** : Généré automatiquement
- **Google Analytics** : Désactivé pour le développement
- Cliquer sur "Créer le projet"

#### **1.3 Activation des Services**
- **Authentication** : Activer
- **Firestore Database** : Activer
- **Cloud Messaging** : Activer (optionnel)

### **Phase 2 : Configuration de l'Authentification**

#### **2.1 Méthodes de Connexion**
- **Email/Mot de passe** : Activer
- **Google** : Activer (optionnel)
- **Anonyme** : Désactiver

#### **2.2 Règles de Validation**
- **Email** : Validation standard
- **Mot de passe** : Minimum 6 caractères

### **Phase 3 : Génération des Clés d'API**

#### **3.1 Compte de Service**
- **Paramètres du projet** → **Comptes de service**
- **SDK Admin Firebase** → **Générer une nouvelle clé privée**
- Télécharger le fichier JSON

#### **3.2 Variables d'Environnement**
Le fichier JSON contient :
```json
{
  "type": "service_account",
  "project_id": "votre-project-id",
  "private_key_id": "abc123...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xxxxx@votre-project.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

---

## 🔧 **Configuration dans Tech4Elles**

### **Variables d'Environnement Requises**

Dans `apps/api/.env` :
```bash
# ========================================
# CONFIGURATION FIREBASE
# ========================================
FIREBASE_PROJECT_ID=votre-project-id
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@votre-project.iam.gserviceaccount.com
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----
VOTRE_CLE_PRIVEE_ICI
-----END PRIVATE KEY-----"

# ========================================
# CONFIGURATION FIREBASE OPTIONNELLE
# ========================================
FIREBASE_DATABASE_URL=https://votre-project.firebaseio.com
FIREBASE_STORAGE_BUCKET=votre-project.appspot.com
```

### **Structure des Données Firestore**

#### **Collection `users`**
```json
{
  "id": "user123",
  "email": "mentee@example.com",
  "firstName": "Marie",
  "lastName": "Dupont",
  "type": "mentee",
  "createdAt": "2025-08-28T15:00:00Z",
  "profile": {
    "interests": ["web", "mobile"],
    "experience": "beginner",
    "goals": ["learn-react", "build-portfolio"]
  }
}
```

#### **Collection `mentors`**
```json
{
  "id": "mentor456",
  "email": "marraine@example.com",
  "firstName": "Sophie",
  "lastName": "Martin",
  "type": "mentor",
  "expertise": ["react", "nodejs", "python"],
  "maxMentees": 3,
  "currentMentees": 1,
  "availability": "weekends"
}
```

---

## 🧪 **Tests et Validation**

### **Test 1 : Connexion à Firebase**
```bash
# Vérifier que l'API démarre sans erreur
npx pnpm dev

# Vérifier les logs Firebase
# Devrait voir : "Firebase initialized successfully"
```

### **Test 2 : Création d'Utilisateur**
1. Aller sur http://localhost:5180/register
2. Remplir le formulaire d'inscription
3. Vérifier que l'utilisateur est créé dans Firestore

### **Test 3 : Authentification**
1. Se connecter avec l'utilisateur créé
2. Vérifier la session
3. Accéder au dashboard

---

## ⚠️ **Sécurité et Bonnes Pratiques**

### **1. Protection des Clés**
- **Ne jamais commiter** le fichier `.env` dans Git
- **Utiliser des variables d'environnement** en production
- **Rotation régulière** des clés privées

### **2. Règles Firestore**
```javascript
// Exemple de règles de sécurité
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Utilisateurs peuvent lire/modifier leur propre profil
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    // Mentors peuvent lire les profils des mentees
    match /mentors/{mentorId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null && request.auth.uid == mentorId;
    }
  }
}
```

### **3. Limites et Quotas**
- **Gratuit** : 50,000 lectures/jour, 20,000 écritures/jour
- **Payant** : $0.18/100,000 lectures, $0.18/100,000 écritures

---

## 🚨 **Dépannage**

### **Erreur : "Invalid private key"**
- Vérifier le format de la clé privée
- S'assurer que les retours à la ligne sont préservés
- Utiliser des guillemets doubles dans `.env`

### **Erreur : "Project not found"**
- Vérifier l'ID du projet Firebase
- S'assurer que le projet est bien créé
- Vérifier les permissions du compte de service

### **Erreur : "Permission denied"**
- Vérifier les règles Firestore
- S'assurer que l'authentification est activée
- Vérifier les permissions du compte de service

---

## 📊 **Monitoring et Maintenance**

### **1. Logs Firebase**
- Surveiller les tentatives de connexion
- Détecter les activités suspectes
- Optimiser les performances

### **2. Métriques Utilisateurs**
- Nombre d'inscriptions par jour
- Taux de conversion
- Temps de session moyen

### **3. Sauvegarde**
- Exporter régulièrement les données
- Sauvegarder les règles de sécurité
- Documenter les configurations

---

## 🎯 **Résultats Attendus**

### **Après ce MODOP :**
- ✅ Projet Firebase créé et configuré
- ✅ Variables d'environnement générées
- ✅ Authentification fonctionnelle
- ✅ Base de données opérationnelle
- ✅ Application Tech4Elles entièrement fonctionnelle

---

## 📚 **Ressources Complémentaires**

### **Documentation Officielle**
- [Firebase Documentation](https://firebase.google.com/docs)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Firestore Security Rules](https://firebase.google.com/docs/firestore/security/get-started)

### **Outils Utiles**
- [Firebase CLI](https://firebase.google.com/docs/cli)
- [Firebase Emulator](https://firebase.google.com/docs/emulator-suite)
- [Firebase Extensions](https://firebase.google.com/docs/extensions)

---

**🚀 Prêt à configurer Firebase pour Tech4Elles !**
