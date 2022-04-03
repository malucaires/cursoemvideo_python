from random import randint
from time import sleep


def sorteia():
    lista = list(randint(1, 10) for c in range(0, 5))
    return lista


def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma


numeros = sorteia()
soma_par = somaPar(numeros)
print(f'Sorteando 5 valores: ', end='')
for num in numeros:
    print(f'{num}', end=' ')
    sleep(0.5)
print('PRONTO!')
print(f'Somando os valores pares de {numeros} temos {soma_par}')
