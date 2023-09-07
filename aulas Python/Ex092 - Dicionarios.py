from datetime import date
anoAtual = date.today().year
dados = dict()
dados['nome'] = str(input('Nome: '))
idade = int(input('Ano de Nascimento: '))
dados['idade'] = anoAtual - idade
dados['ctps'] = int(input('Carteira de Trabalho ( 0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    tempoRegistro = dados['contratação'] - idade
print('=*' * 30)
print(dados)
print(f'Nome tem valor {dados["nome"]}')
print(f'Idade tem valor {dados["idade"]}')
if dados['ctps'] != 0:
    print(f'CTPS tem o valor {dados["ctps"]}')
    print(f'Contratação tem o valor {dados["contratação"]}')
    print(f'Salário tem o valor R$ {dados["salário"]}')
    print(f'Aposentadoria tem o valor {tempoRegistro + 35}')

