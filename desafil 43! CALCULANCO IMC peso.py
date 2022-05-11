print('{}CALCULADORA DE IMC!{}\n(Indice de Massa Corporal)\n'.format('\033[7m', '\033[m'))
peso = int(input('Digite o seu peso: '))
altura = int(input('Digite a sua altura: ')) / 100
imc = peso / altura ** 2
print('Seu IMC é de {}{}{}'.format('\033[1m', imc.__round__(1), '\033[m'))
if imc < 18.5:
    print('Seu IMC esta abaixo de 18.5\nVocê esta {}ABAIXO DO PESO{}'.format('\033[1;33m', '\033[m'))
elif 18.5 < imc < 25:
    print('Seu IMC esta entre 18.5 à 25\nVocê esta com o {}PESO IDEAL{}'.format('\033[1;32m', '\033[m'))
elif 25 < imc < 30:
    print('Seu IMC esta entre 25 à 30\nVocê esta {}SOBREPESO{}'.format('\033[1;43', '\033[m'))
elif 30 < imc < 40:
    print('Seu IMC esta entre 30 à 40\nVocê esta na {}OBESIDADE{}'.format('\033[1;31', '\033[m'))
elif imc > 40:
    print('Seu IMC esta acima de 40\n Você esta na {}OBESIDADE MÓRBIDA{}'.format('\033[1;35m', '\033[m'))
