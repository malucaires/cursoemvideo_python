#Leia o ano de nascimento e informe se (ainda vai se alistar, se é hora de se alistar ou se passou do prazo. Mostrar dif de anos.
from datetime import date
nasc = int(input('Qual é o seu ano de nascimento? '))
alist = nasc+18
atual = date.today().year
idade=atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if alist > atual:
    print('Ainda faltam {} anos para seu alistamento'.format(alist-atual))
    print('Seu alistamento será em {}.'.format(alis))
elif alist == atual:
    print('Você deve se alistar esse ano!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(atual-alist))
    print('Seu alistamento foi em {}.'.format(alist))

