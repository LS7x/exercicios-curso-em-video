
cores = {'padrao': '\033[m', 'roxo': '\033[1;35m'}


def deco():
    print('{}-{}'.format(cores['roxo'], cores['padrao'])*60)


deco()
print('{}Leitura de nome e peso, utilizando listas!'.format('\033[1m').center(60))
deco()

print('{}Algumas informações a respeito:'.format('\033[1m'))
print('{}(Não é necessario colocar a unidade de medida){}'.format(cores['roxo'], cores['padrao']))
deco()

lista = []
dados = []
contador = 1
pesoMax = 0
pesoMin = 0

while True:
    dados.append(str(input('Digite o nome da {}ª pessoa: '.format(contador))))
    dados.append(float(input('Digite o peso da {}ª pessoa em KG: '.format(contador))))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ').upper().strip())

        if continuar == 'N':
            deco()
            break

        elif continuar == 'S':
            deco()

    if len(lista) == 0:
        pesoMax = dados[1]
        pesoMin = dados[1]

    else:
        if dados[1] > pesoMax:
            pesoMax = dados[1]

        if dados[1] < pesoMin:
            pesoMin = dados[1]

    contador += 1
    lista.append(dados[:])
    dados.clear()
    if continuar == 'N':
        break

print('{}Foram cadastrados {} pessoas!'.format(cores['roxo'], len(lista)))
print('A pessoa mais pesada foi', end=' ')
for pessoa in lista:
    if pessoa[1] == pesoMax:
        print(f'{pessoa[0]}', end=' e ')
print(f'com o peso de {pesoMax}Kg')

print('A pessoa mais leve foi', end=' ')
for pessoa in lista:
    if pessoa[1] == pesoMin:
        print(f'{pessoa[0]}', end=' e ')
print(f'com o peso de {pesoMin}Kg')
