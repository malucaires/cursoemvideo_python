#Leia um número inteiro e informe se é par ou ímpar
num=int(input('Digite um número: '))
if (num%2 == 0):
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar'.format(num))