from datetime import date
print('Ano Bissexto')
ano = int(input('Esse Ano e Bissexto? Coloque 0 para analisar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} e Bissexto'.format(ano))
else:
    print('O ano de {} nao e Bissexto'.format(ano))