from datetime import date
print('Exercicio 41 - Categoria de Natação')
anoAtual = date.today().year
anoNasc = int(input('Ano de Nascimento: '))
idade = anoAtual - anoNasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
