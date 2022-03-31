aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-'*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
