print('Soma dos Numeros impares multplos de 3 de 1 a 500')
soma = 0
contador = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c, end=' ')
            contador += 1
            soma += c
print('\nA soma dos {} valores é {}'.format(contador, soma))