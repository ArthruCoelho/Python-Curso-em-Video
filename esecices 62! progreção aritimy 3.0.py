import random

print('{}Progreção Aritimética{}'.format('\033[7m', '\033[m'))
lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
termo = pri
cont = 1
while cont <= 10:
    c = random.choice(ca)
    print('{}{}{} –> '.format(c, termo, lim), end='')
    cont += 1
    termo = termo + raz
valor = 2
cont = 1
while cont <= valor:
    c1 = random.choice(ca)
    print('{}{}{} –> '.format(c1, termo, lim), end='')
    cont += 1
    termo = termo + raz
    if cont == valor:
        valor = int(input('\nQuer quer mostre quantos mais termos a mais? '))
        if valor != 0:
            cont = 1
        if valor == 0:
            valor = 1
print("FIM")
