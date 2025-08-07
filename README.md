# Encrypting-and-decrypting-files

This program implements the Vigenère cipher: an early form of encryption for text. This form of encryption was first used around the year 1500, and was thought to be unbreakable until 1868. With an appropriately sized truly random key, this can be ‘perfect’ encryption.

**What does it do?**

The program is able to both encrypt and decrypt files. It will first ask if the user is encrypting or decrypting. It will then ask for the input file, the output file, and finally it will have the user type the encryption key. If encrypting, the ciphertext is written to the output file. If decrypting, the decrypted plaintext is accordingly written to the output file.

**Details**

This specific program only encrypts alphabetical characters, Any character which isn’t a letter (punctuation, numbers) is written to the output file without modification. Captialization of all the letters is also applied for simplicity purposes.

A sample file is included to test the program.
