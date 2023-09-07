def notas(*n, sit=False):
    """
    -> Função para analisar notas e siatuções de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando ou não se deve ou não adicionar situação
    :return: dicionário com várias informações sobre a situaão da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resp = notas(5.6, 9.5, 9, 8.5, 6.8)
print(resp)
help(notas)