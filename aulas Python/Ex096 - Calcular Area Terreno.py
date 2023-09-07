def area_Terreno(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m²')


print('Controle de Terrenos')
print('-'*21)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area_Terreno(larg, comp)
