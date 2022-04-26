from random import randint
from time import sleep
import sys
import os

cores = {'padrao': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m'}


# Criação de uma string para finalização do codigo!
def restart_program():
    reinicio = sys.executable
    os.execl(reinicio, reinicio, *sys.argv)


print('{}-{}'.format(cores['verde'], cores['padrao']) * 50)
print('{}Seja bem-vindo ao Python Games!'
      '\nO game do dia sera Jokenpô, aproveite.{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['verde'], cores['padrao']) * 50)

print('{}Para jogar siga as instruções abaixo:{}'.format('\033[1m', cores['padrao']))
print('{}[0]{} Para Pedra!'
      '\n{}[1]{} Para Papel!'
      '\n{}[2]{} Para Tesoura!'
      .format(cores['verde'], cores['padrao'], cores['verde'], cores['padrao'], cores['verde'], cores['padrao']))

player = int(input('\nDigite o numero escolhido: '))

if player > 3 or player < 0:
    print('{}Opção invalida! Tente novamente...{}'.format(cores['vermelho'], cores['padrao']))
    restart_program()

print('Agora irei fechar meus olhos e escolher um aleatoriamente!')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('\n{}JO!'.format('\033[1m'))
sleep(1)
print('KEN!')
sleep(1)
print('PÓ!{}\n'.format(cores['padrao']))
sleep(1)

print('{}-{}'.format(cores['verde'], cores['padrao']) * 70)
print('{}Eu escolhi {} e você escolheu {}{}'.format('\033[1m', itens[computador], itens[player], cores['padrao']))

if computador == 0:  # Escolheu Pedra
    if player == 0:  # Escolheu Pedra
        print('{}DRAWN! Hum que sorte deu empate!{}'.format(cores['azul'], cores['padrao']))

    elif player == 1:  # Escolheu Papel
        print('{}Parabens! Você ganhou :({}'.format(cores['verde'], cores['padrao']))

    elif player == 2:  # Escolheu Tesoura
        print('{}Eu ganhei HAHAHA! Mais sorte na proxima! :){}'.format(cores['vermelho'], cores['padrao']))

if computador == 1:  # Escolheu Papel
    if player == 0:  # Escolheu Pedra
        print('{}Eu ganhei HAHAHA! Mais sorte na proxima! :){}'.format(cores['vermelho'], cores['padrao']))

    elif player == 1:  # Escolheu Papel
        print('{}DRAWN! Hum que sorte deu empate!{}'.format(cores['azul'], cores['padrao']))

    elif player == 2:  # Escolheu Tesoura
        print('{}Parabens! Você ganhou :({}'.format(cores['verde'], cores['padrao']))

if computador == 2:  # Escolheu Tesoura
    if player == 0:  # Escolheu Pedra
        print('{}Parabens! Você ganhou :({}'.format(cores['verde'], cores['padrao']))

    elif player == 1:  # Escolheu Papel
        print('{}Eu ganhei HAHAHA! Mais sorte na proxima! :){}'.format(cores['vermelho'], cores['padrao']))

    elif player == 2:  # Escolheu Tesoura
        print('{}DRAWN! Hum que sorte deu empate!{}'.format(cores['azul'], cores['padrao']))

print('{}-{}'.format(cores['verde'], cores['padrao']) * 70)
