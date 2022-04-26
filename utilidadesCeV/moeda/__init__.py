cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'azul': '\033[1;34m'}


def aumentar(valor=0.00, porcento=1, formato=False):
    retorno = valor * ((porcento/100)+1)
    return retorno if formato is False else moeda(retorno)


def diminuir(valor=0.00, porcento=1, formato=False):
    retorno = valor - (valor * (porcento/100))
    return retorno if formato is False else moeda(retorno)


def dobro(valor=0.00, formato=False):
    retorno = valor * 2
    return retorno if formato is False else moeda(retorno)


def metade(valor=0.00, formato=False):
    retorno = valor / 2
    return retorno if formato is False else moeda(retorno)


def deco(valor=70):
    print(f'{cores["azul"]}-{cores["padrao"]}' * valor)


def titulo(msg):
    valor = len(msg) + 20
    deco(valor)
    print(f'{cores["negrito"]}{msg}'.center(valor+3))
    deco(valor)


def moeda(valor=0.00, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')


def resumo(valor=0.00, aumento=1, reducao=1, formato=False):
    titulo('RESUMO DO VALOR!')
    print(f'Valor analisado: \t{valor if formato is False else moeda(valor)}')
    print(f'Dobro do valor: \t{dobro(valor, formato):}')
    print(f'Metade do valor: \t{metade(valor, formato)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, formato)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, formato)}')
    deco(36)
