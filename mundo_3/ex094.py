pessoas = list()
dados = dict()
soma = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')
    if op == 'N':
        break
for p in pessoas:
    for k, v in p.items():
        if k == 'idade':
            soma += v
media = soma / len(pessoas)
print('-=' * 20)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram:', end= ' ')
for p in pessoas:
    for k, v in p.items():
        if v == 'F':
            print(f'{p["nome"]}', end= ' ')
print()
print('- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
print('\n-=ENCERRADO=-')
