s = str(input("Qual seu sexo (M/F): ")).strip().upper()[0]
while s not in 'MF':
    s = str(input("Dados inválidos. Por favor, inform seu sexo: (M/F): ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(s))