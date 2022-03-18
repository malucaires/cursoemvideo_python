#Leia o preço e o novo valor com desconto de 5%
p=float(input('Digite o preço do produto: R$'))
print('O preço do produto era R${:.2f} e com desconto de 5% é R${:.2f}'.format(p,(p*0.95)))