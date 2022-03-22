#Mostrar se pode formar um triângulo e se é equilátero, isósceles ou escaleno
l1 = float(input('Qual é o comprimento do primeiro lado? '))
l2 = float(input('Qual é o comprimento do segundo lado? '))
l3 = float(input('Qual é o comprimento do terceiro lado? '))

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    if l1 == l2 == l3:
        print('É um triângulo equilátero!')
    elif l1 == l2 or l1 == l3:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Não podem formar um triângulo!')