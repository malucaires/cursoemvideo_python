def leiaInt(n):
    """
    Função para imprimir valores numéricos
    :return: Número validado
    """
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except:
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        else:
            return n


def leiaFloat(n):
    """
    Função para imprimir valores reais
    :return: Número validado
    """
    while True:
        try:
            n = float(input('Digite um número real: '))
        except:
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
            continue
        else:
            return n
