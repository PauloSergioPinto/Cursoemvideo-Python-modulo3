n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
lista = [n1, n2, n3]
ordenada = sorted(lista)
print(lista)
print('O Menor numero é {} e o Maior numero é {}'.format(ordenada[0], ordenada[2]))