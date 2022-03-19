#Leia o angulo e mostre o valor de seno, cosseno e tangente
from math import sin,cos,tan,radians
ang=int(input('Digite o valor do ângulo: '))
print('O valor do seno é {:.2f}'.format(sin(radians(ang))))
print('O valor do cosseno é {:.2f}'.format(cos(radians(ang))))
print('O valor da tangente é {:.2f}'. format(tan(radians(ang))))
