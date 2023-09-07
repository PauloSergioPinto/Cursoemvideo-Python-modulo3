listaNum = []
while True:
    num = int(input('Digite um valor: '))
    if num not in listaNum:
        listaNum.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar (S/N)')).strip().upper()
    if op == 'N':
        break
print(f'Você adicionou os valores {sorted(listaNum)}')
