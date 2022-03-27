#Tupla tot
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end= ' ')
    print(f'Você digitou o número {extenso[num]}.')
    while True:
        cont = str(input('Você deseja continuar? [S/N] ')).upper().strip()
        if cont in 'SN':
            break
        else:
            print('Opção inválida, tente novamente!', end= ' ')
    if cont == 'N':
        break
print('FIM')