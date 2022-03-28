#ordenar sem sort()
num = []
for c in range(0, 5):
    add = int(input('Digite um valor: '))
    if c == 0 or add > num[c-1]:
        num.append(add)
        print('Adicionado ao final da lista. ')
    else:
        cont = 0
        while cont <= len(num):
            if add <= num[cont]:
                num.insert(cont,add)
                break
            cont+=1
        print(f'Adicionado na posição {cont} da lista')
print(f'Os valores digitados foram: {num}')