from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(p)
    print(f'-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}', end=' ')
            inicio += passo
            sleep(0.5)
        print('FIM!')
    else:
        while inicio >= fim:
            print(f'{inicio}', end=' ')
            inicio -= passo
            sleep(0.5)
        print('FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
