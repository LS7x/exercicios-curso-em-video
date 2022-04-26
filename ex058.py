from random import randint

cores = {'padrao':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}

print('{}-{}'.format(cores['azul'], cores['padrao'])*55)
print('{}Seja bem-vindo ao Python games!'.format('\033[1m').center(55))
print('Hoje iremos jogar o jogo da adivinhação melhorado.{}'.format(cores['padrao']))
print('{}-{}'.format(cores['azul'], cores['padrao'])*55)

numMaquina = randint(0, 10)
acertou = False
contador = 0

while not acertou:
    numPlayer = int(input('Tente adivinhar o numero em que pensei: '))

    if numPlayer == numMaquina:
        acertou = True
    else:
        print('{}Que pena você errou hahaha :){}'.format(cores['vermelho'], cores['padrao']))

        if numPlayer > numMaquina:
            print('{}Tente denovo soque um pouco menos!{}\n'.format('\033[1m', cores['padrao']))

        elif numPlayer < numMaquina:
            print('{}Tente denovo soque um pouco mais!{}\n'.format('\033[1m', cores['padrao']))
    contador += 1

print('{}Parabens você acertou :('.format(cores['verde']))
print('Você precisou de atualmente {} tentativas para acertar!{}'.format(contador, cores['padrao']))
print('{}-{}'.format(cores['azul'], cores['padrao'])*55)
