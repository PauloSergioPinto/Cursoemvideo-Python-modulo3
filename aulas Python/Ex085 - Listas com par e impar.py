lista = [[], []]
#par = list()
#impar = list()
for n in range(1, 8):
    valor = int(input(f'Digite o {n}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
#lista.append(par[:])
#lista.append(impar[:])
print('=-' * 25)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')