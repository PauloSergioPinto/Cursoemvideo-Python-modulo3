n1 = float(input('Digitea primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi Boa! Parabéns!')
else:
    print('Sua média foi ruim. Estude Mais!')
print('*'*20)