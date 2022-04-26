
cores = {'padrao': '\033[m',
         'ciano': '\033[1;36m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Identificando informações em lista'.format('\033[1m').center(60))
deco()

lista = []
contador = 0

while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    if numero == 5:
        contador += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').strip().upper())

        if continuar == 'S':
            deco()

        if continuar == 'N':
            break

    if continuar == 'N':
        deco()
        break

lista.sort(reverse=True)
print('{}Foram digitados {}ª números nesta lista!{}'.format(cores['ciano'], len(lista), cores['padrao']))
print('{}Os valores da lista em ordem decrescente ficara:{} {}'
      .format(cores['ciano'], cores['padrao'], lista))

# ---------------------------------------------------------------------------------------------------
# Modo para verificar se possui o numero cinco [Utilizando a propria lista!]
if 5 in lista:
    print('{}O valor 5º se encontra na lista!{}'
          .format(cores['ciano'], cores['padrao']))

else:
    print('{}O valor 5ª não se encontra na lista!{}'.format(cores['vermelho'], cores['padrao']))

# ---------------------------------------------------------------------------------------------------
# Modo para verificar se possui o numero cinco [Utilizando apenas o contador!]
'''if contador == 0:
    print('{}O valor 5ª não se encontra na lista!{}'.format(cores['vermelho'], cores['padrao']))

else:
    print('{}O valor 5º se encontra na lista e foi digitado {}ª vezes!{}'
          .format(cores['ciano'], contador, cores['padrao']))'''
# ---------------------------------------------------------------------------------------------------
deco()
