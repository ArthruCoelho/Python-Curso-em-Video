import random
l = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
print('{}Progreção Aritimética 2.0{}'.format('\033[7m', l))
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pri
cont = 1
while cont <= 10:
    c = random.choice(ca)
    print('{}{}{} –> '.format(c, termo, l), end='')
    cont += 1
    termo = termo + raz
