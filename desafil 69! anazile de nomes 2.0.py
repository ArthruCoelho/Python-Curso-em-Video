print('{}ANALIZE DE NOME{}'.format('\033[7m', '\033[m'))
maior = 0
mulhmenores = 0
s = 0
f = 0
count = 0
counthomi = 0
countmaior = 0
while True:
    count += 1
    v = 1
    sexo = 'v'
    print('{:20}Pessoa n°{}{:20}'.format('\033[1;32m', count, '\033[m'))
    idad = int(input('Digite sua idade: '))
    f += v
    s += idad
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu sexo (M/F): ')).upper()
    if sexo == 'M':
        counthomi += 1
    if sexo == 'F':
        if idad < 20:
            mulhmenores += v
    if idad >= 18:
        countmaior += 1
    perg = str(input('Que continuar [S/N]: ')).upper()
    if perg == 'N':
        break
media = s / f
print("""\nNo total são {}{}{} pessoas maiores de 18 anos\nTem {}{}{} homen(s) cadastrado(s)
Ao todo são {}{}{} melheres com menos de 20 anos""".format('\033[1;35m', countmaior, '\033[m', '\033[1;35m',
                                                           counthomi, '\033[m', '\033[1;33m',
                                                           mulhmenores, '\033[m'))