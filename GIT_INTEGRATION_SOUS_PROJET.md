# Intégration d'un Sous-Projet Git avec `git subtree`

Ce guide explique comment intégrer un sous-projet Git dans un dépôt principal en utilisant `git subtree`. Il couvre également les étapes de débogage en cas de problèmes.

---

## Prérequis
- Avoir Git installé sur votre machine.
- Avoir les droits de lecture sur le dépôt du sous-projet.
- Être dans le répertoire de votre dépôt principal.

---

## Étapes d'Intégration

### 1. Supprimer le Submodule (si nécessaire)
Si le sous-projet est déjà ajouté en tant que submodule, commencez par le supprimer.

#### Commandes :
```bash
# Supprimer le submodule de l'index Git
git rm --cached Tech4Elles

# Supprimer les fichiers du submodule dans `.git/modules`
rm -rf .git/modules/Tech4Elles

# Supprimer l'entrée du submodule dans `.gitmodules` (si le fichier existe)
rm .gitmodules

# Valider les changements
git add .gitmodules
git commit -m "Suppression du submodule Tech4Elles"
```

---

### 2. Ajouter le Dépôt Distant du Sous-Projet
Ajoutez le dépôt distant du sous-projet en utilisant HTTPS.

#### Commandes :
```bash
# Ajouter le dépôt distant
git remote add -f sous_depot_tech4elles https://github.com/WHAT-06/Tech4Elles.git
```

#### Débogage :
- **Erreur :** `error: remote sous_depot_tech4elles already exists.`
  **Solution :** Mettez à jour l'URL du dépôt distant existant.
  ```bash
  git remote set-url sous_depot_tech4elles https://github.com/WHAT-06/Tech4Elles.git
  ```

---

### 3. Récupérer les Dernières Modifications
Récupérez les dernières modifications du sous-projet.

#### Commandes :
```bash
git fetch sous_depot_tech4elles
```

---

### 4. Intégrer le Sous-Projet avec `git subtree`
Intégrez le sous-projet dans un sous-répertoire de votre dépôt principal.

#### Commandes :
```bash
git subtree add --prefix=sous_depot_tech4elles sous_depot_tech4elles dev --squash
```

#### Débogage :
- **Erreur :** `fatal: working tree has modifications. Cannot add.`
  **Solution :** Validez ou mettez de côté vos modifications en attente.
  ```bash
  # Vérifier les modifications en attente
  git status

  # Valider les modifications
  git add .
  git commit -m "Validation des modifications en attente"

  # Ou mettre de côté les modifications
  git stash
  ```

---

### 5. Vérifier l'Intégration
Vérifiez que le sous-projet a été intégré correctement.

#### Commandes :
```bash
# Vérifier l'historique des commits
git log

# Vérifier les fichiers intégrés
ls sous_depot_tech4elles/
```

---

## Problèmes Courants et Solutions

### Problème : Permission Denied (Publickey)
Si vous utilisez SSH et que vous rencontrez une erreur de permission, passez à HTTPS.

#### Solution :
```bash
git remote set-url sous_depot_tech4elles https://github.com/WHAT-06/Tech4Elles.git
```

---

### Problème : Submodule a des Modifications Non Validées
Si le submodule a des modifications non validées, vous devez les valider ou les annuler.

#### Solution :
```bash
# Accéder au répertoire du submodule
cd Tech4Elles

# Vérifier les modifications
git status

# Valider les modifications
git add .
git commit -m "Validation des modifications dans le submodule"

# Ou annuler les modifications
git restore .

# Revenir au répertoire principal
cd ..
```

---

### Problème : Le Submodule Existe Toujours dans le Dépôt Principal
Si le submodule existe toujours dans le dépôt principal après suppression, assurez-vous de bien l'avoir supprimé de `.gitmodules` et de `.git/modules`.

#### Solution :
```bash
# Supprimer le submodule de l'index Git
git rm --cached Tech4Elles

# Supprimer les fichiers du submodule dans `.git/modules`
rm -rf .git/modules/Tech4Elles

# Valider les changements
git commit -m "Suppression définitive du submodule Tech4Elles"
```

---

### Problème : Le Répertoire de Destination Existe Déjà
Si le répertoire de destination (`sous_depot_tech4elles`) existe déjà, supprimez-le avant d'utiliser `git subtree`.

#### Solution :
```bash
rm -rf sous_depot_tech4elles
```

---

## Conclusion
En suivant ces étapes, vous devriez pouvoir intégrer un sous-projet Git dans votre dépôt principal en utilisant `git subtree`. Si vous rencontrez d'autres problèmes, assurez-vous de vérifier les messages d'erreur et de suivre les solutions de débogage proposées.

---

## Résumé des Commandes Utiles

| Commande | Description |
|----------|-------------|
| `git rm --cached Tech4Elles` | Supprime le submodule de l'index Git. |
| `rm -rf .git/modules/Tech4Elles` | Supprime les fichiers du submodule dans `.git/modules`. |
| `git remote add -f sous_depot_tech4elles https://github.com/WHAT-06/Tech4Elles.git` | Ajoute le dépôt distant en HTTPS. |
| `git remote set-url sous_depot_tech4elles https://github.com/WHAT-06/Tech4Elles.git` | Met à jour l'URL du dépôt distant pour utiliser HTTPS. |
| `git fetch sous_depot_tech4elles` | Récupère les dernières modifications du sous-projet. |
| `git subtree add --prefix=sous_depot_tech4elles sous_depot_tech4elles dev --squash` | Intègre le sous-projet dans votre projet principal. |
| `git status` | Vérifie les modifications en attente. |
| `git add .` | Ajoute toutes les modifications à l'index. |
| `git commit -m "message"` | Valide les modifications. |
| `git stash` | Met de côté les modifications non validées. |
| `git log` | Vérifie l'historique des commits. |