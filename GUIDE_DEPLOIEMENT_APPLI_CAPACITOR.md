guide = """# Guide pour Développer et Tester une Application Mobile avec Capacitor (Projet Svelte + Vercel)

## 1. Objectif
Déployer une petite application mobile (Android & iOS) et Web à partir d’un projet Svelte hébergé sur Vercel, en utilisant Capacitor.

---

## 2. Pré-requis
- Projet existant en **Svelte** déployé sur **Vercel**
- **Node.js** installé
- **Android Studio** (Windows/Linux/macOS)
- **Xcode** (uniquement si vous disposez d’un Mac, obligatoire pour publier sur iOS)
- Compte développeur :
  - **Google Play Console** (25€ à vie)
  - **Apple Developer** (99$/an)

---

## 3. Capacitor – Intégration
### Installation
```bash
npm install @capacitor/core @capacitor/cli
npx cap init
