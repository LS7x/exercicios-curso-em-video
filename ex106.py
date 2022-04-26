from time import sleep

cores = ('\033[m',  # Padrão
         '\033[1m',  # Negrito
         '\033[7;37;40m',  # Verde
         '\033[1;31;40m',  # Vermelho
         '\033[1;33;40m')  # Amarelo


def deco(cor=0):
    print(cores[cor], end='')
    print('-' * 70, end='')
    print(cores[0])


def titulo(msg, cor=0):
    deco(3)
    print(cores[cor], end='')
    print(msg.center(65), end='')
    print(cores[0])
    deco(3)


titulo('Sistema de ajuda interativa PyHelp', 1)
print(f'{cores[2]}Este programa irar informar as funcionalidades de tal função')
print('Para finalizar o programa escreva a palavra fim!')
print(f'{cores[0]}', end='')


def interactiveHelp(cor=0):
    while True:
        deco(3)
        valor = str(input('Digite a função ou biblioteca desejada: ').strip().lower())

        if valor == 'fim':
            print('Finalizando programa...')
            sleep(1)
            deco(3)
            break

        else:
            titulo(f'Acessando o manual interativo do comando "{valor}"', 1)
            sleep(1)
            print(cores[cor], end='')
            help(valor)
            print(cores[0], end='')


interactiveHelp(2)
