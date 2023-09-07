def titulo(txt):
    print('-' * 30)
    print(f'{txt :^30}')
    print('-' * 30)


titulo('Aula 20')

#+++++++++++++++++

def soma(a, b):
    s = a + b
    print(f'a soma de {a} e {b} é {s}')


soma(4, 5)

#outra função de soma com varios valores
def soma1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somados os valores {valores} temos {s}')


soma1(4, 5, 6)
soma1(9, 7 ,3, 7 ,2)

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
print('-=' * 20)
print('Função Contador')
contador(2, 5, 7, 9)
contador(0, 4, 7)
contador(8, 9, 39, 9, 2)


def contado(* num1):
    tam = len(num1)
    print(f'Recebi os valores {num1} e são ao todo {tam} números')

print('-=' * 20)
print('Função Contador (outro exemplo)')
contado(2, 5, 7, 9)
contado(0, 4, 7)
contado(8, 9, 39, 9, 2)

print('-=' * 20)
print('Função trabalhando com lista')
print('-=' * 20)

def dobra(lst):
    pos = 0
    while pos< len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)