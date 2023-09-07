print('=' * 30)
a = int(input('Qual a altura? '))
l = int(input('Qual a largura? '))
area = (a * l)
tinta = area / 2
print('Para pintar a parede de {} m² \n >>> vai ser preciso de {} litros de tinta' .format(area, tinta))