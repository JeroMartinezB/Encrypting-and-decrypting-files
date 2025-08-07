# VIGENÈRE CIPHER
def vigenere_cipher(line, key, encrypt=True):
    result = []
    # Make everthing uppercase
    line = line.upper()
    key = key.upper()

    key_index = 0
    direction = -1

    # Confirm direction
    # Positive for encryption, negative for decryption
    if encrypt:
        direction = 1
    
    # Iterate through characters
    for char in line:
        if char.isalpha():
            # Calculate shift
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Apply shift
            applied_shift = (ord(char) - ord('A') + direction * shift) % 26
            # Append characters to the result
            result.append(chr(applied_shift + ord('A')))
            key_index += 1
        else:
            result.append(char) # Non-letters stay the same

    return ''.join(result) 
    

# ENCRYPT FILE
def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as input, open(output_file, 'w') as output:
        # Encrypt line by line
            for line in input:
                output.write(vigenere_cipher(line, key, encrypt=True)) # Write to output file

        print("Encryption complete.")

    except FileNotFoundError:
        print("File not found")


# DECRYPT FILE
def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as input, open(output_file, 'w') as output:
        # Decrypt line by line
            for line in input:
                output.write(vigenere_cipher(line, key, encrypt=False)) #Write 
        
        print("Decryption complete.")

    except FileNotFoundError:
        print("File not found")


# MAIN PROGRAM --------------------------------------------------------------------------------------
def main():
    
    # Input validation
    while(True):
        user_input = input("Are you encrypting or decrypting? 1 for encrypt, 2 for decrypt: ")

        if user_input in ("1", "2"):
            break
        else:
            print("Wrong Input, try again!")

    # Input and output files
    input_file = input("Input file name: ")
    output_file = input("Output file name: ") 
    
    # Validate the key
    while True:
        key = input("Please enter the key: ")
        if not key.isalpha():
            print("The key needs to be only letters")
        else:
            break

    # Encrypt
    if user_input == "1":
        encrypt_file(input_file, output_file, key)
    # Decrypt
    else:
        decrypt_file(input_file, output_file, key)



main()
