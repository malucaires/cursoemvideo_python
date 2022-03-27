#crie uma tupla, mostrar cada palavra e a quantidade de vogal
palavras = ('Criar', 'Programa', 'Palavra', 'Vogal')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nFIM')