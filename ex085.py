
cores = {'padrao': '\033[m', 'ciano': '\033[1;36m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Lendo valores pares e ímpares em listas compostas!'.format('\033[1m').center(60))
deco()
# --------------------------------------------------------------------------------------------------
# Programa feito porem não utilizando listas compostas!
'''temporario = 0
pares = []
impares = []
lista = []

for numero in range(1, 7 + 1):
    temporario = int(input(f'Digite o valor do {numero}ª número: '))

    if temporario % 2 == 0:
        pares.append(temporario)

    else:
        impares.append(temporario)

deco()
pares.sort(), impares.sort()
lista.append(pares), lista.append(impares)
print('{}Os valores pares são:{} {}'.format(cores['ciano'], cores['padrao'], pares))
print('{}Os valores impares são:{} {}'.format(cores['ciano'], cores['padrao'], impares))
print('{}A lista completa é:{} {}'.format(cores['ciano'], cores['padrao'], lista))'''
# --------------------------------------------------------------------------------------------------
# Utilizando a lista composta:

lista = [[], []]
temporario = 0

for numero in range(1, 7 + 1):
    temporario = int(input(f'Digite o valor do {numero}ª número: '))

    if temporario % 2 == 0:
        lista[0].append(temporario)

    else:
        lista[1].append(temporario)

deco()
lista[0].sort(), lista[1].sort()
print('{}Os valores pares são:{} {}'.format(cores['ciano'], cores['padrao'], lista[0]))
print('{}Os valores impares são:{} {}'.format(cores['ciano'], cores['padrao'], lista[1]))
print('{}A lista completa é:{} {}'.format(cores['ciano'], cores['padrao'], lista))
# --------------------------------------------------------------------------------------------------
