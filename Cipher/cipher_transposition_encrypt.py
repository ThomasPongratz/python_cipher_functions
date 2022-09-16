# Transposition Cipher Encryption

import pyperclip

def main():
    #my_message = 'Common sense is not so common.'
    my_message = input('Enter text: ')
    #my_key = 8
    my_key = int(input('Enter key: '))

    ciphertext = encrypt_message(my_key, my_message)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)

def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key
    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)

# If cipher_transposition_encrypt.py is run (instead of imported as a module) 
# call the main() function:
if __name__ == '__main__':
    main()