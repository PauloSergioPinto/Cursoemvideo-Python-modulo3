print('=' * 30)
n1 = float(input('Qual o preço do produto? '))
desconto = n1 * .05
np = n1 - desconto
print('O produto de R$ {} com 5% de desconto está R$ {}' .format(n1, np))