#Leia vários números inteiros, parar qdo 999. Mostre qtos números digitados e qual a soma
soma = cont = n = 0
while n != 999:
    n = int(input('Digite um número ou digite 999 para parar o programa: '))
    if n != 999:
        soma += n
        cont += 1
print('Foram digitados {} números e a soma entre eles foi {}.'.format(cont,soma))
