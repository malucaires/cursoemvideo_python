jogador = dict()
gols = list()
jogador['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
qtde_partidas = int(input('Digite a quantidade de partidas: '))
for c in range(0, qtde_partidas):
    gols.append(int(input(f'Digite a quantidade de gols na {c+1} partida: ')))
jogador['qtde_gols'] = gols[:]
jogador['total_gols'] = sum(gols)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["qtde_gols"])} partidas.')
for i, v in enumerate(jogador['qtde_gols']):
    print(f'   => Na partida {i+1}, fez gols {v}.')
print(f'Foi um total de {jogador["total_gols"]}')
