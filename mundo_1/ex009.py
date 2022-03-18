#Leia um número inteiro qualquer e mostre a sua tabuada
i=1
n=int(input('Digite o número:'))
print('-'*13)
while (i<=10):
    print('{:1} x {:2} = {:3}'.format(n,i,n*i))
    i+=1
print('-'*13)