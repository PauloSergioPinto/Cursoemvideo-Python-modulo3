print('Exercício 31 - Valor da viagem')
print('*'*30)
d = int(input('Qual a distância da Viagem (Km)? '))
if d <= 200:
    valor = float(d * .45)
    print('O valor da passagem é R$ {:.2f}'.format(valor))
else:
    valor = float(d * .50)
    print('O valor da passagem é R$ {:.2f}'.format(valor))