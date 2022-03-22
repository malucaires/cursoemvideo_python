#média de duas notas. 5 reprovado, 5-6,9 recuperação, 7 aprovado
n1 = float(input('Qual é a primeira nota? '))
n2 = float(input('Qual é a segunda nota? '))
media = (n1 + n2) / 2
if media < 5:
    print('A média do aluno foi {:.2}. O aluno foi REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('A média do aluno foi {:.2f}. O aluno está em RECUPERAÇÃO!'.format(media))
else:
    print('A média do aluno foi {:.2f}. O aluno foi APROVADO!'.format(media))