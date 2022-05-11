from random import choice

print('{}Progreção Aritimética{}'.format('\033[7m', '\033[m'))
lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
count = 0
number = 0
print('․·' * 20)
while True:
    if count == 0:
        number = int(input('Digite um numero para ver na tabuada: '))
    count += 1
    if number <= -1:
        break
    if number >= 0:
        ca1 = choice(ca)
        ca2 = choice(ca)
        ca3 = choice(ca)
        print('{}{}{} x {}{:2}{} = {}{}{}'.format(ca1, number, lim, ca2, count, lim, ca2, number * count, lim))
    if count == 10:
        count = 0
        print('․·' * 20)


print(f'\nVocê digitou {number}, que é um numero negativo\nO programa sera encerrado.\n\033[1mVolte sempre!\033[m')
