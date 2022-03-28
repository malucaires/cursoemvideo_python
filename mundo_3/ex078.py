num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posíção {c}: ')))
print('=-'*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi o {max(num)} na posição', end= ' ')
for c in range (0, 5):
    if num[c] == max(num):
        print(f'{c} ...', end= '')
print(f'\nO menor valor digitado foi o {min(num)} na posição', end= ' ')
for c in range (0, 5):
    if num[c] == min(num):
        print(f'{c} ...', end= '')
print('\nFIM')
