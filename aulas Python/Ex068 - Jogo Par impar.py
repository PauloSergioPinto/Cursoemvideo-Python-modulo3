from random import randint
cont = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    nc = randint(0, 10)
    n = int(input('Diga um Valor: '))
    op = str(input('Par ou Impar? [P/I]: ')).upper().strip()
    soma = nc + n
    print('-' * 30)
    if op == 'P' and (soma%2) == 0:
        print(f'Você jogou {n} e o computador {nc}. Total de {soma} DEU PAR')
        print('Você venceu')
        cont += 1
        print('Vamos Jogar novamente...')
    elif op == 'I' and (soma%2) != 0:
        print(f'Você jogou {n} e o computador {nc}. Total de {soma} DEU IMPAR')
        print('Você venceu')
        cont += 1
        print('Vamos Jogar novamente...')
    else:
        if op == 'P' and (soma%2) != 0:
            print(f'Você jogou {n} e o computador {nc}. Total de {soma} DEU IMPAR')
        else:
            print(f'Você jogou {n} e o computador {nc}. Total de {soma} DEU PAR')
        break
print('Você PERDEU')
print('=-'*15)
print(f'GAME OVER! você venceu {cont} vez(es)')
