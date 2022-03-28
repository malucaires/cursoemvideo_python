lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite o valor: ')))
    while True:
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('Opção inválida.', end = ' ')
    if op == 'N':
        break
for c in range(0, len(lista)):
    if lista[c] %2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
lista.sort()
print('=-'*30)
print(f'Lista completa {lista}')
print(f'Pares: {par}')
print(f'Ímpar: {impar}')