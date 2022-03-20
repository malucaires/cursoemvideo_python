#Leia o nome completo e mostre o primeiro e o último nome
nome=str(input('Digite o nome completo: ')).strip().title()
lista=nome.split()
print('O primeiro nome é: {}.'.format(lista[0]))
print('O último nome é: {}.'.format(lista[len(lista)-1]))