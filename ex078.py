cores = {'padrao': '\033[m',
         'verde': '\033[1;32m'}


def deco():
    print('{}-{}'.format(cores['verde'], cores['padrao']) * 60)


deco()
print('{}Organizando listas em Python'.format('\033[1m').center(60))
deco()
maxValor = 0
minValor = 0

valores = []
# Para descobrir o maior e menor valor:
for quantidade in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {quantidade}ª: ')))
    if quantidade == 0:
        maxValor = valores[quantidade]
        minValor = valores[quantidade]

    else:
        if valores[quantidade] > maxValor:
            maxValor = valores[quantidade]

        if valores[quantidade] < minValor:
            minValor = valores[quantidade]

deco()
print('{}Você digitou os valores: {}{}'.format(cores['verde'], cores['padrao'], valores))

# ------------------------------------------------------------------
print('{}O maior valor digitado foi:{} {} nas posições '
      .format(cores['verde'], cores['padrao'], maxValor), end='')

# Para descobrir à posição do valor:
for indiceMax, valor in enumerate(valores):
    if valor == maxValor:
        print(f'{indiceMax}... ', end='')
print()
# ------------------------------------------------------------------

# ------------------------------------------------------------------
print('{}O menor valor digitado foi:{} {} nas posições '
      .format(cores['verde'], cores['padrao'], minValor), end='')

# Para descobrir à posição do valor:
for indiceMin, valor in enumerate(valores):
    if valor == minValor:
        print(f'{indiceMin}... ', end='')
print()
# ------------------------------------------------------------------

deco()
