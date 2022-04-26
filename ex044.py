from time import sleep
import sys
import os

cores = {'padrao': '\033[m',
         'azul': '\033[1;34m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'roxo': '\033[1;35m'}


# Criação de uma string para finalização do codigo!
def restart_program():
    reinicio = sys.executable
    os.execl(reinicio, reinicio, *sys.argv)


# Continuação do codigo!
print('{}-{}'.format(cores['azul'], cores['padrao']) * 65)
print('{}Seja bem vindo ao Python calculo!'
      '\nIremos verificar o preço do produto e iformar seu real valor!{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['azul'], cores['padrao']) * 65)

valor = float(input('Digite o valor do produto: R$'))

print('\n{}Asseguir digite o numero correto para a forma de pagamento escolhida!{}'.format('\033[1m', cores['padrao']))
print('{}[1]{} Pagamento à vista no dinheiro, cheque ou cartão de debito!'.format(cores['verde'], cores['padrao']))
print('{}[2]{} Pagamento à vista no cartão de credito!'.format(cores['verde'], cores['padrao']))
print('{}[3]{} Pagamento em até 2x no cartão!'.format(cores['verde'], cores['padrao']))
print('{}[4]{} Pagamento em 3x ou mais no cartão!\n'.format(cores['verde'], cores['padrao']))

forma = int(input('Digite o numero da forma de pagamento: '))
if forma == 4:
    vezes = int(input('Em quantas vezes sera dividido: '))
    dividido = valor / vezes

print('Aguarde, gerando pagamento...\n')
sleep(3)

if valor <= 0:
    print('{}Valor invalido! Tente novamente.{}'.format(cores['vermelho'], cores['padrao']))
    restart_program()

elif forma > 4:
    print('{}Forma de pagamento invalida! tente novamente.{}'.format(cores['vermelho'], cores['padrao']))

elif (vezes < 3) or (vezes > 24):
    print('{}Quantidade de parcelamentos invalida! tente novamente.'.format(cores['vermelho'], cores['padrao']))
    restart_program()

if forma == 1:
    nvalor = valor * 0.90
    print('{}O Produto no valor de R${:.2f} recebera desconto de 10%!'
          '\nFicando com o novo valor em R${:.2f} com esta forma de pagamento!{}'
          .format(cores['verde'], valor, nvalor, cores['padrao']))

elif forma == 2:
    nvalor = valor * 0.95
    print('{}O produto no valor de R${:.2f} recebera desconto de 5%!'
          '\nFicando com o novo valor em R${:.2f} com esta forma de pagamento!{}'
          .format(cores['azul'], valor, nvalor, cores['padrao']))

elif forma == 3:
    print('{}O produto se mantera com o mesmo valor de R${:.2f} com esta forma de pagamento!{}'
          .format('\033[1m', valor, cores['padrao']))

elif forma == 4:
    nvalor = valor * 1.20
    print('{}O produto no valor de R${:.2f} recebera juros de 20%!'
          '\nO Produto sera parcelado em {}x de R${:.2f} !'
          '\nFicando com o novo valor total em R${:.2f} com esta forma de pagamento!{}'
          .format(cores['roxo'], valor, vezes, dividido, nvalor, cores['padrao']))
