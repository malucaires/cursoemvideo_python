#Leia um número inteiro n e mostre os n primeiros elementos da sequência de Fibonacci
n1 = 0
n2 = 0
n = int(input('Digite a quantidade de elementos da sequência de Fibonacci: '))
c = 0
while c < n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 == 0:
        n1 += 1
    print('{}'.format(n3),end = ' ')
    c += 1
print('\nFIM!')
