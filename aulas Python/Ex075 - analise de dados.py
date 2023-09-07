c = 1
lista = []
while c < 5:
    n = int(input(f'Digite o {c}° número: '))
    lista.append(n)
    c +=1
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
print(f'O valor 3 apareceu na {lista.index(3)+1}° posição')
print(f'Os valores pares digitados foram ', end='')
for x in lista:
    if x % 2 == 0:
        print(x, end=' ')
