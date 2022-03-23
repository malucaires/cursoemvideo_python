#Ler ano de nascimento de 7 pessoas e indicar quantas atingiram a maior idade e quantas não
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range (1, 8):
    nasc=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (nasc + 21) <= atual:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas, {} são maiores e {} são menores'.format(maior,menor))