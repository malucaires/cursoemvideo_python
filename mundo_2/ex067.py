#Tabuada de vários números - pare quando negativo
print('-' * 40)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*20)
    for c in range (1,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 40)
print('-' * 40)
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')