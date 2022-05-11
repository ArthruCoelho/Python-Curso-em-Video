distance = int(input('Qual é a distancia da viagem que você ira fazer? em km: '))
if distance <= 200:
    valor = distance / 2
else:
    valor = distance * 0.45
print('Você esta prestes a realizar uma viagem de {}km\n    O valor da viagem é de {} R$'.format(distance, valor))
