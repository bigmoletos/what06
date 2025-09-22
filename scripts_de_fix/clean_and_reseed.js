// Script pour nettoyer complètement les utilisateurs et relancer les seeders
// Usage: node clean_and_reseed.js

console.log('🧹 NETTOYAGE COMPLET ET RESEEDING');
console.log('==================================');

import { execSync } from 'child_process';

try {
  console.log('1. 🗑️  Rollback des migrations...');
  execSync('node ace migration:rollback --batch=0', { stdio: 'inherit' });

  console.log('2. 🔄 Re-exécution des migrations...');
  execSync('node ace migration:run', { stdio: 'inherit' });

  console.log('3. 🌱 Seeding admin...');
  execSync('node ace db:seed --files="database/seeders/admin_seeder.ts"', { stdio: 'inherit' });

  console.log('4. 🌱 Seeding mentees...');
  execSync('node ace db:seed --files="database/seeders/mentee_seeder.ts"', { stdio: 'inherit' });

  console.log('5. 🌱 Seeding mentors...');
  execSync('node ace db:seed --files="database/seeders/mentor_seeder.ts"', { stdio: 'inherit' });

  console.log('🎉 NETTOYAGE ET RESEEDING TERMINÉS!');

} catch (error) {
  console.error('❌ Erreur:', error.message);
  process.exit(1);
}


