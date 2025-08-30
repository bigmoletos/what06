# 🚀 **Tech4Elles - Projet de Mentoring**

## 📚 **Documentation Principale**

**📖 MODOP TECH4ELLES UNIFIÉ** : [`MODOP_TECH4ELLES_UNIFIE.md`](./MODOP_TECH4ELLES_UNIFIE.md)

> **🎯 GUIDE COMPLET** : Installation, configuration, démarrage et développement

**🚀 MODOP DÉPLOIEMENT** : [`MODOP_DEPLOIEMENT_TECH4ELLES.md`](./MODOP_DEPLOIEMENT_TECH4ELLES.md)

> **🌐 GUIDE DÉPLOIEMENT** : CI/CD, Cloudflare Pages, Docker, production

**📋 FORMULAIRE CLOUDFLARE** : [`FORMULAIRE_DEMANDE_CLOUDFLARE.md`](./FORMULAIRE_DEMANDE_CLOUDFLARE.md)

> **🔐 DEMANDE D'ACCÈS** : Formulaire complet pour récupérer les credentials Cloudflare

---

## 🚀 **Démarrage Rapide**

```bash
# 1. Test rapide de l'environnement
.\outils\test_quick.ps1

# 2. Démarrage automatique
.\outils\start_tech4elles.ps1

# 3. Ou démarrage manuel
cd Tech4Elles
pnpm dev
```

---

## 🛠️ **Installation et Configuration**

### **Installation des Outils (Windows)**
```bash
# Installation complète des outils (en tant qu'administrateur)
.\outils\install_tools.ps1

# Réparation de pnpm si problème d'accès
.\outils\fix_pnpm.ps1
```

### **Vérification de l'Environnement**
```bash
# Vérification complète de l'environnement
.\outils\check_setup.ps1

# Test rapide de l'environnement
.\outils\test_quick.ps1
```

### **Configuration de l'Environnement**
```bash
# Création du fichier .env complet
.\outils\create_env_complete.ps1

# Configuration Firebase (optionnel)
.\outils\firebase_setup.ps1
```

---

## 🌐 **URLs de Développement**

- **API Backend** : http://localhost:3333
- **App Utilisateur** : http://localhost:3000
- **App Admin** : http://localhost:3001
- **Base de données** : localhost:5435 (PostgreSQL)

---

## 🔐 **Accès Admin**

```
Email: pro@alopez.fr
Mot de passe: admin1234
```

---

## 📋 **Ordre d'Utilisation Recommandé**

### **Première Installation**
1. **Installation des outils** : `.\outils\install_tools.ps1` (administrateur)
2. **Vérification** : `.\outils\check_setup.ps1`
3. **Configuration** : `.\outils\create_env_complete.ps1`
4. **Démarrage** : `.\outils\start_tech4elles.ps1`

### **Utilisation Quotidienne**
1. **Test rapide** : `.\outils\test_quick.ps1`
2. **Démarrage** : `.\outils\start_tech4elles.ps1`

### **En Cas de Problème**
- **pnpm inaccessible** : `.\outils\fix_pnpm.ps1`
- **Configuration Firebase** : `.\outils\firebase_setup.ps1`
- **Vérification complète** : `.\outils\check_setup.ps1`

---

**📖 Pour plus d'informations, consultez le [MODOP TECH4ELLES UNIFIÉ](./MODOP_TECH4ELLES_UNIFIE.md)**
