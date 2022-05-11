from random import choice
print('{}FATORIAL{}'.format('\033[7m', '\033[m'))
l = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
number = int(input('Digite um numero: '))
c = number
f = 1
while c > 0:
    ca1 = choice(ca)
    f *= c
    print('{}{}{}'.format(ca1, c, l), end='')
    print(' X ' if c > 1 else ' = {}{}{}'.format('\033[7;;42m', f, '\033[m'), end='')
    c -= 1

