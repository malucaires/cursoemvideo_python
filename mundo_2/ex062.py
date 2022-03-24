#Leia o primeiro termo e a razao de uma PA e determine os primeiros 10 termos
pt = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão da PA? '))
ant = 0
i = 10
total = 0
while i != 0:
    cont = 1
    while cont <= i:
        termo = pt + (cont - 1) * razao + ant
        print('{}'.format(termo), end= ' ')
        cont += 1
        total += 1
    i = int(input('\nVocê deseja mostrar mais quantos termos? '))
    ant = termo
print('\nFIM! Foram mostrados {} números no total.'.format(total))