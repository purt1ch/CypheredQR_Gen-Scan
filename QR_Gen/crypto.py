def encrypt(code):
    print(code)
    result = ''
    n = 0
    for i in code:
        i = ord(i) + n
        n += 1
        result += chr(i)
        if n == 10:
            n = 0
    return result
def decrypt(code):
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
        choice = input('Зашифровать (1) - Расшифровать (2) - Выйти (3): ')
        if choice == '1':
            code = input('Введите текст для зашифровки: ')
            tmp = encrypt(code)
            print('\n', 'Зашифрованый текст: ' + tmp)

        elif choice == '2':
            code = input('Введите текст для расшифровки: ')
            tmp = decrypt(code)
            print('\n', 'Расшифрованный текст: ' + tmp)
        elif choice == '3':
            break
        else:
            print('Неверный выбор, попробуйте снова')