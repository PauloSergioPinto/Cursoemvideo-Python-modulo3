print('='* 33)
print('10 TERMOS DE UMA PA usando While')
print('='* 33)
c = 1
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = inicio
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU')