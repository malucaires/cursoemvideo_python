def aumentar(valor, porcentagem):
    res = valor * (1 + porcentagem / 100)
    res_moeda = moeda(res)
    return res_moeda


def diminuir(valor, porcentagem):
    res = valor * (1 - porcentagem/100)
    res_moeda = moeda(res)
    return res_moeda


def dobro(valor):
    res = valor * 2
    res_moeda = moeda(res)
    return res_moeda


def metade(valor):
    res = valor / 2
    res_moeda = moeda(res)
    return res_moeda


def moeda(valor):
    res = round(valor, 2)
    res = str(res)
    res = res.replace('.',',')
    res.join('R$ ')
    return res
