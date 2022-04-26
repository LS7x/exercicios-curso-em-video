from random import randint
from time import sleep
cores = {'padrao': '\033[m', 'amarelo': '\033[1;33m'}


def deco():
    print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)


deco()
print('{}Gerador de números para MEGA SENA!'.format('\033[1m').center(60))
deco()

lista = []
jogos = []
contador = 0

while True:
    quantidade = int(input('Quantos jogos você que sortear: '))
    deco()

    for numero in range(1, quantidade+1):
        for n in range(1, 6 + 1):

            # Verificar se o número aleatorio não esta se repetindo
            while True:
                numeroAleatorio = randint(1, 60)

                if numeroAleatorio not in lista:
                    lista.append(numeroAleatorio)
                    break

        lista.sort()
        jogos.append(lista[:])
        lista.clear()

        sleep(1)
        print('{}Jogo {}ª:{} {}'.format(cores['amarelo'], numero, cores['padrao'], jogos[contador]))
        contador += 1

    deco()
    break

# print('{}Lista completa:{} {}'.format(cores['amarelo'], cores['padrao'], jogos))
