from datetime import date
ano = date.today().year
adulta = 0
menor = 0
for i in range(1, 8):
    dtNasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano - dtNasc
    if idade >= 21:
        adulta += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(adulta))
print('E também tivemos {} pessoas menores de idade'.format(menor))
