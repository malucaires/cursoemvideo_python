#Pergunte a qtde de km percorrido de um carro alugado e quantidade de dias, custa R$60/dia e R$0,15/Km
dia=int(input('Por quantos dias o carro foi alugado? '))
km=float(input('Quantos kms foram percorridos? '))
valor=km*0.15+dia*60
print('O carro foi alugado por {:.0f} dias, percorreu {:.2f}Km. O preço a pagar é R${:.2f}.'.format(dia,km,(valor)))