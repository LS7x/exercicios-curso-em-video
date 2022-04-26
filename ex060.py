from time import sleep

cores = {'padrao':'\033[m',
         'azul':'\033[1;34m'}

print('{}-{}'.format(cores['azul'], cores['padrao'])*60)
print('{}Calculando números fatoriais!{}'.format('\033[1m',cores['padrao']).center(60))
print('{}-{}'.format(cores['azul'], cores['padrao'])*60)

numero = int(input('Digite o numero: '))
contator = numero

print('Aguarde calculando...\n')
sleep(3)

fatorial = 1

print('Fatorial de !{} = '.format(contator), end='')

while contator > 0:
    print('{}'.format(contator), end='')
    print(' x ' if contator > 1 else ' = ', end='')
    fatorial *= contator
    contator -= 1

print('{}'.format(fatorial))
print('{}-{}'.format(cores['azul'], cores['padrao'])*60)
