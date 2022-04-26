from time import sleep
cores = {'padrao': '\033[m',
         'azul': '\033[1;34m'}


def deco():
    print('{}-{}'.format(cores['azul'], cores['padrao'])*70)


deco()
print('{}LISTAGEM DE PREÇÕS | LOJA PYTHONCELL'.format('\033[1m').center(72))
deco()

lista = ('Samsung A22', 1200, 'Samsung A32', 1500, 'Samsung A52', 1700, 'Samsung A72', 2000,
         'Samsung S20 FE', 2300, 'Samsung S20', 3500, 'Samsung S21', 4000, 'Samsung 21 Ultra',
         6000, 'Samsung S22', 5400, 'Samsung S22 Ultra', 8400)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print('{:.<60}'.format(lista[posicao]), end='')

    else:
        print(f'R$: {lista[posicao]}')
        sleep(0.5)

deco()
