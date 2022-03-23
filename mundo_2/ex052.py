#Leia um número inteiro e diga se é um número primo:
num = int(input('Digite um número inteiro: '))
cont = 0
for c in range (1,num+1):
    if num % c == 0:
        print('\33[33m{}'.format(c), end=' ')
        cont += 1
    else:
        print('\33[31m{}'.format(c), end=' ')
print('\n\033mO número {} pode ser dividido {} vezes.'.format(num,cont))
if cont <= 2:
    print('Logo ele É PRIMO!')
else:
    print('Logo ele NÃO É PRIMO!')
