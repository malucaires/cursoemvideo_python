#Pergunte o salário dos funcionários e aumento de 10% para salário maior que 1250 e 15% para valores menores ou iguais
sal = float(input('Qual é o valor do salário? '))
if sal > 1250:
    print('O valor do salário era {:.2f} e com o aumento de 10% será {:.2f}'.format(sal,sal*1.10))
else:
    print('O valor do salário era {:.2f} e com o aumento de 15% será {:.2f}'.format(sal,sal*1.15))