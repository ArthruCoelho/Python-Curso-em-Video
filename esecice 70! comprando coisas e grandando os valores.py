print('{}Comprando!{}'.format('\033[7m', '\033[m'))
lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
total = 0
countmil = 0
barato = 0
count = 0
perg = '0'
nomeb = '0'
while True:
    count += 1
    print('.·' * 20, '\n')
    print('{:20}Produto{} {}n°{}{}\n'.format(c['verd'], lim, c['verd'], count, lim))
    produto = str(input('Digite o nome do produto: '))
    valor = int(input('Digite o vaor do produto: R$ '))
    if count == 1:
        barato = valor
        nomeb = produto
    elif valor < barato:
        barato = valor
        nomeb = produto
    if valor >= 1000:
        countmil += 1
    total += valor
    print('.·' * 20, '\n')
    while True:
        perg = str(input('Quer continuar [S/N]: ')).upper()
        if perg == 'S' or perg == 'N':
            break
    if perg == 'N':
        break
print('\nForam verificados {}{}{} produto(s)'.format(c['ciano'], count, lim))
print('O total foi de {}R${}{}\nTeve {}{}{} Produtos acima de {}R$1000{}\nO produto mais barato é o(a){}{}{},'
      ' de {}R${}{}.'
      .format(c['roxo'], total, lim, c['verm'], countmil, lim, c['verm'], lim, c['verd'], nomeb, lim, c['verd'], barato,
              lim))
print('\nFim!')
