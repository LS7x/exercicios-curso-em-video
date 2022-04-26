from random import randint

cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('{}Seja bem vindo ao Pyhton Games!'.format('\033[1m').center(60))
print('Desta vez vamos jogar PAR ou IMPAR! Boa sorte!{}'.format(cores['padrao']).center(60))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

print('{}Regras do jogo:'
      '\nPara escolher PAR utilize [P]'
      '\nPara escolher IMPAR utilize [I]' .format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

contador = 0
vitorias = 0

while True:
    valorComputador = randint(0, 5)
    valorPlayer = int(input('Digite o número: '))
    player = str(input('Faça sua escolha: ')).upper().strip()
    valor = valorPlayer + valorComputador

    if player in 'PI':
        print('\nVocê jogou {} e o computador jogou {}! O total deu {}! '
              .format(valorPlayer, valorComputador, valor), end='')
        contador += 1

        if (valor % 2) == 0:  # Se for divisivel por dois é PAR!
            print('DEU {}PAR!{}'.format(cores['amarelo'], cores['padrao']))
            if player == 'P':
                print('{}Parabens você ganhou!{}'.format(cores['verde'], cores['padrao']))
                vitorias += 1

            else:
                print('{}Que pena, você perdeu :({}'.format(cores['vermelho'], cores['padrao']))
                print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
                break

        else:  # Se não for divisivel, então é impar!
            print('DEU {}IMPAR!{}'.format(cores['amarelo'], cores['padrao']))
            if player == 'I':
                print('{}Parabens você ganhou!{}'.format(cores['verde'], cores['padrao']))
                vitorias += 1

            else:
                print('{}Que pena, você perdeu :({}'.format(cores['vermelho'], cores['padrao']))
                print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
                break
        print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)

    if player not in 'PI':
        print('\n{}Escolha invalida, tente novamente...{}'.format(cores['vermelho'], cores['padrao']))
        print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)


print('{}Você jogou {} vezes e venceu {}!{}'.format(cores['verde'], contador, vitorias, cores['padrao']))
