num = []
while True:
    add = (int(input('Digite um número: ')))
    if add not in num:
        num.append(add)
        print(f'O valor {add} foi adicionado à lista!')
    else:
        print(f'O valor {add} já existe e não foi adicionado à lista!')
    while True:
        op = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('Opção inválida.', end=' ')
    if op == 'N':
        break
num.sort()
print('-='*30)
print(f'Você digitou os números {num}.')