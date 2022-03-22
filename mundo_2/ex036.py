#Aprovar financiamento de casa (ler valor da casa, salário e em quantos anos vai pagar)
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado
casa=float(input('Qual é o valor da casa? R$'))
salario=float(input('Qual é o seu salário? R$'))
anos=int(input('Em quantos anos você pagará o financiamento? '))
meses=anos*12
if (casa/meses)<=0.3*salario:
    print('O empréstimo foi CONCEDIDO. Serão {} parcelas de {:.2f} durante {} anos.'.format(meses,casa/meses,anos))
else:
    print('O empréstimo foi NEGADO!')