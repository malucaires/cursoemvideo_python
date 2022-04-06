import moedas

p = float(input('Digite o valor: R$ '))
print(f'A metade de R$ {p} é R$ {moedas.metade(p)}.')
print(f'O dobro de R$ {p} é R$ {moedas.dobro(p)}.')
print(f'R$ {p} acrescido em 10% é R$ {moedas.aumentar(p, 10)}.')
print(f'R$ {p} diminuido em 13% é R$ {moedas.diminuir(p, 13)}.')
