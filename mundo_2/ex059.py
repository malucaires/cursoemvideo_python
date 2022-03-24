#Leia 2 valores e mostre o menor e dê opções de cálculo
op = 0
while op != 5:
    op = 0
    n1 = int(input('Qual o primeiro número? '))
    n2 = int(input('Qual o segundo número? '))
    while op != 4 and op != 5:
        print('''Suas opções são: 
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
        op = int(input('Escolha uma opção: '))
        if op == 1:
            print('A soma de {} e {} é {}.'.format(n1,n2,n1 + n2))
        elif op == 2:
            print('A multiplicação de {} e {} é {}.'.format(n1,n2,n1 * n2))
        elif op == 3:
            if n1 > n2:
                print('Entre {} e {}, o maior é o {}.'.format(n1,n2,n1))
            elif n2 > n1:
                print('Entre {} e {}, o maior é o {}.'.format(n2,n1,n2))
            else:
                print('Os números são iguais')
        elif op == 4:
            print('Digite novamente os números!')
        elif op != 5:
            print('Você digitou uma opção inválida. Tente novamente')
print('FIM!')