print('{}MAIOR E MENOR PESO DA SEQUENCIA{}'.format('\033[7m', '\033[m'))
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso foi de {}{}Kg{}\nO menor peso foi {}{}Kg{}'.format('\033[1;35m', maior, '\033[m', '\033[1;35m',
                                                                         menor, '\033[m'))
