cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'azul': '\033[1;34m'}


def aumentar(valor=0, porcento=1):
    retorno = valor * ((porcento/100)+1)
    return retorno


def diminuir(valor=0, porcento=1):
    retorno = valor - (valor * (porcento/100))
    return retorno


def dobro(valor=0):
    retorno = valor * 2
    return retorno


def metade(valor=0):
    retorno = valor / 2
    return retorno


def deco(valor=70):
    print(f'{cores["azul"]}-{cores["padrao"]}' * valor)


def titulo(msg):
    valor = len(msg) + 10
    deco(valor)
    print(f'{cores["negrito"]}{msg}'.center(valor+3))
    deco(valor)
