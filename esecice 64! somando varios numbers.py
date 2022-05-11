import random

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
ca1 = random.choice(ca)
ca2 = random.choice(ca)
print('{}SOMANDO VARIOS NUMEROS{}'.format('\033[7m', '\033[m'))
number = 0
soma = 0
count = 0
while number != 999:
    number = int(input('Digite um numero [999 para sair]: '))
    if number != 999:
        soma += number
        count += 1
print('A soma de {}{}{} numeros é {}{}{}'.format(ca1, count, lim, ca2, soma, lim))