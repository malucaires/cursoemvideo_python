#Ler o primeiro termo e a ração de uma PA. No final mostre os 10 primeiros termos
ptermo=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da RA: '))
for c in range (1,11):
    print('{}'.format(ptermo+(c-1)*razao), end=' -> ')
print('FIM!')