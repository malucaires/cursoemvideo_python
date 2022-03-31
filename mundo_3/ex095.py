dados_jogador = dict()
jogadores = list()
gols = list()
while True:
    dados_jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    qtde_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    for c in range (0, qtde_partidas):
        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    dados_jogador['qtde_gols'] = gols[:]
    dados_jogador['total_gols'] = sum(dados_jogador['qtde_gols'])
    jogadores.append(dados_jogador.copy())
    gols.clear()
    while True:
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('ERRO! Digite S ou N.')
    if op == 'N':
        break
    else:
        print('-'*40)
print('-='*20)
print('| cod', end='')
for i in dados_jogador.keys():
    print(f'|{str(i):<10}', end='')
print()
print('-'*40)
for i, j in enumerate(jogadores):
    print(f'|{i:^4}|', end='')
    for d in j.values():
        print(f'{str(d):<10}|', end='')
    print()
print('-'*40)
while True:
    op = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if 0 <= op < len(jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[op]["nome"]}:')
        for i, v in enumerate(jogadores[op]['qtde_gols']):
            print(f'   No jogo {i} fez {v} gols.')
    elif op == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com o código {op}')
print('VOLTE SEMPRE!')
