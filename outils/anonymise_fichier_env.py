"""
anonymise_fichier_env.py

Ce script permet d'anonymiser les valeurs d'un fichier .env ou texte contenant des paires clé=valeur.
Pour chaque ligne contenant une variable d'environnement (clé=valeur), la valeur est masquée (ex : 'password=secret' devient 'password=sxxxT').
Le résultat est écrit dans un nouveau fichier suffixé '_anonymised.txt'.

Usage :
    input_file_path = "chemin/vers/.env"
    mask_values_in_file(input_file_path)

Auteur : bigmoletos
Date : 2025-09-12
"""


def mask_values_in_file(input_file_path):
    """
    Masque les valeurs des paires clé=valeur dans un fichier texte.
    La valeur est remplacée par son premier caractère, 'xxx', puis le dernier caractère (si la valeur a plus d'un caractère).
    Le résultat est écrit dans un nouveau fichier suffixé '_anonymised.txt'.

    Args:
        input_file_path (str): Chemin du fichier à anonymiser
    """
    # Lire toutes les lignes du fichier d'entrée
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Déterminer le chemin du fichier de sortie
    if input_file_path.endswith('.txt'):
        output_file_path = input_file_path.replace('.txt', '_anonymised.txt')
    else:
        output_file_path = input_file_path + '_anonymised.txt'

    masked_lines = []
    for line in lines:
        # Traiter uniquement les lignes contenant un '='
        if '=' in line:
            key, value = line.split('=', 1)
            stripped_value = value.strip()
            # Masquer la valeur : premier caractère + 'xxx' + dernier caractère (si >1)
            if len(stripped_value) > 0:
                masked_value = (stripped_value[0] + 'xxx' + stripped_value[-1]
                                if len(stripped_value) > 1 else 'x')
            else:
                masked_value = 'xxx'
            masked_lines.append(f"{key}={masked_value}\n")
        else:
            # Conserver les lignes sans '=' (ex : commentaires)
            masked_lines.append(line)

    # Écrire le résultat dans le fichier de sortie
    with open(output_file_path, 'w') as file:
        file.writelines(masked_lines)


# --- Utilisation du script ---
if __name__ == "__main__":
    import os

    # Obtenir le répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Remonter d'un niveau pour atteindre le répertoire racine du projet
    project_root = os.path.dirname(script_dir)
    default_env_path = os.path.join(project_root, ".env")

    # Chemin personnalisé pour Tech4Elles
    custom_env_path = "C:/programmation/Projets_python/what06/Tech4Elles/apps/api/.env"

    # === CHOIX DU CHEMIN À UTILISER ===
    # Décommentez la ligne souhaitée :

    # Pour utiliser le chemin par défaut :
    # input_file_path = default_env_path

    # Pour utiliser le chemin personnalisé (Tech4Elles) :
    input_file_path = custom_env_path

    # Pour spécifier un autre chemin manuellement :
    # input_file_path = "C:/chemin/vers/votre/fichier/.env"

    print(f"🔍 Recherche du fichier .env...")
    print(f"   Chemin par défaut: {default_env_path}")
    print(f"   Chemin personnalisé: {custom_env_path}")
    print(f"   Chemin utilisé: {input_file_path}")
    print()

    # Vérifier si le fichier existe
    if os.path.exists(input_file_path):
        print(f"✅ Fichier .env trouvé: {input_file_path}")
        print(f"🔄 Début de l'anonymisation...")
        mask_values_in_file(input_file_path)
        print("✅ Anonymisation terminée avec succès!")

        # Afficher le chemin du fichier anonymisé
        if input_file_path.endswith('.txt'):
            output_file = input_file_path.replace('.txt', '_anonymised.txt')
        else:
            output_file = input_file_path + '_anonymised.txt'
        print(f"📁 Fichier anonymisé créé: {output_file}")

    else:
        print(f"❌ Fichier .env non trouvé: {input_file_path}")
        print()
        print("💡 Solutions possibles:")
        print("   1. Vérifiez que le fichier .env existe au chemin spécifié")
        print("   2. Modifiez la variable 'custom_env_path' dans le script")
        print("   3. Utilisez le chemin par défaut en décommentant 'default_env_path'")
        print()
        print("📋 Chemins testés:")
        print(f"   - Par défaut: {default_env_path}")
        print(f"   - Personnalisé: {custom_env_path}")

        # Vérifier si le fichier existe dans le répertoire courant
        current_dir = os.getcwd()
        current_env = os.path.join(current_dir, ".env")
        if os.path.exists(current_env):
            print(f"   - Répertoire courant: {current_env} ✅")
            print(f"💡 Utilisez ce chemin: {current_env}")
