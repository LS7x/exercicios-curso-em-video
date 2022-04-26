
cores = {'padrao': '\033[m',
         'ciano': '\033[1;36m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Organizando listas! Pares e Ímpares'.format('\033[1m').center(60))
deco()

lista = []
listaPar = []
listaImpar = []
posicao = 0

while True:
    lista.append(int(input(f'Digite o valor da posição {posicao}ª da lista: ')))
    posicao += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').upper().strip())

        if continuar == 'N':
            break

        if continuar == 'S':
            deco()

    if continuar == 'N':
        deco()
        break

print('{}A lista completa ficara:{} {}'.format(cores['ciano'], lista, cores['padrao']))
# ----------------------------------------------------------------------------------------
# Encontrando o numero par e ímpar na lista!
for numero in lista:
    if numero % 2 == 0:
        listaPar.append(numero)

    else:
        listaImpar.append(numero)
# ----------------------------------------------------------------------------------------
listaPar.sort(), listaImpar.sort()

print('{}A lista de pares ficara:{} {}'.format(cores['ciano'], listaPar, cores['padrao']))
print('{}A lista de ímpares ficara:{} {}'.format(cores['ciano'], listaImpar, cores['padrao']))
