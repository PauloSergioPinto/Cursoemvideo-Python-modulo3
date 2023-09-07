resp = 'S'
media = cont = 0
valores = []
while resp != 'N':
    n1 = int(input('Digite um número: '))
    media += n1
    cont += 1
    valores.append(n1)
    resp = str(input('Quer continuar? [S/N] ').upper().strip())
ordenada = sorted(valores)
tamanho = len(ordenada)
print('você digitou {} números e a média foi {:.2f}'.format(cont, media/cont))
print('O maior valor foi {} e o menor foi {}'.format(ordenada[tamanho-1], ordenada[0]))