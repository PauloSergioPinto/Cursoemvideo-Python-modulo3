import random
nc = random.randint(0, 5)
n = int(input('Escolhi um numero de 0 a 5. Tente adivinhar! '))
if nc == n:
    print('Parabens, você acertou!´')
else:
    print('Que pena, você errou! Escolhi o numero {}'.format(nc))