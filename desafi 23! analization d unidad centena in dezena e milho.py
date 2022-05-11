number = input('Digite um numero de 1 a 9999: ')
number1 = number[::4]
number2 = number[1::4]
number3 = number[2::4]
number4 = number[3::4]
print('Milar(es): {}\nCentena(s): {}\nDezena(s): {}\nUnidade(s) {}'.format(number1, number2, number3, number4))
