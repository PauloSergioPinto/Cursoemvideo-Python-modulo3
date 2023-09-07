from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
print('Valores sorteados:')
for n in range(1, 5):
    dados[f'jogador{n}'] = randint(1, 6)

for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-' * 30)

#criando uma lista para copiar os valores do dicionário
ranking = list()

#ordenando os valores em ordem do maior para o menor com a ordem que foi sorteado
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')