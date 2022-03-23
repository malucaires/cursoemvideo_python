#Tabuada de 1 a 9
num=int(input('Digite o número: '))
for c in range (1,11):
    print('{:2} x {:2} = {:3}'.format(num,c,num*c))
print('FIM!')