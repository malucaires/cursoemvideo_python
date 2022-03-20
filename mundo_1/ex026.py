#Leia uma frase e mostre quantas vezes aparece a letra A, em que posição o primeiro A aparece, em qual posição ela aparece a última vez

frase=str(input('Digite uma frase: ')).strip().upper()
print('A quantidade de vezes que A aparece é: {}.'.format(frase.count('A')))
print('A primeira posição em que A aparece é: {}.'.format(frase.find('A')+1))
print('A última posição em que A aparece é: {}.'.format(frase.rfind('A')+1))