print('\033[7mFAZENDO UM TRINGULO!\033[m\nDigite o tamanho dos lados.\n')
a1 = float(input('Digite o segmento: '))
a2 = float(input('Digite o outro segmeno: '))
a3 = float(input('Digite o o ultimo segmento: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('\n\033[7;30;42mDá para fazer um triangulo!\033[m\n')
    if a1 == a2 and a2 == a3 and a3 == a1:
        print('Todos lados do seu triangulo são iguais!\nEntão ele é um triangulo {}EQUILÁTERO{}!'.format('\033[1;31m',
                                                                                                          '\033[m'))
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('Dois lados do seu triangulo são iguais!\nEntão ele é um triangulo {}ISÓCELES{}!'.format('\033[1;33m',
                                                                                                       '\033[m'))
    else:
        print('Todos os lados são diferentes!\nEntão ele é um tringulo {}ESCALENO{}!'.format('\033[1;36m', '\033[m'))
else:
    print('\n\033[1;31mNÃO da um triangulo\033[m')
