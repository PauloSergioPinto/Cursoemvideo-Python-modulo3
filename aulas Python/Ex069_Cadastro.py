maior = homem = mulher = 0
while True:
    print('-'*30)
    print('   CADASTRE UMA PESSOA    ')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    op = str(input('Quer Continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
print('-'*30)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')