n1 = int(input('Lado 1 do Triangulo: '))
n2 = int(input('Lado 2 do Triangulo: '))
n3 = int(input('Lado 3 do Triangulo: '))
lados = [n1, n2, n3]
ord = sorted(lados)
if (ord[0] + ord[1]) <= ord[2]:
    print('\033[1;30;44mNao e possivel criar um Triangulo com essas medidas {}\033[m'.format(lados))
else:
    print('E possivel criar um Triangulo com as medidas {}'.format(lados))