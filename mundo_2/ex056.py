#Leia o nome idade e sexo de 4 pessoas. Resposta: média da idade do grupo, nome do homem mais velho, qts mulheres tem menos de 20 anos
soma = 0
idadeh = 0
mulher20 = 0
for c in range (1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(c))).strip()
    soma += idade
    if sexo in 'Ff' and idade <20:
        mulher20 = mulher20 + 1
    if sexo in 'Mm' and idade > idadeh:
        idadeh = idade
        homem = nome
media = soma / 4
print('A média de idade do grupo é {:.2f}.'.format(media))
print('O homem mais velho é {} com {} anos.'.format(homem,idadeh))
print('São {} mulheres com menos de 20 anos.'.format(mulher20))

