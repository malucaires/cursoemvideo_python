def ficha(n='<desconhecido>',g=0):
    """
    Retorna a ficha do jogador conforme o nome e a quantidade de gols

    :param n: (opcional) nome do jogador
    :param g: (opcional) quantidade de gols marcada
    :return: ficha do jogador
    """
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


#Programa Principal
nome = input('Digite o nome do jogador: ').title()
gols = input('Digite a quantidade de gols: ')
if nome != '':
    if gols != '':
        gols = int(gols)
        ficha(nome, gols)
    else:
        ficha(nome)
elif gols != '':
    gols = int(gols)
    ficha(g=gols)
else:
    ficha()
