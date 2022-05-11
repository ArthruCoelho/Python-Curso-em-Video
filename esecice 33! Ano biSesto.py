ano = int(input('Digite o ano: '))
bisexto = ano % 4
if bisexto == 0:
    print('O ano {} é BISEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISEXTO.'.format(ano))
