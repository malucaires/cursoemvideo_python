#Peça o sexo até que seja um sexo válido F/M
sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]
print('A informação foi registrada com sucesso!')