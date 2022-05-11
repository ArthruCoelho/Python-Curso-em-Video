print('{}MASCULINO OU FEMININO{}'.format('\033[7m', '\033[m'))
genero = str(input('\nDigite seu sexo (M/F): ')).upper()
while genero != 'M' and genero != 'F':
    genero = str(input('Digite seu sexo (M/F): ')).upper()
print('Ok')
