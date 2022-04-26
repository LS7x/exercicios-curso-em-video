cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'azul': '\033[1;34m'}


def aumentar(valor=0, porcento=1, formato=False):
    retorno = valor * ((porcento/100)+1)
    return retorno if formato is False else moeda(retorno)


def diminuir(valor=0, porcento=1, formato=False):
    retorno = valor - (valor * (porcento/100))
    return retorno if formato is False else moeda(retorno)


def dobro(valor=0, formato=False):
    retorno = valor * 2
    return retorno if formato is False else moeda(retorno)


def metade(valor=0, formato=False):
    retorno = valor / 2
    return retorno if formato is False else moeda(retorno)


def deco(valor=70):
    print(f'{cores["azul"]}-{cores["padrao"]}' * valor)


def titulo(msg):
    valor = len(msg) + 10
    deco(valor)
    print(f'{cores["negrito"]}{msg}'.center(valor+3))
    deco(valor)


def moeda(valor=0.00, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')
