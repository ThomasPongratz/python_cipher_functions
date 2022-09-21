# Transposition Cipher Encrypt/Decrypt File
import time, os, sys
import cipher_transposition_encrypt as transEn
import cipher_transposition_decrypt as transDe

def main():
    #input_filename = 'frankenstein.txt'
    #output_filename = 'frankenstein.encrypted.txt'
    input_filename = 'frankenstein.encrypted.txt'
    output_filename = 'frankenstein.decrypted.txt'
    my_key = 10
    #my_mode = 'encrypt' # Set to 'encrypt' or 'decrypt'
    my_mode = 'decrypt'
    #my_key = int(input('Enter key: '))
    #my_mode = input('Enter Mode: ')

    # if input-file doesn't exist:
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % (input_filename))
        sys.exit()

    # if output-file already exists:
    if os.path.exists(output_filename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %\
            (output_filename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # read in message from input-file:
    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print('%sing...' % (my_mode.title()))

    # measure how long the encryption/decryption takes:
    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transEn.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transDe.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print('%sion time: %s seconds' % (my_mode.title(), total_time))

    # write to output-file:
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print('Done %sing %s (%s characters).' % (my_mode, input_filename, \
        len(content)))
    print('%sed file is %s.' % (my_mode.title(), output_filename))

if __name__ == '__main__':
    main()