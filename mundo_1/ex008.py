#Leia um valor em metros e converta em centimetros e milímetros
n=float(input('Digite a quantidade em metros:'))
print('A quantidade em metros é {:.2f}, em centrimetros é {:.0f} e em milímetros é {:.0f}'.format(n,n*100,n*1000))