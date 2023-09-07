print('=' * 30)
n1 = int(input('Qual a tabuada '))
print('=' * 15)
print('TABUADA DO {}'.format(n1))
print('=' * 15)
for i in range(11):
    print('{} * {} = {}' .format(n1, i, n1*i))