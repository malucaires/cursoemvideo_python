listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15,
            'Estojo', 25, 'Transferidor', 4.20)
print('-'*40)
print('{:^40}'.format('Listagem de Preços'))
print('-'*40)
c = 0
while c < len(listagem):
    print(f'{listagem[c]:.<30} R$ {listagem[c+1]:>6.2f}')
    c += 2
print('-'*40)