# Transposition Cipher Test

import random, sys
import cipher_transposition_encrypt as transEn
import cipher_transposition_decrypt as transDe

def main():
    random.seed(42)
    print()
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)     # string to list
        random.shuffle(message)
        message = ''.join(message)  # list back to string
        print('Test #%s: "%s..."' % (i+1, message[:50]))
        for key in range(1, int(len(message)/2)):
            encrypted = transEn.encrypt_message(key, message)
            decrypted = transDe.decrypt_message(key, encrypted)
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('\nTransposition cipher test passed.\n')

if __name__ == '__main__':
    main()