def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print(f'\33[31mERRO: {entrada} é um preço inválido!\33[m')
        else:
            valido = True
            return float(entrada)


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
