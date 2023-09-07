extenso = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
op = int(input(f'Digite um número entre 0 e 20: '))
while op < 0 or op > 20:
    op = int(input(f'Tente Novamente. Digite um número entre 0 e 20: '))
if op >= 0 or op <= 20:
        print(f'você digitou o número {extenso[op]}')
print('FIM')