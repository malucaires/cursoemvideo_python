#ler ano de nascimento e indicar categoria
from datetime import date
ano=int(input('Qual é o ano de nascimento? '))
idade=(date.today().year)-ano
if idade<=9:
    print('O atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade<=14:
    print('O atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade<=19:
    print('O atleta tem {} anos e está na categoria JUNIOR'.format(idade))
elif idade<=20:
    print('O atleta tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER'.format(idade))