print('Exercicio 29 - Limite de velocidade')
v = int(input('Qual a sua velocidade? '))
if v > 80:
    multa = float(v - 80) * 7
    print('Você está acima do limite e foi Multado em R$ {:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade')
