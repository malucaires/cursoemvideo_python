#lista decrescente , se o valor 5 apareceu e está ou não na lista
lista = []
while True:
    lista.append(int(input('Digite o valor do número: ')))
    while True:
        op = str(input('Você deseja digitar outro número? [S/N] ')).upper().strip()
        if op in 'SN':
            break
        else:
            print('Opção incorreta...', end = ' ')
    if op == 'N':
        break
print('-='*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
