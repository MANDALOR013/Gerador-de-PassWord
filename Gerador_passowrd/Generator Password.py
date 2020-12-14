#Programa para gerar várias senhas
import random

#Maiúsculas
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Minúsculas
lowercase_letters = uppercase_letters.lower()
#Números
digits = '0123456789'
#Simbolos
symbols = '() {} [] , ; : . _ /\\?+*= '

upper, lower, nums, syms = True, True, True, False

all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = ''.join(random.sample(all, length))
    print(password)
