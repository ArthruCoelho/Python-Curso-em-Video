print('\033[7mCOFEDERAÇÂO NACIONAL DE NATAÇÂO APRESENTA\033[m\nSeleção de classes por idade\n')
ano = int(input('Digite sua idade: '))
print('Você tem {}{}{} anos'.format('\033[1;32m', ano, '\033[m'))
if ano < 9:
    print('Para menores de 9 anos: {}MIRIN{}'.format('\033[1;36m', '\033[m'))
elif 9 < ano < 14:
    print('Para menores de 14 anos: {}INFANTIL{}'.format('\033[1;33m', '\033[m'))
elif 14 < ano < 19:
    print('Para menores de 19 anos: {}JUNIOR{}'.format('\033[1;31m', '\033[m'))
elif 19 < ano < 20:
    print('Para menores de 20 anos : {}SÊNIOR{}'.format('\033[1;32m', '\033[m'))
else:
    print('Para maiores de 20 anos: {}MASTER{}'.format('\033[1;34m', '\033[m'))
