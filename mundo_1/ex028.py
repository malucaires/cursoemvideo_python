from random import randint
n1 = randint(0,5)
n2 = int(input('Digite um número entre 0 e 5: '))
print(n1)
if (n1==n2):
    print('Você venceu!')
else:
    print('Você perdeu!')
print('--FIM--')