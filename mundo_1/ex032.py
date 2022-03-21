#Leia um ano e mostre se é bissexto
from datetime import date
ano=int(input('Qual é o ano? Digite o ano 0 para o ano atual. '))
if ano==0:
    ano=date.today().year
print('O ano selecionado foi o {}.'.format(ano))
if (ano%100 != 0 or ano%400 == 0) and ano%4 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))