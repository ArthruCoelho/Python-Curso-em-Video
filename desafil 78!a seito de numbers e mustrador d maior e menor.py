from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]

n = range(1, 10)
number = [9, 8, 4, 3, 2]
print('Os numeros são: ')
count = 0
mais = []
menos = []
for count in range(0, len(number)):
    print(f'{choice(ca)}{number[count - 1]}{lim}', end=' | ')
    count += 1
print('\n\n', '=' * 20, f'\nO maior numero é: {choice(ca)}{max(number)}{lim}, na posição : ')
for i, v in enumerate(number):
    if v == max(number):
        print(i + 2, end=', ')
print(f'\nO menor numero é: {choice(ca)}{min(number)}{lim}  na posição : ')
for i, v in enumerate(number):
    if v == min(number):
        print(i + 2, end=', ')
