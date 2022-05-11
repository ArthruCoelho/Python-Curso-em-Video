print('{}PALÍNDROMO!{}'.format('\033[7m', '\033[m'))
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase ínversa é {}{}{}\n'.format('\033[1;35m', inverso, '\033[m'))
if inverso == junto:
    print('Por tanto é um {}PALÍNDROMO{}!'.format('\033[1;33m', '\033[m'))
else:
    print('Por tanto {}NÃO É UM PALÍNDROMO{}!'.format('\033[1;31m', '\033[m'))
