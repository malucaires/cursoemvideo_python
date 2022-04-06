import interface as i

def se_arq_existe(arq):
    try:
        arquivo = open(arq, 'rt')
    except:
        arquivo = open(arq, 'wt+')
        print(f'O arquivo {arq} foi criado')
    finally:
        arquivo.close()


def ler_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        i.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar_pessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao adicionar a pessoa.')
        else:
            print(f'{nome} adicionado com sucesso.')
    finally:
        a.close()
