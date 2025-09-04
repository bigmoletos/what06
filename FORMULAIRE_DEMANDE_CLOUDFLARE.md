# 📋 **FORMULAIRE DE DEMANDE CLOUDFLARE - TECH4ELLES**

## 🎯 **Objectif de cette Demande**

Ce formulaire vous permet de **récupérer toutes les informations manquantes** pour configurer le déploiement automatique de Tech4Elles sur Cloudflare Pages.

---

## 🔐 **INFORMATIONS REQUISES**

### **1. Compte Cloudflare**
- [ ] **Email de connexion** : `_________________`
- [ ] **Mot de passe** : `_________________`
- [ ] **Compte existant** : ☐ Oui ☐ Non (à créer)

### **2. Account ID Cloudflare**
- [ ] **Account ID** : `________________________________`
- [ ] **Nom du compte** : `_________________`
- [ ] **Type de compte** : ☐ Gratuit ☐ Pro ☐ Business ☐ Enterprise

### **3. API Token Cloudflare**
- [ ] **Token API** : `________________________________________________`
- [ ] **Nom du token** : `_________________`
- [ ] **Date de création** : `__/__/____`
- [ ] **Date d'expiration** : `__/__/____` (si applicable)

### **4. Projets Cloudflare Pages**
- [ ] **Projet "tech4elles"** : ☐ Existant ☐ À créer
- [ ] **Projet "tech4elles-admin"** : ☐ Existant ☐ À créer
- [ ] **Domaines associés** : `_________________`

---

## 🌐 **ÉTAPES DE RÉCUPÉRATION**

### **Étape 1 : Connexion Cloudflare**
```
1. Aller sur : https://dash.cloudflare.com
2. Se connecter avec vos identifiants
3. Noter l'Account ID (visible en haut à droite)
4. Aller dans "My Profile" → "API Tokens"
```

### **Étape 2 : Création du Token API**
```
1. Cliquer "Create Token"
2. Sélectionner "Custom token"
3. Configurer les permissions :
   - Account: Cloudflare Pages: Edit ✅
   - Zone: Zone: Edit ✅
   - Zone: Zone Settings: Edit ✅
4. Account Resources: Include All accounts
5. Zone Resources: Include All zones
6. Cliquer "Continue to summary"
7. Vérifier et cliquer "Create Token"
8. ⚠️ COPIER LE TOKEN IMMÉDIATEMENT !
```

### **Étape 3 : Création des Projets**
```
1. Aller dans "Pages" (menu principal)
2. Cliquer "Create a project"
3. Créer le projet "tech4elles"
4. Créer le projet "tech4elles-admin"
5. Noter les URLs générées
```

---

## 📝 **FORMULAIRE DE DEMANDE**

### **Informations Personnelles**
- **Nom** : `_________________`
- **Prénom** : `_________________`
- **Email** : `_________________`
- **Organisation** : `_________________`

### **Demande d'Accès**
- **Service demandé** : ☐ Compte Cloudflare ☐ API Token ☐ Projets Pages
- **Usage prévu** : Déploiement automatique Tech4Elles
- **Niveau d'accès** : ☐ Lecture ☐ Écriture ☐ Administration
- **Durée d'accès** : ☐ Permanent ☐ Temporaire ☐ Renouvelable

### **Justification**
```
Décrivez pourquoi vous avez besoin de ces accès :

________________________________________________
________________________________________________
________________________________________________
________________________________________________
```

---

## 🔍 **VÉRIFICATION DES INFORMATIONS**

### **Test de l'Account ID**
```bash
# Commande à exécuter pour vérifier
curl -X GET "https://api.cloudflare.com/client/v4/accounts/VOTRE_ACCOUNT_ID" \
  -H "Authorization: Bearer VOTRE_API_TOKEN" \
  -H "Content-Type: application/json"
```

**Résultat attendu** : `{"success": true, "result": {...}}`

