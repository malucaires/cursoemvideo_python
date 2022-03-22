#Calcular IMC
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('O seu peso é {:.2f}, a sua altura é {:.2f}, o seu IMC é {:.1f} e você está ABAIXO DO PESO!'.format(peso,altura,imc))
elif imc <= 25:
    print('O seu peso é {:.2f}, a sua altura é {:.2f}, o seu IMC é {:.1f} e você está com o PESO IDEAL!'.format(peso,altura,imc))
elif imc <= 30:
    print('O seu peso é {:.2f}, a sua altura é {:.2f}, o seu IMC é {:.1f} e você está com SOBREPESO!'.format(peso,altura,imc))
elif imc <= 40:
    print('O seu peso é {:.2f}, a sua altura é {:.2f}, o seu IMC é {:.1f} e você está com OBESIDADE!'.format(peso,altura,imc))
else:
    print('O seu peso é {:.2f}, a sua altura é {.:2f}, o seu IMC é {:.1f} e você está com OBESIDADE MÓRBIDA!'.format(peso,altura,imc))
print('--FIM--')