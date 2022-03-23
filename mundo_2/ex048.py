#Calcular a soma entre todos os números ímpares e múltiplos de 3 de 1 até 500.
s=0
i=0
for c in range (1,501,2):
    if c%3 == 0:
        s += c
        i += 1
print('A soma de todos os números ímpares e múltiplos de 3 de 1 a 500 é: {}. São {} números no total'.format(s,i))
