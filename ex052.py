
cores = {'padrao':'\033[m',
         'ciano':'\033[1;36m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m'}

print('{}-{}'.format(cores['ciano'], cores['padrao'])*70)
print('{}Bem-vindo a calculadora Python!'.format('\033[1m').center(70))
print('Desta vez iremos verificar se seu número é um número primo.{}'.format(cores['padrao']))
print('{}-{}'.format(cores['ciano'], cores['padrao'])*70)

numero = int(input('Digite seu número: '))

total = 0
for primos in range(1, numero + 1):
    if numero % primos == 0:
        print(cores['ciano'], end='')
        total += 1
    else:
        print(cores['padrao'], end='')
    print('{} '.format(primos), end='')
print()
if total > 2 or total == 1:
    print('{}O número {} foi dividido {} vezes e portanto não é um número PRIMO!{}'
          .format(cores['vermelho'], numero, total, cores['padrao']))

elif total == 2:
    print('{}O número {} foi dividido {} vezes e portanto é um número PRIMO!{}'
          .format(cores['verde'], numero, total, cores['padrao']))

else:
    print('{}Número invalido, tente novamente!'.format(cores['vermelho'], cores['padrao']))
