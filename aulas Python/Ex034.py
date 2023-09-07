salario = float(input('Qual o salário: '))
if salario >= 1250:
    salarioN = (salario * .10) + salario
else:
    salarioN = salario * .15 + salario
print('Seu Salário era R$ {:.2f} e agora é R$ {:.2f}'.format(salario, salarioN))