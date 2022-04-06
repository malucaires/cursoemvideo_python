def aumentar(valor=0, porcentagem=0, formato=False):
    """
    Aumenta o valor informado conforme a porcentagem informada
    :param valor: valor inicial
    :param porcentagem: taxa de aumento
    :param formato: formata para moeda caso True
    :return:
    """
    res = valor * (1 + porcentagem / 100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, porcentagem=0, formato=False):
    """
    Diminui o valor informado conforme porcentagem
    :param valor: valor inicial
    :param porcentagem: taxa de diminuição
    :param formato: formatado para moeda caso True
    :return: valor final
    """
    res = valor * (1 - porcentagem/100)
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    """
    Retorna o dobro do valor inicial
    :param valor: valor inicial
    :param formato: formatado para moeda caso True
    :return: valor final
    """
    res = valor * 2
    return res if formato is False else moeda(res)


def metade(valor=0, formato=False):
    """
    Retorna a metade do valor inicial
    :param valor: valor inicial
    :param formato: formatado para moeda caso True
    :return: valor final
    """
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$ '):
    """
    Formata para moeda
    :param valor: valor indicado
    :param moeda: símbolo da moeda desejada
    :return: retorna valor formatado
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aum=0, dim=0):
    print('='*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('='*30)
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Dobro do preço:\t\t{dobro(valor, True)}')
    print(f'Metade do preço:\t{metade(valor,True)}')
    print(f'{aum}% de aumento:\t\t{aumentar(valor, aum, True)}')
    print(f'{dim}% de diminuição:\t{diminuir(valor, dim, True)}')
    print('='*30)
