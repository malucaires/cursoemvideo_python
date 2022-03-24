#Pensar um número entre 0 e 10. Jogador adivinhar até acertar e indicar qtde de palpites
from random import randint
comp = randint(0, 10)
cont = 0
print('Vamos jogar! Estou pensando em um número...')
jog=int(input('Adivinhe o número que pensei entre 0 e 10: '))
while comp != jog:
    if jog < comp:
        jog=int(input('Mais... Tente novamente. Qual é o seu palpite? '))
    elif jog > comp:
        jog=int(input('Menos... Tente novamente. Qual é o seu palpite? '))
    cont += 1
print('Você acertou o número! Foram necessárias \33[34m{}\033[m tentativas.'.format(cont))
