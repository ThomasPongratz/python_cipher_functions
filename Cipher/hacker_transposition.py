# Transposition Cipher Hack

import pyperclip, detect_english, cipher_transposition_decrypt

def main():
    my_message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e enlh
na indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
euarisfatt e mealefedhsppmgAnlnoe(c -or)alat r lw o eb nglom,Ain
one dtes ilhetcdba. t tg eturmudg,tfl1e1 v nitiaicynhrCsaemie-sp
ncgHt nie cetrgmnoa yc r,ieaa toesa- e a0m82e1w shcnth ekh
gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
aBercaeu thllnrshicwsg etriebruaisss d iorr."""
    my_message = 'Cenoonommstmme oo snnio. s s c'
    
    hacked_message = hack_transposition(my_message)

    if hacked_message == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hacked_message + '\n')
        pyperclip.copy(hacked_message)


def hack_transposition(message):
    print('Hacking...')
    print('(Press Ctrl-C to quit at any time.)')

    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decrypted_text = cipher_transposition_decrypt.decrypt_message(key, \
            message)

        if detect_english.is_english(decrypted_text):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decrypted_text[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None
    
if __name__ == '__main__':
    main()