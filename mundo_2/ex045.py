#Pedra, papel e tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('\33[1;34m','-'*8,'PEDRA, PAPEL E TESOURA!','-'*8)
print('''\33[0;0mVamos jogar!
Suas opções são:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
jogador = int(input('Escolha a opção: '))
computador = randint(0,2)
print('Você jogou: {}.'.format(itens[jogador]))
print('O computador jogou: {}.'.format(itens[computador]))
if jogador == 0 or jogador == 1 or jogador == 2:
    if jogador == computador:
        vencedor = 'O jogo terminou empatado!'
    elif jogador == 0 and computador == 1:
        vencedor = 'Eu ganhei o jogo!'
    elif jogador == 0 and computador == 2:
        vencedor = 'Você ganhou o jogo!'
    elif jogador == 1 and computador == 0:
        vencedor = 'Você ganhou o jogo!'
    elif jogador == 1 and computador == 2:
        vencedor = 'Eu ganhei o jogo!'
    elif jogador == 2 and computador == 0:
        vencedor = 'Eu ganhei o jogo!'
    elif jogador == 2 and computador == 1:
        vencedor = 'Você ganhou o jogo!'

    print('{}'.format(vencedor))
else:
    print('\33[2;31mVocê digitou um número inválido. Jogo encerrado!')