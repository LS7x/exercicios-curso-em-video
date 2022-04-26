from random import randint
from time import sleep
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m'}


def deco():
    print(f'{cores["verde"]}-{cores["padrao"]}' * 70)


deco()
print(f'{cores["negrito"]}Sorteando e somando valores pares através de funções!'.center(70))
deco()

valores = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for numero in range(0, 5):
        numero = randint(1, 10)
        valores.append(numero)

        sleep(0.5)
        print(numero, end=' ')
    sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    pares = 0
    print(f'Somando os valores pares de ', end='')
    for numero in valores:
        sleep(0.5)
        print(numero, end=' ')
        if numero % 2 == 0:
            pares += numero
    sleep(0.5)
    print(f'temos {pares}')


sorteia(valores)
somaPar(valores)
deco()
