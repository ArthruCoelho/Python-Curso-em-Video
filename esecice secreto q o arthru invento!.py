import random
br1 = str(input('O animal numero 1: '))
br2 = str(input('O animal numero 2: '))
br3 = str(input('O animal numero 3: '))
try_ori = [br1, br2, br3]
alectory = random.choice(try_ori)
print("O animal escolhido pela entidae Baur's Reach é o(a) {}!".format(alectory))