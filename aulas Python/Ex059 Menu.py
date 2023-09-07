n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
op = 0
while op != 5:
    op = int(input("Escolha uma opção \n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos numeros\n[5] - Sair do programa\n op =>  "))
    if op == 1:
        print("A soma de {} e {} é {}".format(n1, n2, n1+n2))
    if op == 2:
        print("A Multiplicação de {} e {} é {}".format(n1, n2, n1 * n2))
    if op == 3:
        if n1 > n2:
            print("O maior valor entre {} e {} é {}".format(n1, n2, n1))
        else:
            print("O maior valor entre {} e {} é {}".format(n1, n2, n2))
    if op == 4:
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input("Digite outro novo valor: "))
print("****  FIM  ****")