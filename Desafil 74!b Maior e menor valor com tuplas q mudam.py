from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]

n = range(0, 10)
number = choice(n), choice(n), choice(n), choice(n), choice(n)
for count in range(0, len(number)):
    if count == 0:
        print('Os numeros são estes: ')
    print('{}{}{}'.format(choice(ca), number[count], lim), end=' ')
print('\n')
print('.·' * 20)
print('O maior numero é o: {}{}{}'.format(choice(ca), max(number), lim))
print('O menor numero é o: {}{}{}'.format(choice(ca), min(number), lim))
