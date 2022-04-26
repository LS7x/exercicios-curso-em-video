from time import sleep

cores = {'padrao':'\033[m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(60))
print('Desta vez, fique avontade para escolher uma função!{}'.format(cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

sair = False

while not sair:
    num1 = float(input('Digite o 1º valor: '))
    num2 = float(input('Digite o 2º valor: '))
    print()
    reinicio = False

    while not reinicio:
        print('{}A seguir escolha a função desejada:{}'.format(cores['amarelo'], cores['padrao']))
        print('{}[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Saber o maior valor\n'
              '[4] Reiniciar\n'
              '[5] Sair{}\n'.format('\033[1m', cores['padrao']))

        funcao = int(input('Digite a função: '))
        if funcao == 1:
            resulSoma = num1 + num2
            print('O soma entre {} e {} sera de {}{}{}'
                  .format(num1, num2, cores['amarelo'], resulSoma, cores['padrao']))
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
            sleep(2)

        elif funcao == 2:
            resulMulti = num1 * num2
            print('A multiplicação entre {} e {} sera de {}{}{}'
                  .format(num1, num2, cores['amarelo'], resulMulti, cores['padrao']))
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
            sleep(2)

        elif funcao == 3:
            resulMaior = num1

            if num2 > resulMaior:
                resulMaior = num2

            print('O maior numero entre {} e {} sera de {}{}{}'
                  .format(num1, num2, cores['amarelo'], resulMaior, cores['padrao']))
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
            sleep(2)

        elif funcao == 4:
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
            reinicio = True
            sleep(2)

        elif funcao == 5:
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
            sair = True
            reinicio = True

        else:
            print('{}Opção invalida, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))
            print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
