#Sortear um de quatro alunos.
from random import choice
a=input('Digite o nome do primeiro aluno: ')
b=input('Digite o nome do segundo aluno: ')
c=input('Digite o nome do terceiro aluno: ')
d=input('Digite o nome do quarto aluno: ')
lista=[a,b,c,d]
e=choice(lista)
print('O aluno escolhido foi o {}'.format(e))