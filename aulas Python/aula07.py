n1 = int(input('digite um valor '))
n2 = int(input('digite outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} o produto {} e a \ndivisão é {:.3f}'.format(s ,m, d), end='>>>')
print('Divisão inteira é {} e potência é {}'.format(di, e))