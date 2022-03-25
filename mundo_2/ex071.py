#caixa eletrônico
print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
valor = int(input('Quanto você deseja sacar? R$ '))
montante = valor
ced = 50
qtde = 0
while True:
    while montante >= ced:
        montante -= ced
        qtde += 1
    print(f'Total de {qtde} cédulas de R$ {ced}')
    qtde = 0
    if montante >= 20:
        ced = 20
    elif montante >= 10:
        ced = 10
    elif montante >= 1:
        ced = 1
    else:
        break
print('='*40)
print('Volte sempre!')
