print('{}FINALIZANDO COMPRA{}\n'.format('\033[7m', '\033[m'))
valor = int(input('Digite o valor do prodto: R$ '))
print('\nBOLETO = BL\nCARTÃO = CT')
meio = str(input('Digite a sigla do meio de pagamento: ')).upper()
if meio == 'BL':
    desbl = (valor / 100) * 10
    valorbl = valor - desbl
    print('\nMeio de pagamento: {}BOLETO{}\nValor com 10% de descoto: {}R${}{}\nVocê está economizando {}R${}{}'
          .format('\033[1;34m', '\033[m', '\033[1;35m', valorbl.__round__(), '\033[m', '\033[1;35m', desbl.__round__(),
                  '\033[m'))
elif meio == 'CT':
    print('\nNo CARTÂO em até 12 vezes!')
    meioct = int(input('Deseja pagar em quantas vezes? '))
    if meioct == 1:
        desct1 = (valor / 100) * 5
        print("""Meio de pagamento: {}À Vista{} no {}CARTÂO{}\nValor com 5% de descoto: {}R${}{}\n
              Você está ecomomizando: {}R${}{}"""
              .format('\033[1;35m', '\033[m', '\033[1;34m', '\033[m', '\033[1;35m', valor - desct1.__round__(),
                      '\033[m', '\033[1;35m', desct1.__round__(), '\033[m'))
    elif meioct == 2:
        print('Meio de pagamento: {}{}x{} no {}CARTÂO{}\nValor total: {}R${}{}\nValor das parcelas: {}R${}{}'
              .format('\033[1;35m', meioct, '\033[m', '\033[1;34m', '\033[m', '\033[1;35m', valor.__round__(), '\033[m',
                      '\033[1;35m', valor / meioct.__round__(), '\033[m'))
    elif 2 < meioct <= 12:
        jusct3 = (valor / 100) * 20
        print("""Meio de pagamento: {}{}x{} no {}CARTÂO{}\nValor total: {}R${}{}\nAcrecimo pelo juros: {}R${}{}
        \nValor das parcelas: {}R${}{}"""
              .format('\033[1;35m', meioct, '\033[m', '\033[1;34m', '\033[m', '\033[1;35m', valor + jusct3.__round__(),
                      '\033[m', '\033[1;31m', jusct3.__round__(), '\033[m', '\033[1;35m',
                      (valor + jusct3) / meioct.__round__(), '\033[m'))
    else:
        print('\n{}   {}x{} {}Não esta dentro da quantidade de vezes{}'
              .format('\033[1;35m', meioct, '\033[m', '\033[7;31m', '\033[m'))
else:
    print('\n{}    {}{} {}Não é uma  igla de meio de pagamento{}'
          .format('\033[1;35m', meio, '\033[m', '\033[7;31m', '\033[m'))
