lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar (S/N)')).strip().upper()
    if op == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')