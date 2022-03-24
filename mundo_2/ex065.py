soma = cont = 0
op = 'S'
while op in 'S':
    n = int(input('Digite um número inteiro: '))
    if cont == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    op = str(input('Você deseja digitar outro número? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Foram digitados {} números, com média de {}, sendo {} o maior número e {} o menor.'.format(cont,media,maior,menor))
