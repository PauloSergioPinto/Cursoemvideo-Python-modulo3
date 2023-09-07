print('='* 20)
print('DETECTOR DE PALÍNDROMO')
print('='* 20)
texto = input('Digite uma frase: ').upper()
frase1 = texto.replace(" ", "")
inverso = frase1[::-1]
print('O inverso de {} é {}!'.format(frase1, inverso))
if frase1 == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')