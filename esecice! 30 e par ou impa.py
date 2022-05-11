number = int(input('Digite qualquer numero: '))
number1 = number % 2
if number1 == 1:
    print('{} é um numero IMPA'.format(number))
else:
    print('{} é um numero PAR'.format(number))
