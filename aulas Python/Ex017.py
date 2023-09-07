import math
co = float(input('Entre com o valor do Cateto Oposto: '))
ca = float(input('Entre com o valar do Cateto Adjacente: '))
hipotenusa = math.hypot(co, ca)
print('A hipotenusa de {} e {} é ==> {}' .format(co, ca, hipotenusa))