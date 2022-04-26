from PythonExercicios.ex115.banco import *
from PythonExercicios.ex115.arquivo import *
from time import sleep

arquivo = 'pythonDados.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    escolha = menu(["Verificar pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])

    if escolha == 1:
        lerArquivo(arquivo)

    elif escolha == 2:
        titulo('NOVO CADASTRO')
        while True:
            name = str(input('Nome: '))
            if name.isdigit():
                print(f'{cores["vermelho"]}Nome invalido!{cores["padrao"]}')
            else:
                break

        idade = leiaInt('Idade: ')
        cadastrar(arquivo, name, idade)

    elif escolha == 3:
        titulo('Saindo do sistema...')
        sleep(2)
        break

    else:
        print(f'{cores["vermelho"]}Opção Inválida{cores["padrao"]}')
