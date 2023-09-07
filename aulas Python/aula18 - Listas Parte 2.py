galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[2][1])
print('=-'*20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

#outro exemplo
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input(('Nome: '))))
    dado.append((int(input('Idade: '))))
    galera.append(dado[:]) #uma copia de dado para galera
    dado.clear()  #apaga lista dado

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')