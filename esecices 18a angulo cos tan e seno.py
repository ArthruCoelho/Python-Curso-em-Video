from math import sin, radians, cos, tan
an = float(input('Digite o ângulo que tu deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
co = cos(radians(an))
ta = tan(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem o TANGENTE de {:.2f}'.format(an, co, an, ta))
