#usando DOCSTRINGS


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')


contador(2, 10, 2)
help(contador)

#parametro opcionais
def somar(a=0, b=0, c=0):
    """
    -> soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return:
    """
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)

#Funções com retorno

def somar1(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar1(3, 2, 5)
r2 = somar1(3, 2)
r3 = somar1(9)

print(f'Os resultados foram {r1}, {r2}, {r3}')



#programa Principal
n = 2
print(f'No programa principal, n vale {n}')


#Fatorial
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a: {fatorial(n)}')


#Retorna true ou false se o número é par
def par(t=0):
    if t % 2 ==0:
        return True
    else:
        return False


num1 = int(input('Digite um número para saber se e par ou impar: '))
if par(num1):
    print('É Par')
else:
    print('Não é par')
