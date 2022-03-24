#leia um número e mostre o fatorial
from math import factorial
num = int(input('Escolha um número: '))
f = factorial(num)
i = num
print('{}! ='.format(num), end='')
while 1 <= i <= num:
    print(' {}'.format(i), end='')
    print(' x' if i > 1 else ' = ', end='')
    i -= 1
print('{}!'.format(f))