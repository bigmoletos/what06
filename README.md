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
- **App Utilisateur** : http://localhost:5180
- **App Admin** : http://localhost:5181
- **Base de données** : localhost:5435 (PostgreSQL)

## 🚀 **Nouvelles Fonctionnalités Disponibles**

### **💬 Système de "Premier Contact" (Poke/Bonjour)**
- **Bouton Poke** : Envoi de messages simples entre mentorées et marraines
- **Gestion des Contacts** : Page `/contacts` avec filtres et actions
- **Dashboard Admin** : `/admin` et `/admin/contacts-stats` avec métriques
- **Types de Contact** : Poke, Message, Demande de mentorat
- **Statuts** : En attente, Accepté, Rejeté, Expiré

### **📊 Métriques et Statistiques**
- **Taux de conversion** des contacts
- **Répartition** par statut et type
- **Suivi en temps réel** des interactions
- **Interface admin** intuitive et responsive

---

## 🔐 **Accès Admin**

```
Email: pro@alopez.fr
Mot de passe: *****
```

## 🧪 **Comptes de Test - Fonctionnalité "Premier Contact"**

### **👩‍🎓 Lycéennes (Mentorées)**
```
Emma Martin     - emma.martin@test.com     / password123
Léa Dubois      - lea.dubois@test.com      / password123
Chloé Bernard   - chloe.bernard@test.com   / password123
Jade Petit      - jade.petit@test.com      / password123
Zoé Moreau      - zoe.moreau@test.com      / password123
```

### **👩‍🏫 Marraines (Mentors)**
```
Sophie Leroy    - sophie.leroy@test.com    / password123
Marie Garcia    - marie.garcia@test.com    / password123
Isabelle Roux   - isabelle.roux@test.com   / password123
Catherine Simon - catherine.simon@test.com / password123
Valérie Michel  - valerie.michel@test.com  / password123
```

### **💡 Utilisation des Comptes de Test**
- **Test complet** de la fonctionnalité "Premier Contact"
- **Simulation** d'interactions entre mentorées et marraines
- **Validation** des pokes, messages et demandes
- **Test** du dashboard admin avec métriques
- **Pas besoin** de créer manuellement des comptes

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

### **🧪 Génération des Données de Test**
```bash
# Depuis le dossier API
cd Tech4Elles/apps/api
node ace db:seed

# Ou depuis la racine du projet
cd Tech4Elles/apps/api && node ace db:seed
```

**💡 Note** : Les données de test incluent 5 lycéennes, 5 marraines et 12 contacts variés pour tester la fonctionnalité "Premier Contact".

---

**📖 Pour plus d'informations, consultez le [MODOP TECH4ELLES UNIFIÉ](./MODOP_TECH4ELLES_UNIFIE.md)**
