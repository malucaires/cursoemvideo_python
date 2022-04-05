def backcolor(cor):
    if cor == 'Verde':
        print('\033[42m', end='')
    elif cor == 'Azul':
        print('\033[30;44m', end='')
    elif cor == 'Branco':
        print('\033[30;107m', end='')
    elif cor == 'Padrão':
        print('\033[m', end='')
    elif cor == 'Vermelho':
        print('\033[41m', end='')


def titulo(a):
    print('~'*(len(a)+2))
    print(f' {a}')
    print('~'*(len(a)+2))


#Programa Principal
backcolor('Verde')
titulo('SISTEMA DE AJUDA PyHELP')
while True:
    backcolor('Padrão')
    funcao = input('Função ou Biblioteca > ')
    if funcao.upper() == 'FIM':
        backcolor('Vermelho')
        titulo('ATÉ LOGO!')
        break
    backcolor('Azul')
    titulo(f'Acessando o manual do comando {funcao}')
    backcolor('Branco')
    help(funcao)
