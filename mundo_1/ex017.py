#Calcular valor da hipotenusa
from math import hypot
cta=float(input('Digite o comprimento do cateto adjacente: '))
ctb=float(input('Digite o comprimento do cateto oposto: '))
hip=hypot(cta,ctb)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))