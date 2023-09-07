from time import sleep
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for i in range(1, 11):
    print(f'{i}', end=' ')
    sleep(1)
print('fim!')

print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for cont in range(10, -1, -2):
    print(f'{cont}', end=' ')
    sleep(1)
print('Fim!')
print('-=' * 20)



def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        for n in range(i, f, p):
            print(f'{n}', end=' ')
            sleep(1)
        print('FIM!')
    if i > f:
        for n in range(i, f-1, -p):
            print(f'{n}', end=' ')
            sleep(1)
        print('FIM!')


print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('Passo: '))
contagem(i, f, p)