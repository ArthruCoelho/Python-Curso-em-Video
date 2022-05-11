from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
perg = 'm'
print('=' * 20, '\n{}B{}{}A{}{}N{}{}C{}{}O{} {}DO{} {}A{}{}R{}{}T{}{}H{}{}U{}{}R{}'
      .format(choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim,
              choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim, choice(ca), lim,))
print('=' * 20)

while True:
    while True:
        valor = int(input('Que valor você quer sacar: R$ '))
        while True:
            f1 = int(valor / 50)
            if f1 > 0:
                f2 = f1 * 50
                valor -= f2
                break
            else:
                break
        while True:
            g1 = int(valor / 20)
            if g1 >= 1:
                g2 = g1 * 20
                valor -= g2
                break
            else:
                break
        while True:
            h1 = int(valor / 10)
            if h1 > 0:
                h2 = h1 * 10
                valor -= h2
                break
            else:
                break
        while True:
            j1 = int(valor / 1)
            if j1 > 0:
                valor -= j1
                break
            else:
                break
        if valor == 0:
            break
        else:
            break
    print('\n')
    if f1 == 1:
        print('Total de {} cédulas de {}R$50{}'.format(f1, c['verd'], lim))
    if f1 != 0 and f1 != 1:
        print('Total de {} cédulas de {}R$50{}'.format(f1, c['verd'], lim))
    if g1 == 1:
        print('Total de {} cédulas de {}R$20{}'.format(g1, c['amare'], lim))
    if g1 != 0 and g1 != 1:
        print('Total de {} cédulas de {}R$20{}'.format(g1, c['amare'], lim))
    if h1 == 1:
        print('Total de {} cédulas de {}R$10{}'.format(h1, c['verm'], lim))
    if h1 != 0 and h1 != 1:
        print('Total de {} cédulas de {}R$10{}'.format(h1, c['verm'], lim))
    if j1 == 1:
        print('Total de {} moedas de {}R$1{}'.format(j1, c['roxo'], lim))
    if j1 != 0 and j1 != 1:
        print('Total de {} moedas de {}R$1{}'.format(j1, c['roxo'], lim))
    print('=' * 20)
    while True:
        perg = str(input('Quer testar novamente? [{}S{}/{}N{}] '.format(c['verd'], lim, c['verm'], lim))).upper()
        if perg == 'N' or 'S':
            print('=' * 20)
            break
    if perg == 'N':
        break
