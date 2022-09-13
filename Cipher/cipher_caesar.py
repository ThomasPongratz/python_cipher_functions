# Caesar Cipher
import pyperclip

message = 'abcdef This is my secret message.'

# encryption/decryption-key:
key = 0
key = int(input('\nEnter encryption-key [1 - 26]: '))
if key == 0:
    key = 13
# set mode - encrypt / decrypt:
mode = 'encrypt'
mode = input("Enter 'e' for encrypt, 'd' for decrypt: ")
if (mode == 'd'):
    mode = 'decrypt'
else:
    mode = 'encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789 !?.'
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translated_index = symbol_index + key
        elif mode == 'decrypt':
            translated_index = symbol_index - key

        if translated_index >= len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)

        translated = translated + SYMBOLS[translated_index]
    else:
        translated = translated + symbol

print('\n[ KEY: ' + str(key) + ' ] [ MODE: ' + mode + ' ]:\n')
print(translated + '\n')
pyperclip.copy(translated)