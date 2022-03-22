#Leia dois números inteiros, qual é maior, qual é o menor, e igual.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número digitado é maior!')
elif n2 > n1:
    print('O segundo número digitado é maior!')
else:
    print('Os números são iguais!')
