#Condição de pgto
preco=float(input('Qual é o preço do produto? '))
pgto=int(input('Qual é a forma de pagamento? Digite 1 - À vista dinheiro/cheque; 2 - À vista cartão; 3 - Até 2x no cartão; 4 - 3x ou mais no cartão: '))

if pgto == 1:
    print('O preço do produto é {:.2f} e com o desconto de 10% à vista no dinheiro ou cheque ficará {:.2f}!'.format(preco,preco*0.9))
elif pgto == 2:
    print('O preço do produto é {:.2f} e com o desconto de 5% à vista no cartão ficará por {:.2f}!'.format(preco,preco*0.95))
elif pgto == 3:
    print('O preço do produto é {:.2f}!'.format(preco))
elif pgto == 4:
    print('O preço do produto é {:.2f} e com juros de 20% ficará por {:.2f}!'.format(preco,preco*1.2))
else:
    print('Forma de pagamento inválida!')
print('Obrigada e volte sempre!')