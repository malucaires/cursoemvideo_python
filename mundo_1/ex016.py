#Digitar um número real e retornar apenas a parte inteira
from math import trunc
num=float(input('Digite um numero: '))
print('A parte inteira do número {} é {}'.format(num,(trunc(num))))