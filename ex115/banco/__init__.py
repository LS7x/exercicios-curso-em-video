# from time import sleep
cores = {'padrao':   '\033[m',
         'negrito':  '\033[1m',
         'verde':    '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo':  '\033[1;33m'}


def deco(cor=cores["negrito"], tam=42):
    return print(f'{cor}-{cores["padrao"]}'*tam)


def titulo(msg='Sem texto'):
    deco()
    print(f'{cores["negrito"]}{msg}'.center(42))
    deco()


def menu(lista):
    titulo('MENU PRINCIPAL')
    i = 0
    for item in lista:
        i += 1
        print(f'{cores["amarelo"]}{i} - {cores["verde"]}{item}{cores["padrao"]}')
    deco()
    escolha = leiaInt(f'{cores["amarelo"]}Sua Opção: {cores["padrao"]}')
    return escolha


def leiaInt(valor):
    while True:
        try:
            escolha = int(input(valor))

        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Valor Inválida{cores["padrao"]}')
            deco()

        except KeyboardInterrupt:
            print(f'{cores["vermelho"]}Valor está em branco!{cores["padrao"]}')
            deco()

        else:
            return escolha
