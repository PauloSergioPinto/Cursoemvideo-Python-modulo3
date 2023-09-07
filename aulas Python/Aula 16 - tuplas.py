lanche = ('Hamuurguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche)

print(sorted(lanche))

for comida in lanche:
    print(f'Eu vu comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print("="*30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(f'Quantas vezes aparece o numero 5: {c.count(5)} vezes')
print(f'Em que posição aparece o numero 2: Posição {c.index(2)}')
print(f'Qual a ultima posição que aparece o numero 2: Posição {c.index(2, 1)}')
