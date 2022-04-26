import emoji
import datetime
import sys
import os
from time import sleep

cores = {'cinza':'\033[37m',
         'ciano':'\033[36m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'padrao':'\033[m'}

print('{}-{}'.format(cores['verde'], cores['padrao'])*60)
print('{}Seja bem vindo! Ao Alistamento Militar\n'
      'Asseguir iremos verificar se seus serviçõs estão em dia!{}'.format('\033[1;33m', cores['padrao']))
print('{}-{}'.format(cores['verde'], cores['padrao'])*60)

nascimento = int(input('Digite o ano completo de seu nascimento: '))

# Criação de uma string para finalização do codigo!
def restart_program():
      reinicio = sys.executable
      os.execl(reinicio, reinicio, * sys.argv)

# Continuação do codigo porem caso a data de nascimento seja invalida!
if nascimento <= 1900:
      print('\nData de nascimento invalida!\n'
            'Favor tente novamente!')
      restart_program()

# Data Atual do computador:
atual = datetime.datetime.now()
data = atual.date()
ano = int(data.strftime("%Y"))

# Conversão para idade:
idade = ano - nascimento

print('Aguarde gerando resultados...\n')
sleep(3)

if idade == 18:
      print('Você tem ou irá fazer {} anos de idade este ano!'.format(idade))
      print('{}Chegou a hora de você se alistar campeão!{}'.format('\033[1;34m', cores['padrao']))

elif idade < 18:
      tempo = 18 - idade
      print('Você tem ou irá fazer {} anos de idade este ano!'.format(idade))
      print('{}Sorte sua! Ainda não esta na hora do seu alistamento.{}'.format(cores['verde'], cores['padrao']))
      print('{}Ainda faltam {} anos para seu alistamento.{}'.format(cores['verde'], tempo, cores['padrao']))

elif idade > 18:
      tempo = idade - 18
      print('Você tem ou irá fazer {} anos de idade este ano!\n'.format(idade))
      print(emoji.emojize('{}Amigão oque você esta esperando, seu prazo ja estorou!\n'
            'É bom você ir se alistar, e não esquesse que você já passou do prazo e no alistamento agora :sunglasses:{}'.format('\033[1;31m', cores['padrao']), use_aliases= True))
      print('{}Você deveria ter se alistado á {} anos atras.\n'.format('\033[1;31m', tempo, cores['padrao']))
