#Leia vários números int, pare quando 999, mostre quantidade e soma
s = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} números é {s}!')