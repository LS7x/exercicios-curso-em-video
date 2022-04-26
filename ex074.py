from random import randint

cores = {'padrao': '\033[m',
         'azul': '\033[1;34m'}


def deco():
    print('{}-{}'.format(cores['azul'], cores['padrao'])*60)


deco()
print('{}Lista de numeros aleatorios'.format('\033[1m').center(60))
print('Organizados em uma tupla!{}'.format(cores['padrao']).center(60))
deco()

tupla = tuple(randint(1, 100) for gerar in range(1, 5+1))
print('{}Os números da tupla são: {}'.format(cores['azul'], cores['padrao']), end='')

for gerar in tupla:
    print(gerar, end=' ')

print()
deco()

print('{}O número com maior valor é {}{}'.format(cores['azul'], cores['padrao'], max(tupla)))
deco()
print('{}O número com menor valor é {}{}'.format(cores['azul'], cores['padrao'], min(tupla)))
deco()
