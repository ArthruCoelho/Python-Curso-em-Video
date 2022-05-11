import math
print('{}ANALIZE DE NOME{}'.format('\033[7m', '\033[m'))
maior = 0
mulhmenores = 0
s = 0
f = 0
namem = '0'
for i in range(1, 5):
    v = 1
    sexo = 'v'
    print('{:20}Pessoa n°{}{:20}'.format('\033[1;32m', i, '\033[m'))
    name = str(input('Digite seu nome: ')).title()
    idad = int(input('Digite sua idade: '))
    f += v
    s += idad
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo (M/F): ')).upper()
    if sexo == 'M':
        if i == 1:
            maior = idad
            namem = name
        elif idad > maior:
            maior = idad
            namem = name
    if sexo == 'F':
        if idad < 20:
            mulhmenores += v
media = s / f
print("""\nA média de idade do grupo é de {}{} anos{}\nO homem mais velho tem {}{} anos{}, e se chama {}{}{}.
Ao todo são {}{}{} melheres com menos de 20 anos""".format('\033[1;35m', media.__round__(1), '\033[m', '\033[1;35m',
                                                           maior, '\033[m', '\033[1;33m', namem, '\033[m', '\033[1;33m',
                                                           mulhmenores, '\033[m'))
