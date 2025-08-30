# 🚀 GUIDE FIREBASE RAPIDE - Tech4Elles

## ⚡ **Configuration Express (5 minutes)**

### **1. Créer le Projet Firebase**
- Aller sur [https://console.firebase.google.com/](https://console.firebase.google.com/)
- Cliquer "Créer un projet"
- Nom : `tech4elles-dev`
- Désactiver Google Analytics
- Cliquer "Créer le projet"

### **2. Activer les Services**
- **Authentication** → "Commencer" → Email/Mot de passe → "Activer"
- **Firestore Database** → "Créer une base de données" → Mode test → "Suivant"

### **3. Générer la Clé API**
- **Paramètres du projet** (⚙️) → **Comptes de service**
- **SDK Admin Firebase** → **Générer une nouvelle clé privée**
- Télécharger le fichier JSON

### **4. Exécuter le Script Automatique**
```bash
cd what06/outils
powershell -ExecutionPolicy Bypass -File firebase_setup.ps1
```

---

## 🔑 **Variables à Saisir**

### **Project ID**
- Trouvé dans les paramètres du projet
- Exemple : `tech4elles-dev-12345`

### **Client Email**
- Dans le fichier JSON téléchargé
- Clé : `client_email`
- Format : `firebase-adminsdk-xxxxx@project.iam.gserviceaccount.com`

### **Private Key**
- Dans le fichier JSON téléchargé
- Clé : `private_key`
- Copier TOUT le contenu (avec `-----BEGIN PRIVATE KEY-----`)

---

## 🧪 **Test Rapide**

### **1. Redémarrer l'App**
```bash
cd what06/Tech4Elles
npx pnpm dev
```

### **2. Vérifier l'API**
- Port 3333 ouvert ✅
- Pas d'erreur Firebase ✅

### **3. Tester l'Inscription**
- Aller sur http://localhost:5180/register
- Remplir le formulaire
- Vérifier dans Firebase Console

---

## 🚨 **Problèmes Courants**

### **"Invalid private key"**
- Vérifier que la clé est complète
- Inclure `-----BEGIN PRIVATE KEY-----` et `-----END PRIVATE KEY-----`

### **"Project not found"**
- Vérifier l'ID du projet
- S'assurer que le projet est créé

### **"Permission denied"**
- Vérifier que Authentication est activé
- Vérifier que Firestore est créé

---

## 🎯 **Résultat Attendu**

Après 5 minutes :
- ✅ Firebase configuré
- ✅ API fonctionnelle
- ✅ Inscription/Connexion opérationnelles
- ✅ Base de données Firestore active

---

**🚀 Prêt à configurer Firebase en 5 minutes !**
