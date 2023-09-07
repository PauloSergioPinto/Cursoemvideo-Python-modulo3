# filme = dict() ou posso usar
filme = {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

print('-=' * 30)

pessoas = {'nome': 'Paulo', 'sexo': 'M', 'idade': 45}
for k ,v in pessoas.items():
    print(f'{k} = {v}')

print('**>>Apagando um item usando del<<**')
del pessoas['sexo']
for k ,v in pessoas.items():
    print(f'{k} = {v}')

print('**>>Trocando um item<<**')
pessoas['nome'] = 'Leandro'
for k ,v in pessoas.items():
    print(f'{k} = {v}')

print('**>>Adicionando um item<<**')
pessoas['peso'] = 78.7
for k ,v in pessoas.items():
    print(f'{k} = {v}')

print('*** Criando um dicionario dentro de uma Lista ***')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()