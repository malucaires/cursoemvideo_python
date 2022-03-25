from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
vit = 0
while True:
    comp = randint(0,11)
    jog = int(input('Digite um valor: '))
    par = ' '
    while par not in 'PI':
        par = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    total = comp + jog
    print('-'*40)
    print(f'Você jogou {jog} e o computador {comp}. Total de {total}:',end=" ")
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    print('-'*40)
    if par == 'P' and total % 2 == 0:
        print('Você VENCEU!')
        vit += 1
    elif par == 'I' and total % 2 != 0:
        print('Você VENCEU!')
        vit += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {vit} vez(es).')
