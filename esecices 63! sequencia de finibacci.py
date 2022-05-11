from random import choice

print('{}SEQUENCIA DE FIBONACCI{}'.format('\033[7m', '\033[m'))
lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
per = int(input('Digite quantos termos você deseja mostrar: '))
print('·․' * 25)
n = 3
fibo1 = 0
fibo2 = 1
fibo = 0
print('{}{} {}->{} {} {} -> '.format(c['verd'], fibo1, lim, c['verd'], fibo2, lim,), end='')
while per != n:
    ca1 = choice(ca)
    n += 1
    fibo = fibo1 + fibo2
    if n % 10 == 0:
        print('\n')
        n1 = 0
    print('{}{}{} –> '.format(ca1, fibo, lim), end='')
    fibo1 = fibo2
    fibo2 = fibo
print('\nFim')
