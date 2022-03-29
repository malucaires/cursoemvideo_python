matriz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]: ')))
print('-='*40)
for i in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[i][c]), end=' ')
    print()
