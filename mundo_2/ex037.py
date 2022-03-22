#Leia um número inteiro e converta 1-binário, 2-octal, 3-hexadecimal
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para binário é {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para octal é {}.'.format(num,oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')