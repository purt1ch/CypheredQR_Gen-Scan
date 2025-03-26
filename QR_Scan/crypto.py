def encrypt(code):
    print(code)
    result = ''
    n = 0
    for i in code: # Every character shifts up in ASCII position gradually by 1, 2, 3 up to 10
        i = ord(i) + n # in a loop
        n += 1
        result += chr(i)
        if n == 10:
            n = 0
    return result
def decrypt(code): # Same thing in reverse
    print(code)
    result = ''
    i = 0
    n = 0
    for i in code:
        i = ord(i) - n
        n += 1
        result += chr(i)
        if n == 10:
            n = 0
    return result

if __name__ == '__main__':
    while True:
        choice = input('Encrypt (1) - Decrypt (2) - Quit (3): ')
        if choice == '1':
            code = input('Enter the text for encryption: ')
            tmp = encrypt(code)
            print('\n', 'Encrypted text: ' + tmp)

        elif choice == '2':
            code = input('Enter the text for decryption: ')
            tmp = decrypt(code)
            print('\n', 'Decrypted text: ' + tmp)
        elif choice == '3':
            break
        else:
            print('Error: Wrong choice, try again...')