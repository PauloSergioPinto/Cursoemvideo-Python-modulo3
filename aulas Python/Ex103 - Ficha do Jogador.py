def jogador(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato')


#Programa Principal
n = str(input(f'Nome do Jogador: '))
g = str(input(f'Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gols=g)
else:
    jogador(n, g)
