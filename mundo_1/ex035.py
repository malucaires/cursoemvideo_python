#Leia o comprimento de 3 retas e determine se pode ser um triângulo
r1=float(input('Qual é o comprimento da primeira reta? '))
r2=float(input('Qual é o comprimento da segunda reta? '))
r3=float(input('Qual é o comprimento da terceira reta? '))
if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
    print('As três retas formam um triângulo')
else:
    print('As três retas não formam um triângulo')