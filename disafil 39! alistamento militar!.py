import datetime
data = int(datetime.date.today().year)
print('\033[1;33mALISTAMENTO MILITAR\033[m')
nas = int(input('Digite seu ano de nascimento: '))
idad = data - nas
if idad < 18:
    print('Você ainda \033[1;31mNÂO\033[m tem idade para o alistamento militar.')
elif idad == 18:
    print('Você \033[1;31mDEVE\033[m fazer o alistamento militar este ano.')
else:
    print('Você já \033[1;31mPASSOU {} ANOS\033[m da idade de fazer o alistamento militar.'.format((idad - 18)))
