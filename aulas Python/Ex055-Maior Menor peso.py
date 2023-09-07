lista = []
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    lista.append(peso)
ordenada = sorted(lista)
print('O maior peso lido foi de {}Kg'.format(ordenada[4]))
print('O menor peso lido foi de {}Kg'.format(ordenada[0]))