matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='|')
    print()
print('-='*30)
print(f'A soma dos valores pares é: {pares}')

for l in range(0, 3):
    terceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é : {terceira}')

#print(f'soma dos valores da coluna 3 é : {sum(matriz[1])}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')