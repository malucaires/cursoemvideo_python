#Leia uma frase e verifique se é um palíndromo
f1 = str(input('Digite uma frase: ')).strip()
f2 = f1.replace(' ','').upper()
igual = 0
for c in range (0,len(f2)-1):
    if f2[c] != f2[len(f2)-1-c]:
        igual += 1
if igual >= 1:
    print('A frase "{}" não é um palíndromo'.format(f1))
else:
    print('A frase "{}" é um palíndromo'.format(f1))