lista = []
par = []
impar = []
while True:
    add = int(input('Digite o valor do número: '))
    lista.append(add)
    if add %2 == 0:
        par.append(add)
    else:
        impar.append(add)
    while True:
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('Opção inválida.', end = ' ')
    if op == 'N':
        break
print(f'A lista digitada foi: {lista}')
print(f'Os números pares foram: {par}')
print(f'Os números ímpares foram: {impar}')
