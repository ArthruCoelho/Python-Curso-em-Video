a1 = float(input('Digite o segmento: '))
a2 = float(input('Digite o outro segmeno: '))
a3 = float(input('Digite o o ultimo segmento: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Dá para fazer um triangulo')
else:
    print('Não da um triangulo')
