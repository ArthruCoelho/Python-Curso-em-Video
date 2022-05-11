from random import choice

lim = '\033[m'
c = {'verm': '\033[1;31m', 'verd': '\033[1;32m', 'amare': '\033[1;33m', 'azu': '\033[1;34m',
     'roxo': '\033[1;35m', 'ciano': '\033[1;36m', 'cinza': '\033[1;37m'}
ca = [c['verm'], c['verd'], c['amare'], c['azu'], c['roxo'], c['ciano']]
number = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite mais um numero: ')),
          int(input('Digite o ùtimo numero: ')))
numbersnone = 0
numberpar = 0
for count in range(0, len(number)):
    if number[count] == 9:
        numbersnone += 1
    if number[count] % 2 == 0:
        numberpar += 1
print(f'As raninhas do didio')
print(f'Foram digitados {choice(ca)}{numbersnone}{lim} numeros nove.')
if 3 in number:
    print(f'O valor 3 foi digitado na posição : {choice(ca)}{number.index(3) + 1}{lim}')
else:
    print('Não tem o numero 3')
count = 0
print(f'Foram digitados {choice(ca)}{numberpar}{lim} numeros pares', end=' ')
if numberpar == 0:
    print('Não tem nenhum numero pares.')
