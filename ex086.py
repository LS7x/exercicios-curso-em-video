
cores = {'padrao': '\033[m', 'ciano': '\033[1;36m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Elaborando matrizes, apartir de listas!'.format('\033[1m').center(60))
deco()

valor = 0
contador1 = 0
contador2 = 0

lista = [[], [], []]
for numeros in range(1, 9 + 1):
    valor = int(input(f'Digite o valor para posição [{contador1}, {contador2}]: '))
    contador2 += 1

    if contador1 == 0:
        lista[0].append(valor)

    elif contador1 == 1:
        lista[1].append(valor)

    elif contador1 == 2:
        lista[2].append(valor)

    if contador2 >= 3:
        contador2 = 0
        contador1 += 1

deco()
print('{}A matriz ficara:'.format(cores['ciano']))
print(f'[ {lista[0][0]:^5} ] [ {lista[0][1]:^5} ] [ {lista[0][2]:^5} ]')
print(f'[ {lista[1][0]:^5} ] [ {lista[1][1]:^5} ] [ {lista[1][2]:^5} ]')
print(f'[ {lista[2][0]:^5} ] [ {lista[2][1]:^5} ] [ {lista[2][2]:^5} ]')
deco()
