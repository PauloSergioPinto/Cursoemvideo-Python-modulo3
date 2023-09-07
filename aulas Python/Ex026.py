texto = str(input('Digite uma Frase: ')).upper().strip()
print('A letra "A" aparece {} vezes' .format(texto.count('A')))
print('A letra "A" aparece a 1° vez na posição {}' .format(texto.find('A')+1))
print('A letra "A" aparece a Ultima vez na posição {}' .format(texto.rfind('A')+1))