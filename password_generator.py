import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? (y / n) ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? (y / n) ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? (y / n) ')
pwd_punctuation = input(
    'Включать ли в пароль символы "!#$%&*+-=?@^_"? (y / n) ')
pwd_exceptions = input(
    'Исключать ли неоднозначные символы "il1Lo0O"? (y / n) ')

if pwd_digits == 'y':
    chars += digits
if pwd_uppercase == 'y':
    chars += uppercase_letters
if pwd_lowercase == 'y':
    chars += lowercase_letters
if pwd_punctuation == 'y':
    chars += punctuation
if pwd_exceptions == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(lenght, chars, quant):
    password_list = []
    passw = ''
    for i in range(quant):
        for i in range(lenght):
            passw += random.choice(chars)
        password_list.append(passw)
        passw = ''
    print('Ваши пароли:', *password_list, sep='\n')

generate_password(pwd_len, chars, pwd_quantity)