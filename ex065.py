from time import sleep

cores = {'padrao':'\033[m',
         'azul':'\033[1;34m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}

print('{}-{}'.format(cores['azul'], cores['padrao'])*90)
print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(90))
print('Desta vez iremos revelar algumas informaçoes a respeito dos seus números digitados.{}'.format(cores['padrao']))
print('{}-{}'.format(cores['azul'], cores['padrao'])*90)

# Continuação do codigo!
continuar = 'S'
contador = 0
media = 0
booleano = False

maior = menor = 0
finalizar = False

valor = int(input('{}Digite um número: {}'.format(cores['verde'], cores['padrao'])))
print()

while not finalizar:
    while not booleano:
        print('{}Segue a regra a seguir para continuar [S] e para parar [N]!{}'.format('\033[1m', cores['padrao']))
        continuar = str(input('Você deseja continuar: ')).upper().strip()
        print()
        contador += 1
        media += valor

        if contador == 1:
            maior = menor = valor

        else:
            if valor > maior:
                maior = valor

            elif valor < menor:
                menor = valor

        if continuar == 'S':
            valor = int(input('{}Digite um número: {}'.format(cores['verde'], cores['padrao'])))
            print()

        elif continuar == 'N':
            finalizar = True
            booleano = True

        elif continuar != 'N':
            print('{}Opção invalida, tente novamente...\n{}'.format(cores['vermelho'], cores['padrao'], end=''))
            media -= valor
            contador -= 1


media /= contador
print('Aguarde, calculando resultados...\n')
sleep(3)

print('{}O valor da media entre os valores digitados serão de {:.2f}{}'.format(cores['azul'], media, cores['padrao']))
print('{}O menor valor digitado equivale á {}{}'.format(cores['azul'], menor, cores['padrao']))
print('{}O maior valor digitado equivale á {}{}'.format(cores['azul'], maior, cores['padrao']))
print('{}-{}'.format(cores['azul'], cores['padrao'])*90)
