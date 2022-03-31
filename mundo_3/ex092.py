from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Digite o nome: ')).strip()
ano = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = date.today().year - ano
pessoa['ctps'] = int(input('Digite o número da CTPS: [Digite 0 quando não existente] '))
if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salário'] = float(input('Digite o valor do salário: '))
    pessoa['idade_aposentadoria'] = pessoa['ano_contratacao'] - ano + 35
print('-='*20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
