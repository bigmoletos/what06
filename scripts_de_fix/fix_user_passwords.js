// Script pour corriger les mots de passe des utilisateurs non-admin

import { BaseCommand } from '@adonisjs/core/ace'
import User from '#models/user'
import AdvancedHashService from '#services/advanced_hash_service'

export default class FixUserPasswords extends BaseCommand {
  static commandName = 'fix:passwords'
  static description = 'Corrige les mots de passe non hashés des utilisateurs'

  async run() {
    this.logger.info('🔧 Correction des mots de passe utilisateurs...')

    try {
      // Trouver tous les utilisateurs non-admin avec des mots de passe en clair
      const users = await User.query()
        .where('type', '!=', 'admin')
        .whereNotNull('password')

      this.logger.info(`📊 ${users.length} utilisateurs non-admin trouvés`)

      for (const user of users) {
        // Vérifier si le mot de passe est déjà hashé (commence par $2b$ pour bcrypt)
        if (!user.password.startsWith('$2b$')) {
          this.logger.info(`🔄 Correction du mot de passe pour: ${user.email}`)

          // Le mot de passe est en clair, le hasher
          const hashedPassword = await AdvancedHashService.make(user.password)
          user.password = hashedPassword
          await user.save()

          this.logger.success(`✅ Mot de passe corrigé pour: ${user.email}`)
        } else {
          this.logger.info(`✅ Mot de passe déjà hashé pour: ${user.email}`)
        }
      }

      this.logger.success('🎉 Correction terminée !')

    } catch (error) {
      this.logger.error('❌ Erreur lors de la correction:', error.message)
    }
  }
}