### **Test de l'API Token**
```bash
# Commande à exécuter pour vérifier
curl -X GET "https://api.cloudflare.com/client/v4/accounts" \
  -H "Authorization: Bearer VOTRE_API_TOKEN" \
  -H "Content-Type: application/json"
```

**Résultat attendu** : `{"success": true, "result": [...]}`

### **Test des Projets Pages**
```bash
# Commande à exécuter pour vérifier
curl -X GET "https://api.cloudflare.com/client/v4/accounts/VOTRE_ACCOUNT_ID/pages/projects" \
  -H "Authorization: Bearer VOTRE_API_TOKEN" \
  -H "Content-Type: application/json"
```

**Résultat attendu** : `{"success": true, "result": [...]}`

---

## 📋 **CHECKLIST DE VALIDATION**

### **Avant Soumission**
- [ ] **Compte Cloudflare** créé et accessible
- [ ] **Account ID** récupéré et noté
- [ ] **API Token** généré avec bonnes permissions
- [ ] **Projets Pages** créés (tech4elles + tech4elles-admin)
- [ ] **Tests API** réussis avec curl
- [ ] **Informations** complétées dans ce formulaire

### **Après Réception**
- [ ] **Secrets GitHub** configurés (CF_API_TOKEN + CF_ACCOUNT_ID)
- [ ] **Workflow GitHub Actions** testé
- [ ] **Déploiement automatique** fonctionnel
- [ ] **URLs Cloudflare Pages** accessibles

---

## 🚨 **POINTS D'ATTENTION**

### **Sécurité**
- ⚠️ **Ne jamais partager** l'API Token
- ⚠️ **Utiliser des permissions minimales** (Custom token)
- ⚠️ **Régénérer le token** si compromis
- ⚠️ **Ne pas commiter** les secrets dans le code

### **Limitations**
- 📊 **Compte gratuit** : 100,000 requests/jour
- 🚀 **Pages gratuit** : 500 builds/mois
- 🌐 **Domaine personnalisé** : Configuration manuelle requise
- 🔄 **Cache** : Mise à jour après déploiement

---

## 📞 **CONTACT ET SUPPORT**

### **Support Cloudflare**
- **Documentation** : [developers.cloudflare.com](https://developers.cloudflare.com)
- **Support** : [support.cloudflare.com](https://support.cloudflare.com)
- **Community** : [community.cloudflare.com](https://community.cloudflare.com)

### **Support Tech4Elles**
- **Repository** : [github.com/what-06/tech4elles](https://github.com/what-06/tech4elles)
- **Issues** : [github.com/what-06/tech4elles/issues](https://github.com/what-06/tech4elles/issues)
- **Documentation** : `MODOP_DEPLOIEMENT_TECH4ELLES.md`

---

## ✅ **VALIDATION FINALE**

### **Signature**
- **Nom** : `_________________`
- **Date** : `__/__/____`
- **Signature** : `_________________`

### **Approbation**
- **Validé par** : `_________________`
- **Date** : `__/__/____`
- **Commentaires** : `_________________`

---

*Formulaire créé le 29 août 2025 - Demande d'accès Cloudflare pour Tech4Elles*

---

## 🎯 **PROCHAINES ÉTAPES APRÈS VALIDATION**

### **1. Configuration GitHub**
```bash
# Ajouter les secrets dans GitHub
CF_API_TOKEN=VOTRE_TOKEN_ICI
CF_ACCOUNT_ID=VOTRE_ACCOUNT_ID_ICI
```

### **2. Test du Déploiement**
```bash
# Pousser sur staging pour tester
git checkout staging
git push origin staging
```

### **3. Vérification**
- **GitHub Actions** : Workflow réussi
- **Cloudflare Pages** : Apps déployées
- **URLs accessibles** : tech4elles.pages.dev

**🎉 Tech4Elles sera alors déployé automatiquement sur Cloudflare !**












