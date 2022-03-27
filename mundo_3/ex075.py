#Leia quatro valores pelo teclado, guarde em uma tupla. Mostre qtde de 9, posição primeiro 3 e quais números pares.
valores = ((int(input('Digite um número: '))),
           (int(input('Digite outro número: '))),
           (int(input('Digite mais um número: '))),
           (int(input('Digite o último número: '))))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if valores.count(3) > 0:
    print(f'O número 3 apareceu pela primeira vez na {valores.index(3)+1}ª posição'
          f'.')
else:
    print('O número 3 não apareceu na sequência')
print('Os valores pares que aparecem foram:', end= ' ')
for c in range (0,4):
    if valores[c] %2 == 0:
        print(f'{valores[c]}', end=' ')
print('\nFIM!')
