altura = float(input('Qual sua altura? (m) '))
peso = float(input('Qual seu peso? (Kg) '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está Abaixo do Peso')
elif imc <= 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com o Peso Normal')
elif imc <= 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com SOBREPESO')
elif imc <= 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com OBESIDADE')
else:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com OBESIDADE MORBIDA')