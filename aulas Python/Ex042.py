n1 = int(input('Lado 1 do Triangulo: '))
n2 = int(input('Lado 2 do Triangulo: '))
n3 = int(input('Lado 3 do Triangulo: '))
lados = [n1, n2, n3]
ord = sorted(lados)
if (ord[0] + ord[1]) <= ord[2]:
    print('Nao e possivel criar um Triangulo com essas medidas {}'.format(lados))
else:
    print('E possivel criar um Triangulo com as medidas {}'.format(lados))
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    if n1 != n2 != n3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
