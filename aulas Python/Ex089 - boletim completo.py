ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar (S/N)? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":8>}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


#while True:
    #nome = str(input('Nome: '))
    #n1 = float(input('Nota1: '))
    #n2 = float(input('Nota2: '))
    #aluno.append(nome)
    #aluno.append(n1)
    #aluno.append(n2)
    #lista.append(aluno[:])
    #aluno.clear()
    #op = ' '
    #while op not in 'SN':
        #op = str(input('Quer continuar (S/N)')).strip().upper()
    #if op == 'N':
        #break
#print('-=' * 30)
#for i, l in enumerate(lista):
    #print(f'{i+1} {l}')
