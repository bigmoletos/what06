// Test simple de hachage avec bcrypt
import bcrypt from 'bcrypt'

console.log('=== TEST BCRYPT DIRECT ===')

const password = 'azerty'
const hash = await bcrypt.hash(password, 10)

console.log('Password:', password)
console.log('Hash généré:', hash)
console.log('Format:', hash.startsWith('$2b$') ? 'bcrypt' : 'autre')

const isValid = await bcrypt.compare(password, hash)
console.log('Vérification:', isValid)

// Test avec le hash de la DB
const dbHash = '$bcrypt$v=98$r=10$LSwGCVu3c/NvaRpKjtC69w$DV2hcs6icwfV1rxNsiy7vJfynqoZ/kY'
console.log('\n=== TEST AVEC HASH DB ===')
console.log('DB Hash:', dbHash)
console.log('Format DB:', dbHash.startsWith('$bcrypt$') ? 'bcrypt' : 'autre')

// Essayer de convertir le format
const convertedHash = dbHash.replace('$bcrypt$v=98$r=10$', '$2b$10$')
console.log('Hash converti:', convertedHash)

const isValidDB = await bcrypt.compare(password, convertedHash)
console.log('Vérification DB:', isValidDB)
