from time import sleep
from datetime import date

cores = {'padrao' : '\033[m',
         'azul'   :    '\033[1;36m'}

print('{}-{}'.format('\033[1;35m', cores['padrao'])*60)
print('{}Seja bem-vindo seletor de categorias da CNN python!'
      '\nIremos verificar em qual classificação você se encaixa.{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format('\033[1;35m', cores['padrao'])*60)

ano = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year

idade = atual - ano
print('Aguarde, verificando...\n')
sleep(3)

if idade >= 120 or ano >= atual:
    print('{}Idade invalida, tente novamente!{}'.format('\033[1;31m', cores['padrao']))

elif idade <= 9:
    print('{}Você possui {} anos e faz parte da categoria MIRIM! Boa sorte!{}'.format(cores['azul'], idade, cores['padrao']))

elif idade <= 14:
    print('{}Você possui {} anos e faz parte da categoria INFANTIL! Boa sorte!{}'.format(cores['azul'], idade, cores['padrao']))

elif idade <= 19:
    print('{}Você possui {} anos e faz parte da categoria JUNIOR! Boa sorte!{}'.format(cores['azul'], idade, cores['padrao']))

elif idade <= 20:
    print('{}Você possui {} anos e faz parte da categoria SÊNIOR! Boa sorte!{}'.format(cores['azul'], idade, cores['padrao']))

elif idade > 20:
    print('{}Você possui {} anos e faz parte da categoria MASTER! Boa sorte!{}'.format(cores['azul'], idade, cores['padrao']))
