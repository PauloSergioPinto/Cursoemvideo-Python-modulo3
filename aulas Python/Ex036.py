print('Exercicio 36 - Emprestimo Bancário')
vlrcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Vai pagar em quantos anos? '))
vlr_prestacao = vlrcasa / (anos * 12)
if vlr_prestacao <= salario * .3:
    print('A prestação da casa para pagar em {} anos é R$ {:.2f}'.format(anos, vlr_prestacao))
else:
    print('Empréstimo negado!')
print('**** FIM  ****')