def notas(*nota, sit = False):
    """
    Função para analisar as notas de um aluno
    :param nota: uma ou mais notas dos alunos
    :param sit: (opcional) indica situação do aluno
    :return: retorna dicionario com a quantidade de notas, maior, menor, média e situação quando solicitado
    """
    resp = dict()
    resp['total'] = len(nota)
    resp['maior'] = max(nota)
    resp['menor'] = min(nota)
    resp['media'] = sum(nota)/len(nota)
    if sit == True:
        if media >= 7:
            resp['situação'] = 'BOA'
        elif media >= 5:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
    return resp


#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=False)
print(resp)
