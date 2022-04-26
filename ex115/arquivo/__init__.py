from PythonExercicios.ex115.banco import *


def arquivoExiste(name):
    try:
        arquivo = open(name, 'rt')
        arquivo.close()

    except FileNotFoundError:
        return False

    else:
        return True


def criarArquivo(name):
    try:
        arquivo = open(name, 'wt+')
        arquivo.close()

    except:
        print(f'{cores["vermelho"]}Ocorreu uma falha na criação do arquivo!{cores["padrao"]}')

    else:
        print(f'{cores["verde"]}Arquivo {name} criado com sucesso!{cores["padrao"]}')


def lerArquivo(name):
    try:
        arquivo = open(name, 'rt')

    except:
        print(f'{cores["vermelho"]}Ocorreu um erro na leitura do arquivo!{cores["padrao"]}')

    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>7} anos')
        arquivo.close()


def cadastrar(arq, name='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')

    except:
        print(f'{cores["vermelho"]}Ocorreu uma falha na abertura do arquivo!{cores["padrao"]}')

    else:
        try:
            arquivo.write(f'{name};{idade}\n')

        except:
            print(f'{cores["vermelho"]}Ocorreu uma falha na escritura dos dados!{cores["padrao"]}')

        else:
            print(f'{cores["verde"]}Novo registro de {name} foi adicionado!{cores["padrao"]}')
            arquivo.close()
