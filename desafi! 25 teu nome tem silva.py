name = str(input('Digite seu nome: '))
frase = name.title().strip()
print('O nome tem "Silva"?\n {}'.format('Silva' in frase))
