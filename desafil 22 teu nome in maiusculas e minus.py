name = input('Digite o teu nome: ')
print('Teu nome em MAIUSCULAS fica: {}'.format(name.upper()))
print('Teu nome em minusculas fica: {}'.format(name.lower()))
numeros = int(len(name.strip()))
print('Seu nome tem {} caracteres '.format(numeros))
dividido = name.strip().split()
print('O seu primeiro nome tem {} caracteres'.format(len(dividido[0])))

