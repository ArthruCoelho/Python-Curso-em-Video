print('Emprestimo?\n\033[7;;49mTOMA\033[m')
house = int(input('Digite o valor da casa: R$ '))
sarario = int(input('Digite o seu salario: R$ '))
years = int(input('Em quantos anos pretende pagar o emprestimo? (Apenas numeros) ')) * 12
enprestimo = house / years
tritapucento = (sarario / 100) * 30
if tritapucento >= enprestimo:
    print('\033[1;34mO seu empréstimo foi Aprovado!\033[m')
    print('Ficará \033[1;32mR${}\033[m por més, de um total de \033[1;32R${}\033[m.'.format(enprestimo.__round__(),
                                                                                            house))
else:
    print('\033[1;35mO seu emprestimo não foi aprovado\033[m.\nTalvés na proxima \033[;35m):\033[m')
