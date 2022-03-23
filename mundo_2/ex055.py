#Leia o peso de cinco pessoas e mostre o maior e o menor
for c in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi {}Kg e o maior foi {}Kg'.format(menor,maior))