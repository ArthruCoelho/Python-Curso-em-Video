from random import shuffle
print('O professor quer sortear uma ordem de alunos!')
al1 = str(input('Digite o nome do aluno 1: '))
al2 = str(input('Digite o nome do aluno 2: '))
al3 = str(input('Digite o nome do aluno 3: '))
al4 = str(input('Digite o nome do aluno 4: '))
list_al = [al1, al2, al3, al4]
shuffle(list_al)
print('A ordem escolhida pela entidade guiadora é {}'.format(list_al))