print('somar 6 numeros Pares inteiros')
print('='* 20)
cont=0
soma = 0
for i in range(1, 7):
    n = int(input('digite o {} número: '.format(i)))
    if n % 2 == 0:
        soma+= n
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))