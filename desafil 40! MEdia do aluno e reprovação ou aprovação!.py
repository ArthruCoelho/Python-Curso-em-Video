print('\033[7mCONSUTOR DE NOTAS DO ALUNO\033[m\ntotal: 10 PONTOS')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('MÉDIA: {}\nSua média foi inferior à 5 pontos: \033[1;31mREPROVADO\033[m'.format(media))
elif 5 <= media <= 6.9:
    print('MÉDIA {}\nSua média foi de 5 à 6.9 pontos: \033[1;33mRECUPERAÇÂO\033[m'.format(media))
else:
    print('MÉDIA {}\nSua média foi maior que 7 pontos: \033[1;32mAPROVADO\033[m'.format(media))
