#Leia a velocidade de um carro se passar de 80KM ele foi multado e a multa custa 7 reais a cada km acima
vel=float(input('Qual é a velocidade do carro? '))
if (vel > 80):
    print('Você foi multado! O valor da multa é {:.2f}'.format((vel-80)*7))
else:
    print('Você não foi multado')