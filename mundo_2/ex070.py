#nome e preço de vários produtos, pergunta se quer continuar
#mostrar total gasto na compra, quantos produtos custam mais de 1k e qual o nome do produto mais barato
total = mil = qtde = pbarato = 0
print('-' * 40)
print('{:^40}'.format('LOJA CEV!'))
print('-' * 40)
while True:
    nome = str(input('Qual é o nome do produto? '))
    preço = float(input('Qual é o preço do produto? R$ '))
    total += preço
    qtde += 1
    if preço >= 1000:
        mil += 1
    if pbarato > preço or pbarato == 0:
        barato = nome
        pbarato = preço
    op = ' '
    while op not in 'SN':
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if op == 'N':
        break
print(f'O total gasto na compra foi de R${total} em {qtde} produtos.')
print(f'Foram comprados {mil} produtos que custam mais de R$1.000,00.')
print(f'O produto mais barato foi o {barato} que custou R$ {pbarato:.2f}.')
