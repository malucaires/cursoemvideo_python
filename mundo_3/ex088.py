from random import randint
from time import sleep
jogos = []
print('-'*35)
print('{:^35}'.format('JOGA NA MEGA SENA'))
print('-'*35)
qtde = int(input('Quantos jogos você quer jogar? '))
for c in range(0, qtde):
    jogos.append(list(randint(1, 61) for i in range(0, 6)))
print(f'-=-=-=-=- SORTEANDO {qtde} JOGOS -=-=-=-=-')
for c in range(0, qtde):
    jogos[c].sort()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print(f'-=-=-=-=-=- BOA SORTE! -=-=-=-=-=-')