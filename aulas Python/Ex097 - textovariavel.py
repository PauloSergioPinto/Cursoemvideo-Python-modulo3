def titulo(txt):
    t = len(txt)+4
    print('~' * t)
    print(f'{txt :^{t}}')
    print('~' * t)


titulo('Ola')
titulo('Paulo Sergio')
titulo('Curs de Python no YouTube')