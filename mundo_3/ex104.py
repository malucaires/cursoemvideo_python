def leiaint(n):
    """
    Função para imprimir valores numéricos
    :return: Número validado
    """
    while True:
        n = input('Digite um número: ')
        if n.isdigit() == False:
            print(f'\033[31m ERRO! Digite um número válido!\033[m')
        else:
            n = int(n)
            return n


#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
