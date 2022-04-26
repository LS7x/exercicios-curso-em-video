from datetime import datetime
from time import sleep
from sys import executable, argv
from os import execl

cores = {'padrao':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}

print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)
print('{}Seja bem-vindo a calculadora Python'.format('\033[1m').center(60))
print('Dessa vez iremos verificar a maior idade no Brasil!{}'.format(cores['padrao']))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)

# Criação de uma string para finalização do codigo!
def restart_program():
      reinicio = executable
      execl(reinicio, reinicio, * argv)

# Continuação do codigo
anoAtual = datetime.now().year
maiorIdade = anoAtual - 18
num = 1
pessoasMaior = 0
pessoasMenor = 0

for variavel in range(1, 7 + 1):
    ano = int(input('Em que ano a {}º nasceu: '.format(num)))
    num += 1
    if ano < 1900 or ano > anoAtual:
        print('{}Ano invalido, favor tente novamente...{}'.format(cores['vermelho'], cores['padrao']))
        restart_program()

    if ano <= maiorIdade:
        pessoasMaior += 1
    else:
        pessoasMenor += 1

print('Aguarde, calculando...\n')
sleep(3)

print('{}O numero de maiores de idade é de {} pessoas{}'.format(cores['verde'], pessoasMaior, cores['padrao']))
print('{}E o numero de menores de idade é de {} pessoas{}'.format(cores['vermelho'], pessoasMenor, cores['padrao']))
