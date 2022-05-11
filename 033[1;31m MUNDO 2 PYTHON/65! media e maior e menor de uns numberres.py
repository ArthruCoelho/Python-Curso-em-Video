import random

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
ca1 = random.choice(ca)
ca2 = random.choice(ca)
print('{}VARIOS NUMEROS{}'.format('\033[7m', lim))
number = int(input('Digite um numero: '))
perg = str(input('Quer continuar? [n/s] ')).upper()
count = 1
maior = number
menor = number
soma = number
while perg != 'N':
    soma += number
    count += 1
    number = int(input('Digite o numero: '))
    perg = str(input('Quer continuar? [n/s] ')).upper()
    if number > maior:
        maior = number
    elif number < menor:
        menor = number
media = soma / count
if count == 1:
    print('Você digitou apenas um numero: {}{}{}'.format(ca1, number, lim))
else:
    print('Foram escritos {}{}{} numero(s)!\nA soma é {}{}{}!\nA média é {}{}{}!\nO maior valor é {}{}{}'
          ' e o menor é {}{}{}'
          .format(ca1, count, lim, ca2, soma, lim, random.choice(ca), media.__round__(1), lim, random.choice(ca), maior
                  , lim, random.choice(ca), menor, lim))
