def menu():
    cabecalho('MENU PRINCIPAL')
    menu=(['Mostrar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    c = 1
    for item in menu:
        print(f'\033[33m{c}\033[34m - {item}\033[m')
        c += 1
    print('-'*42)
    op = leiaInt()
    return op


def cabecalho(msg):
    print('-'*42)
    print(f'{msg:^42}')
    print('-'*42)


def leiaInt():
    while True:
        try:
            op = int(input('\033[33mDigite a sua opção: \033[m'))
        except:
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[m')
        else:
            if 1 <= op <= 3:
                break
            else:
                print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    return op
