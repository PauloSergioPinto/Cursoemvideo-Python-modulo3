print('='* 20)
print('10 TERMOS DE UMA PA')
print('='* 20)
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print('{}'.format(inicio), end=' -> ')
    inicio += razao
print('ACABOU')
