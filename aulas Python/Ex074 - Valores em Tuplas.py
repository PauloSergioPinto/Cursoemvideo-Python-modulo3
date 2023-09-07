import random
c = 0
numeros = []
while c < 5:
    numeros.append(random.randint(0, 10))
    c += 1
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')