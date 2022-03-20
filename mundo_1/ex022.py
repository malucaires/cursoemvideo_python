#Digite o nome completo. Gerar todas maiúsculas, gerar todas minúsculas, quantas letras se considerar espaço e quantas letras primeiro nome
nome=str(input('Digite o seu nome completo: ')).strip()
print('O nome digitado é: {}.'.format(nome))
print('Todas maiúsculas: {}.'.format(nome.upper()))
print('Todas minuscúlas: {}.'.format(nome.lower()))
print('A quantidade de letras sem espaço é: {}.'.format(len(nome.replace(' ',""))))
pnome=nome.split()
print('O primeiro nome é {} e a quantidade de letras é {}'.format(pnome[0],len(pnome[0])))