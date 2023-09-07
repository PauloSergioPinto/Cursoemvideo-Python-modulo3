import random
n = 11
palpite = 0
nc = random.randint(0, 10)
n = int(input('Escolhi um numero de 0 a 10. Tente adivinhar! '))
while nc != n:
    n = int(input('Tente Novamente! '))
    palpite += 1
    if nc == n:
        print("Parabéns, voce acertou com {} tentativas".format(palpite))
    else:
        print("Errou")
print("Fim")