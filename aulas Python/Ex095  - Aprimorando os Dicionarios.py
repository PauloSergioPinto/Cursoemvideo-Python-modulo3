jogador = dict()
partidas = list()
time = list()
#jogador['nome'] = str(input('Nome do Jogador: '))
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, qtd):
        partidas.append(int(input(f'    Quantos gols na partida {i+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        op2 = str(input('Quer Continuar? ')).upper()[0]
        if op2 in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N')
    if op2 == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
       print(f'Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {1+1} fez {g} gols.')
    print('-' * 40)
print('<<  VOLTE SEMPRE  >>')