
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["verde"]}-{cores["padrao"]}'*70)


deco()
print(f'{cores["negrito"]}Analisando notas através de funções e resultando em bibliotecas!'.center(72))
deco()


def notas(*string, sit=False):
    """
    -> Efetua a leitura das notas realizando calculos em bibliotecas!
    :param string: Os valores das notas recebidas
    :param sit: A condição para implantar a situação
    :return: Retorno do dicionario a variavel.
    """
    dicio = dict()
    dicio['Total'] = len(string)
    dicio['Maior'] = max(string)
    dicio['Menor'] = min(string)
    dicio['Média'] = sum(string) / len(string)

    if sit:
        if dicio['Média'] >= 7:
            dicio['Situação'] = 'BOA'

        elif dicio['Média'] >= 5 < 7:
            dicio['Situação'] = 'RAZOÁVEL'

        else:
            dicio['Situação'] = 'RUIM'

    return dicio


# MAIN
resp = notas(5.5, 5, 0, 6.5, sit=True)

for keys, values in resp.items():
    print('{} = {} | '.format(keys, values), end='')
print()
deco()

help(notas)
deco()
