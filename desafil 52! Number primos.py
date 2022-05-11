print('{}NUMEROS PRIMOS{}'.format('\033[7m', '\033[m'))
s = 0
while s != 1:
    s = 0
    print('\nDigite {}1{} para finalizar'.format('\033[1;33m', '\033[m'))
    number = int(input('Digite o numero: '))
    for c in range(1, number + 1):
        if number % c == 0:
            print('{}{}{}'.format('\033[1;32m', c, '\033[m'), end=' ')
            s += number / number
        elif number % c != 0:
            print('{}{}{}'.format('\033[1;31m', c, '\033[m'), end=' ')
    print('\n{}{}{} é dividivel por {}{}{} numeros'.format('\033[1;34m', number, '\033[m', '\033[1;35m', s.__round__(),
                                                           '\033[m'))
    if s == 2:
        print('Por isso {}É UM NUMERO PRIMO{}'.format('\033[1;34m', '\033[m'))
    elif s > 2:
        print('Por isso ele {}NÃO É UM NUMERO PRIMO{}.'.format('\033[1;31m', '\033[m'))
