times = ('Atlético', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Red Bull Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO',
         'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR',
         'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('~='*15)
print(f'Lista de times do Brasileirão: {times}')
print('~='*15)
print(f'Os 5 primeiros sâo: {times[0:5]}')
print('~='*15)
print(f'Os 4 ultimos são: {times[-4:]}')
print('~='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('~='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')