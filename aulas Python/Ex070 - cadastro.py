cont = total = totmil = 0
menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$ '))
    total += valor
    cont += 1
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menor = valor
        barato = produto
    if valor < menor:
        menor = valor
        barato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer Continuar? ')).upper().strip()
    if op == 'N':
        break
print(f'O total da compra foi R$ {total}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
