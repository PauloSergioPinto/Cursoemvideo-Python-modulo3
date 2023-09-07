print('========== PERSONART ==========')
compras = float(input('Preço das compras: R$ '))
op = int(input('FORMAS DE PAGAMENTO'
           '\n[ 1 ] à vista dinheiro/cheque'
           '\n[ 2 ] à vista cartão'
           '\n[ 3 ] 2x no cartão'
           '\n[ 4 ] 3x ou mais no cartão'
           '\nqual é a opção? '))
if op == 1:
    vista = compras - (compras *.1)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compras, vista))
elif op == 2:
    vista = compras - (compras * .05)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compras, vista))
elif op == 3:
    vista = compras / 2
    print('Sua compra de R$ {:.2f} vai ficar em 2x de R$ {:.2f}.'.format(compras, vista))
elif op == 4:
    parcelas = int(input('Em quantas parcelas? '))
    vista = compras + (compras * .2)
    vlrParcela = vista / parcelas
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} em {} parcelas de R$ {:.2f}'.format(compras, vista, parcelas, vlrParcela))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(compras, compras))