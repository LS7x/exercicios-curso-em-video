
cores = {'padrao': '\033[m', 'roxo': '\033[1;35m'}


def deco():
    print('{}-{}'.format(cores['roxo'], cores['padrao'])*70)


deco()
print('{}Elaborando Matrizes apartir da utilização de listas compostas!'.format('\033[1m').center(70))
print('Revelando algumas informações a respeito da matriz'.center(70))
deco()

contador1 = 0
contador2 = 0
pares = 0
maior = 0
lista = [[], [], []]

for numero in range(1, 9 + 1):
    valor = int(input(f'Digite o valor para posição [{contador1}, {contador2}]:'))
    contador2 += 1

    if valor % 2 == 0:
        pares += valor

    if contador1 == 0:
        lista[0].append(valor)

    elif contador1 == 1:
        lista[1].append(valor)

        if valor > maior:
            maior = valor

    elif contador1 == 2:
        lista[2].append(valor)

    if contador2 > 2:
        contador2 = 0
        contador1 += 1

deco()
print('{}A matriz ficara:{}'.format(cores['roxo'], cores['padrao']))
for linha in range(0, 3):
    for digito in range(0, 3):
        print(f'[ {lista[linha][digito]:3^} ]', end='')
    print()
deco()

print('{}A soma dos valores pares na matrix sera de {}'.format(cores['roxo'], pares))

somaColunas = lista[0][2] + lista[1][2] + lista[2][2]
print('A soma dos valores da 3ª coluna sera de {}'.format(somaColunas))

print(f'O maior valor da 2ª linha é de {maior}')
deco()
