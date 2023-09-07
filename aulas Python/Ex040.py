print('Exercicio 40 - média de notas')
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Primeira nota: '))
md = (n1 + n2)/2
if md < 5:
    print('A média da nota1 {} e nota2 {} é {:.2f}. REPROVADO'.format(n1, n2, md))
elif md >= 5 and md < 7:
    print('A média da nota1 {} e nota2 {} é {:.2f}. RECUPERAÇÃO'.format(n1, n2, md))
else:
    print('A média da nota1 {} e nota2 {} é {:.2f}. APROVADO'.format(n1, n2, md))