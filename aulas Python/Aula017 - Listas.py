num = [2,5,9,1]
print(num)
num[2] = 3
num.append(7)
num.sort()
num.insert(4, 2)
print(num)
print('removendo o numero 2')
num.remove(2)
num.sort(reverse=True)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'essa lista tem {len(num)} elementos')

for c, v in enumerate(num):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('Fazer uma cópia da lista')
a = [2,3,4,7]
b = a[:]
print(f'Lista A: {a}')
print(f'Lista B: {b}')