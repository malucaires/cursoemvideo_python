import moedas

p = float(input('Digite o valor: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}.')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}.')
print(f'{moedas.moeda(p)} acrescido em 10% é {moedas.moeda(moedas.aumentar(p, 10))}.')
print(f'{moedas.moeda(p)} diminuido em 13% é {moedas.moeda(moedas.diminuir(p, 13))}.')
