n = total = soma = 0
while True:
    n = int(input('Digite umm número [999 para parar]: '))
    if n == 999:
        break
    total += 1
    soma += n
print('Você digitou {} números e a soma entre eles foi {}.'.format(total, soma))