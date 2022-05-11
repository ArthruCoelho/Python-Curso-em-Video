number = int(input('Digite um numero: '))
number1 = int(input('Digite outo numero: '))
number2 = int(input('Digite mais um numero: '))
maior = 1
menor = 2
if number < number1 and number < number2:
    menor = number
if number1 < number and number1 < number2:
    menor = number1
if number2 < number and number2 < number1:
    menor = number2
print('O menor valor é {}'.format(menor))
if number > number1 and number > number2:
    maior = number
if number1 > number and number1 > number2:
    maior = number1
if number2 > number and number2 > number1:
    maior = number2
print('O maior valor é {}'.format(maior))
