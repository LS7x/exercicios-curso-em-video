from time import sleep
import sys
import os

cores = {'padrao':'\033[m',
         'amarelo':'\033[1;33m',
         'ciano':'\033[1;36m',
         'roxo':'\033[1;35m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*65)
print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(65))
print('Dessa vez vamos organizar os pesos das pesssoas selecionadas!{}'.format(cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*65)

# Criação de uma string para finalização do codigo!
def restart_program():
      reinicio = sys.executable
      os.execl(reinicio, reinicio, * sys.argv)

# Continuação do codigo!
maiorPesso = 0
menorPesso = 0

for pessoas in range(1, 5 + 1):
    pesos = float(input('Digite o peso da {}º pessoa: '.format(pessoas)))
    if pesos < 0:
        print('{}Valor de peso invalido, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))
        restart_program()

    if pessoas == 1:
        maiorPesso = pesos
        menorPesso = pesos
    else:
        if pesos > maiorPesso:
            maiorPesso = pesos

        elif pesos < menorPesso:
            menorPesso = pesos

print('Aguarde, calculando!\n')
sleep(3)

print('{}O maior peso é de {:.2f}Kg{}'.format(cores['roxo'], maiorPesso, cores['padrao']))
print('{}O menor peso é de {:.2f}kg{}'.format(cores['ciano'], menorPesso, cores['padrao']))
