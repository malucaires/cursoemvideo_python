def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}mª')


# Programa Principal
print('CONTROLE DE TERRENOS')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
