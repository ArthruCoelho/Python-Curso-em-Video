from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
products = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Trasferidor', 'Empacotador', 'Compasso', 'Mochila', 'Canetas',
            'Livro das Eras')
precos = (1.75, 2, 15.9, 25, 4.2, 9.99, 120.32, 22.3, 34.90, 0)
print('-' * 30, '\n{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 30)
for count in range(0, len(products)):
    print('{}{:.<30}{}R$ {}{:.2f}{}'.format(choice(ca), products[count], lim, choice(ca), precos[count], lim))
