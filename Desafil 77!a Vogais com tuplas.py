from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]

strings = ('Arthur', 'Cachorro', 'didio', 'miseira', 'mamão')
for count in strings:
    print('Na palavra {}{}{} temos: '.format(choice(ca), count, lim))
    for letra in count:
        if letra.lower() in 'aâãáàéèôõíìîeiou':
            print('{}{}{}'.format(choice(ca), letra.lower(), lim), end=' ')
    print('\n')
print('Fim!')
