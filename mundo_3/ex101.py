from datetime import date


def voto(a):
    """
    Verifica se a pessoa pode votar conforme o ano de nascimento

    :param a: ano de nascimento
    :return: voto negado, opcional ou obrigatório
    """
    ano_atual = date.today().year
    idade = ano_atual - a
    if idade < 16:
        v = f'Com {idade} anos: voto NEGADO.'
    elif 16 <= idade <= 18 or idade >=65:
        v = f'Com {idade} anos: voto OPCIONAL.'
    else:
        v = f'Com {idade} anos: voto OBRIGATÓRIO.'
    return v


ano = int(input('Ano de nascimento: '))
print(f'{voto(ano)}')
