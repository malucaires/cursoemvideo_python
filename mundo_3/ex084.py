pessoas = []
dados = [] #temporario

while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
    dados.clear()
    while True:
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        print('Opção inválida!', end=' ')
    if op == 'N':
        break
print('-'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()
