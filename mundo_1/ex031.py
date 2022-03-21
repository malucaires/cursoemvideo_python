#Pergunte a distância da viagem e calcule 0,5/km para até 200km e 0,45/km para viagens mais longas
km=float(input('Qual é a distância da sua viagem? '))
if (km<200):
    print('A sua viagem irá custar {:.2f}'.format(km*0.5))
else:
    print('A sua viagem irá custar {:.2f}'.format(km*0.45))