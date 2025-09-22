-- Script SQL pour supprimer les utilisateurs non-admin et permettre de relancer les seeders

-- Supprimer les profils liés d'abord (contraintes de clé étrangère)
DELETE FROM mentees WHERE user_id IN (SELECT id FROM users WHERE type != 'admin');
DELETE FROM mentors WHERE user_id IN (SELECT id FROM users WHERE type != 'admin');

-- Supprimer les utilisateurs non-admin
DELETE FROM users WHERE type != 'admin';

-- Vérifier le résultat
SELECT email, type, LEFT(password, 20) as password_start FROM users;


