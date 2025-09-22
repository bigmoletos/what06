// Script pour supprimer directement tous les utilisateurs
console.log('🧹 SUPPRESSION DIRECTE DES UTILISATEURS');

import Database from '@adonisjs/lucid/services/db';

async function cleanUsers() {
  try {
    console.log('1. 🗑️  Suppression des profils...');
    await Database.rawQuery('DELETE FROM mentees');
    await Database.rawQuery('DELETE FROM mentors');
    await Database.rawQuery('DELETE FROM admins');
    console.log('   ✅ Profils supprimés');

    console.log('2. 🗑️  Suppression des utilisateurs...');
    await Database.rawQuery('DELETE FROM users');
    console.log('   ✅ Utilisateurs supprimés');

    console.log('🎉 Nettoyage terminé!');
    process.exit(0);

  } catch (error) {
    console.error('❌ Erreur:', error.message);
    process.exit(1);
  }
}

cleanUsers();


