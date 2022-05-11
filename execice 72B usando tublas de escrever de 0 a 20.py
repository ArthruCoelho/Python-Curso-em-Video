count = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quartoze', 'quinze', 'desseceis',
         'dessecete', 'dezoito', 'dezenove', 'vinte')
while True:
    number = int(input('Digite um numero entre 0 a 20: '))
    if 0 <= number <= 20:
        break
print(f'Você digitou o numero \033[1;31m{count[number]}\033[m!')
