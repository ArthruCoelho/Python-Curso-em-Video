frasi = str.strip((input('Digite uma frase: ')))
frase = frasi.lower()
numbers = frase.count('a')
localization = frasi.lower().find('a')
omega = frase.rfind('a')
print('A frase tem {} "a"\nOnde o primeiro esta na {} \nE o ultimo esta em {}'.format(numbers, localization, omega))