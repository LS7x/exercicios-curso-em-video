from time import sleep
import sys
import os

cores = {'padrao':'\033[m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['vermelho'], cores['padrao'])*80)
print('{}Bem vindo a pesquisa de campo da Python School'.format('\033[1m').center(80))
print('A seguir iremos perguntar alguns dados e revelar algumas informações a respeito!{}'.format(cores['padrao']))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*80)

# Criação de uma string para finalização do codigo!
def restart_program():
      reinicio = sys.executable
      os.execl(reinicio, reinicio, * sys.argv)

# Continuação do codigo!
media = 0
maiorIdadeHomem = 0
nomeOld = ''
contMulheres = 0

for pessoa in range(1, 4 + 1):
    nome = str(input('Digite o nome da {}º pessoa: '.format(pessoa)))
    idade = int(input('Digite a idade da {}º pessoa: '.format(pessoa)))

    # IF's para consertar bugs!
    if idade > 130 or idade <= 0:
        print('{}Valor invalido, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))
        restart_program()

    print('\n{}Agora utilize a seguinte regra:'
          '\nDigite [M] para masculino'
          '\nDigite [F] para feminino{}'.format('\033[1m', cores['padrao']))

    sexo = str(input('\nDigite o sexo da {}º pessoa: '.format(pessoa)))
    print('{}-{}'.format(cores['vermelho'], cores['padrao'])*80)

    # IF's para consertar bugs!
    if sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
        print('{}Valor invalido, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))
        restart_program()

    # Continuação do codigo:
    media += idade

    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeOld = nome

    if idade > maiorIdadeHomem and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeOld = nome

    if idade < 20 and sexo in 'Ff':
        contMulheres += 1

media /= 4

nomeOld = nomeOld.capitalize()
print('Aguarde, organizando...\n')
sleep(3)

print('{}A media de idade do grupo é de {:.2f} anos de idade'.format('\033[1m', media))
print('O nome do homem mais velho do grupo é {} e sua idade é de {} anos.'.format(nomeOld, maiorIdadeHomem))
print('O numero de mulheres abaixo dos 20 anos no grupo é de {} mulheres'.format(contMulheres))
