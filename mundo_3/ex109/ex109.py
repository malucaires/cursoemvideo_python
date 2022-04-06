import moedas as m

p = float(input('Digite o valor: R$ '))
print(f'A metade de {m.moeda(p)} é {m.metade(p, True)}.')
print(f'O dobro de {m.moeda(p)} é {m.dobro(p, True)}.')
print(f'{m.moeda(p)} acrescido em 10% é {m.aumentar(p, 10, True)}.')
print(f'{m.moeda(p)} diminuido em 13% é {m.diminuir(p, 13, True)}.')
