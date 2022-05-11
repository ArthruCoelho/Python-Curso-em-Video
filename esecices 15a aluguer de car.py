dias = int(input('Por quantos dias o carro ficou alugado? '))
km = int(input('Foram quantos KM rodados? '))
vd = dias * 60.0
vk = km * 0.15
print('O valor do alugueu é de R${}'.format(vd + vk))
