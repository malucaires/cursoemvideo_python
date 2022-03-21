#Leia três números e encontre o maior e o menor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n2
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1
print('Entre os números {}, {} e {}, o maior número é o {} e o menor é o {}'.format(n1,n2,n3,maior,menor))