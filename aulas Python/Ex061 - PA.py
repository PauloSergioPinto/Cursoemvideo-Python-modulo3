print('='* 33)
print('10 TERMOS DE UMA PA usando While')
print('='* 33)
c = 1
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while c < 11:
    print('{}'.format(inicio), end=' -> ')
    inicio += razao
    c += 1
print('ACABOU')