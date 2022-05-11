from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
ca1 = choice(ca)
print('{}DE 0 A 20!{}'.format('\033[7m', lim))
variable = range(0, 20)
while True:
    number = int(input('Digite um numero de 0 a 20: '))
    if 0 <= number <= 20:
        break
print('Você digitou o numero: ', end=' ')
if number == 0:
    print(f'{ca1}Zero{lim}', end='')
elif number == 1:
    print(f'{ca1}Um{lim}', end='')
elif number == 2:
    print(f'{ca1}Dois{lim}', end='')
elif number == 3:
    print(f'{ca1}Tres{lim}', end='')
elif number == 4:
    print(f'{ca1}Quatro{lim}', end='')
elif number == 5:
    print(f'{ca1}Cinco{lim}', end='')
elif number == 6:
    print(f'{ca1}Seis{lim}', end='')
elif number == 7:
    print(f'{ca1}Sete{lim}', end='')
elif number == 8:
    print(f'{ca1}Oito{lim}', end='')
elif number == 9:
    print(f'{ca1}Nove{lim}', end='')
elif number == 10:
    print(f'{ca1}Dez{lim}', end='')
elif number == 11:
    print(f'{ca1}Onze{lim}', end='')
elif number == 12:
    print(f'{ca1}Doze{lim}', end='')
elif number == 13:
    print(f'{ca1}Treze{lim}', end='')
elif number == 14:
    print(f'{ca1}Quatorze{lim}', end='')
elif number == 15:
    print(f'{ca1}Quinze{lim}', end='')
elif number == 16:
    print(f'{ca1}Dezesseis{lim}', end='')
elif number == 17:
    print(f'{ca1}Dezessete{lim}', end='')
elif number == 18:
    print(f'{ca1}Dezoito{lim}', end='')
elif number == 19:
    print(f'{ca1}Dezenove{lim}', end='')
else:
    print(f'{ca1}Vinte{lim}', end='')
