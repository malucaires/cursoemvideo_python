#Leia o primeiro termo e a razao de uma PA e determine os primeiros 10 termos
pt = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão da PA? '))
cont = 1
while cont <= 10:
    termo = pt + (cont - 1) * razao
    print('{}'.format(termo), end= ' ')
    cont += 1
print('\nFIM!')