n = total = soma = 0
n = int(input('Digite umm número [999 para parar]: '))
while n != 999:
    total += 1
    soma += n
    n = int(input('Digite umm número [999 para parar]: '))
print('Cocê digitou {} números e a soma entre eles foi {}.'.format(total, soma))
