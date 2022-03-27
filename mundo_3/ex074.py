#Gerar cinco números aleatórios e colocar em uma tupla
from random import randint
tupla = tuple(randint(0,100) for c in range (0,5))
print(f'Os números sorteados foram {tupla}')
print(f'O maior valor é o {max(tupla)}.')
print(f'O menor valor é o {min(tupla)}.')