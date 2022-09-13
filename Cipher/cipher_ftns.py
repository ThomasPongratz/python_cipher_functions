# Reverse Cipher
def reverse_cipher():
    message = input('Enter message: ')
    translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i -= 1

    print(translated)