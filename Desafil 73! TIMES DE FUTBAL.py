from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vítoria', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
for count in range(0, len(times)):
    if count == 0:
        print(' Lista de times: ')
    print(' {}{}{}'.format(choice(ca), times[count], lim), end=', ')
    if count == 10:
        print(' ')
count = 0
print('\n', '<>' * 20)
while count != 5:
    if count == 0:
        print(' Cinco primeiros colocados: ')
    print(' {}{}{}'.format(choice(ca), times[count], lim), end=', ')
    count += 1
print('\n', '<>' * 20)
count = -4
while count != 0:
    if count == -4:
        print(' Quatro ultimos colocados: ')
    print(' {}{}{}'.format(choice(ca), times[count], lim), end=', ')
    count += 1
print('\n', '<>' * 20)
print('Times em ordem ALFABETA: ')
print('{}'.format(sorted(times)))
print('\n', '<>' * 20)
for count in range(0, len(times)):
    time = times[count]
    if time == 'Chapecoense':
        print('\nA chapecoense está na posição {}{}{}'.format(choice(ca), count + 1, lim))
print('\nFIM')