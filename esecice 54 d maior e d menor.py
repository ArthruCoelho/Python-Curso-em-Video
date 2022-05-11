import datetime
data = int(datetime.date.today().year)
print('{}VAMOS VERIFICAR UMA IDADES!{}'.format('\033[7m', '\033[m'))
s = 0
f = 0
for c in range(1, 8):
    yeas = data - int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if yeas <= 18:
        s += 1
    elif yeas > 18:
        f += 1
print('\nTem {}{}{} pessoas maiores de idade.\nE tem {}{}{} pessoas menores de idade.'.format('\033[1;35m', f, '\033[m', '\033[1;35m', s, '\033[m'))
