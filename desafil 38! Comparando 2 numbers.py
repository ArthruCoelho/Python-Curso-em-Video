print('\033[1;33mComparando 2 NUMEROS!\033[m')
n1 = int(input('Digite o primeiro nummero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O \033[1;31mPRIMEIRO NUMERO\033[m é \033[1;31mMAIOR\033[m')
elif n2 > n1:
    print('O \033[1;31mSEGUNDO NUMERO\033[m é o \033[1;31mMAIOR\033[m')
else:
    print('Os dois Numeros são \033[1;31mIGUAIS\033[m')
