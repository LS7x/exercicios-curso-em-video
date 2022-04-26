from time import sleep
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["vermelho"]}-{cores["padrao"]}' * 70)


deco()
print(f'{cores["negrito"]}Decifrando fatorial através de funções!'.center(70))
deco()


def fatorial(valor=1, show=False):
    """
    -> Calcula o fatorial de um número digitado pelo usuario!
    :param valor: Número a ser calculado
    :param show: Parametro opcional para efetuar mostragem da resolução
    :return: Retorna o valor do fatorial caso seja necessario a utilização
    """
    fat = 1

    if show:
        for numero in range(valor, 0, -1):
            if numero == 1:
                print(f'{numero} = ', end='')
                print(fat)
            else:
                print(f'{numero} X ', end='')
                fat = fat * numero
        return fat

    else:
        for numero in range(valor, 0, -1):
            fat = fat * numero
        return fat


digito = int(input('Digite o número que deseja ver o fatorial: '))
while True:
    parametro = str(input('Você deseja ver o processo de calculo do fatorial? [S/N]: ').upper().strip())

    if parametro == 'S' or parametro == 'N':
        deco()
        break

    else:
        print(f'{cores["vermelho"]}Parâmetro invalido, tente novamente...{cores["padrao"]}')
        deco()

sleep(1)
print(f'O fatorial do número {digito} é igual á {fatorial(digito)}')

if parametro == 'S':
    booleano = True
    sleep(1)
    fatorial(digito, booleano)
deco()

help(fatorial)
deco()
