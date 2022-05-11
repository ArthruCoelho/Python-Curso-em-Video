name = str(input('Digite teu nome: ')).lower().strip()
silva = str("silva" in name)
print('Seu nome tem "Silva"?\n {}'.format(silva.replace('True', 'tem')))
