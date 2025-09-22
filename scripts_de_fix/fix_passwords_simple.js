// Script simple pour corriger les mots de passe en clair
// Utiliser avec: node fix_passwords_simple.js

const { Database } = require('@adonisjs/lucid/database')
const bcrypt = require('bcrypt')

async function fixPasswords() {
  console.log('🔧 Correction des mots de passe...')

  try {
    // Se connecter à la base de données
    const Database = require('@adonisjs/lucid/database')

    // Trouver tous les utilisateurs avec des mots de passe en clair
    const users = await Database.from('users')
      .where('type', '!=', 'admin')
      .whereNotNull('password')

    console.log(`📊 ${users.length} utilisateurs trouvés`)

    for (const user of users) {
      // Vérifier si le mot de passe est déjà hashé
      if (!user.password.startsWith('$2b$')) {
        console.log(`🔄 Correction pour: ${user.email}`)

        // Hasher le mot de passe en clair
        const hashedPassword = await bcrypt.hash(user.password, 10)

        // Mettre à jour en base
        await Database.from('users')
          .where('id', user.id)
          .update({ password: hashedPassword })

        console.log(`✅ Corrigé: ${user.email}`)
      } else {
        console.log(`✅ Déjà hashé: ${user.email}`)
      }
    }

    console.log('🎉 Correction terminée !')

  } catch (error) {
    console.error('❌ Erreur:', error.message)
  }
}

fixPasswords()


