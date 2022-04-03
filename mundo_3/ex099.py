from time import sleep


def maior(* num):
    print('-='*25)
    print('Analisando os valores passados...')
    maior = num[0]
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi o {maior}.')


#Programa principal
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(5, 9, 12, 4, 0, 4)
