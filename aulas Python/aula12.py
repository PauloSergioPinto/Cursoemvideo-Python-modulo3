nome = str(input('Qual seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Jose':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana, Ivani, Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))