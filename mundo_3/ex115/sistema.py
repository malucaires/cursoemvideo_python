import interface as i
import arquivo as a
from time import sleep

arq = 'cursoemvideo.txt'
a.se_arq_existe(arq)
while True:
    op = i.menu()
    sleep(1)
    if op == 1:
        i.cabecalho(f'LEITURA')
        a.ler_arquivo(arq)
    elif op == 2:
        i.cabecalho(f'NOVO CADASTRO')
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        a.cadastrar_pessoa(arq, nome, idade)
    elif op == 3:
        break
i.cabecalho(f'Saindo do sistema... Até logo!')

