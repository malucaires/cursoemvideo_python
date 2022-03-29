matriz = [[], [], []]
soma_pares = soma_tcoluna = maior_valor = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]: ')))
        if matriz[i][c] % 2 == 0:
            soma_pares += matriz[i][c]
        if c == 2:
            soma_tcoluna += matriz[i][c]
        if i == 1:
            if matriz[i][c] > maior_valor:
                maior_valor = matriz[i][c]
print('-='*20)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end=' ')
    print('\n')
print('-='*20)
print(f'A soma de todos os números pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_tcoluna}.')
print(f'O maior valor da segunda linha é {maior_valor}.')
