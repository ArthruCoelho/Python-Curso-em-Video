velocidade = int(input('Qual foi a velocidade do seu carro? '))
if velocidade <= 80:
    print('Tenha um ôtimo dia!')
else:
    velocidade1 = velocidade - 80
    multa = velocidade1 * 5
    print('Velocidade acima de 80km/h, você tem que pagar uma multa de {}R$!'.format(multa))
