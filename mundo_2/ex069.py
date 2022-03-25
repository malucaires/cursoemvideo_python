#Leia idade e sexo de várias pessoas
#FALTA WHILE PARA PERGUNTAR S OU N
print('{:=^40}'.format(' INÍCIO DO PROGRAMA '))
cont = 'S'
anos = homens = mulheres = 0
while True:
    print('-'*40)
    print('{:=^40}'.format(' CADASTRE UMA PESSOA '))
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        anos += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    print('-'*40)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {anos}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
