from time import sleep


def maior(* num):
    tam = len(num)
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    #print(f'{num} Foram informados {tam} valores ao todo')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)