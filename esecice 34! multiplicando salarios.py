salario = int(input('Digite seu salario: R$ '))
if salario <= 1350:
    almento = ((salario / 100) * 15) + salario
    print('Você tera um almento de 15%! passando o salario para {}R$'.format(almento))
if salario >= 15000:
    print('Tu não vai ter almento nâo!')
else:
    almento = ((salario / 100) * 10) + salario
    print('Você tera um almento de 10%! passando o salario para {}R$'.format(almento))
