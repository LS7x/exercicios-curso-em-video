from time import sleep
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'amarelo': '\033[1;33m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}' * 80)


deco()
print(f'{cores["negrito"]}Iremos analisar valores, atraves de funções e desempacotamento!'.center(80))


def contador(*numero):
    contator = 0
    deco()
    sleep(0.5)
    print(f'{cores["negrito"]}Analisando os valores passados!{cores["padrao"]}')
    for num in numero:
        sleep(0.5)
        print(num, end=' ')
        contator += 1
    sleep(0.5)
    print(f'Foram informados {len(numero)} valores ao todo.')
    sleep(0.5)

    if contator == 0:
        print(f'Não obteve maior valor, pois o mesmo não apresenta valores!')
    else:
        print(f'O maior valor informado foi {max(numero)}.')


contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador()
deco()
