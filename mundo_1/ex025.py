#Leia um nome e diga se a pessoa possui Silva no nome
nome=str(input('Digite o nome: ')).strip()
print('Seu nome tem Silva? {}.'.format('SILVA' in nome.upper()))
