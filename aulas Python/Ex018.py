import math
angulo = float(input('Qual o ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O Seno do ângulo de {} graus é {:.3f}'.format(angulo, seno))
print('O Coseno do ângulo de {} graus é {:.3f}'.format(angulo, coseno))
print('A Tangente do ângulo de {} graus é {:.3f}'.format(angulo, tangente))