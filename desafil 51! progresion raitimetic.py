print('{}PROGREÇÂO ARITMÉTICA 10 TERMOS{}'.format('\033[7m', '\033[m'))
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = pri + (11 - 1) * raz
for c in range(pri, decimo, raz):
    print('{}{}{}'.format('\033[1;35m', c, '\033[m'), end=' → ')
print('FIM')
