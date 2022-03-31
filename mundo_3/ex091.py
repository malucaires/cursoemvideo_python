from random import randint
from time import sleep
from operator import itemgetter
resultados = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in resultados.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
print(' ==Ranking dos jogadores== ')
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
