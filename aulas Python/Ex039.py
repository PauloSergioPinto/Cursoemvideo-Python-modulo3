from datetime import date
print('Exercicio 39 - Alistamento Militar')
ano = int(input('Qual o ano de seu nascimento? '))
anoAtual = date.today().year
idade = anoAtual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoAtual))
if idade == 18:
    print('Este ano você deve se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não têm 18 anos. Ainda faltam {} para o alistamento'.format(saldo))
    ano = anoAtual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se Alistado há {} anos'.format(saldo))
    ano = anoAtual - saldo
    print('Seu alistamento foi em {}'.format(ano))