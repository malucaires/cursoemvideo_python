#Digite uma temperatura em Celsius e converta para Fahrenheit
celsius=float(input('Digite a temperatura em Celsius: '))
fahrenheit=celsius*(9/5)+32
print('A temperatura de {:.2f}ºC equivale a {:.2f}ºF'.format(celsius,fahrenheit))