print('Exercicio 37 - Base de conversão')
n1 = int(input('Digite um numero inteiro: '))
op = int(input('Converter para: \n [1] - binário \n [2] - octal \n [3] - hexadecimal \n Sua opção? '))
if op == 1:
    print('o número {} em binário é: {}'.format(n1, bin(n1)[2:]))
elif op == 2:
    print('o número {} em octal é: {}'.format(n1, format(n1, "o")))
else:
    print('o número {} em binário é: {}'.format(n1, format(n1, "x")))