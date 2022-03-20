#leia um número de 0 a 9999 e mostre cada digito separado
num=int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número é: {}.'.format(num))
print('Milhar do número: {}.'.format(m))
print('Centena do número: {}.'.format(c))
print('Dezena do número: {}.'.format(d))
print('Unidade do número: {}.'.format(u))