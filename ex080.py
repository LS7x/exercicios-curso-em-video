
cores = {'padrao': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}


def deco():
    print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)


deco()
print('{}Organizando valores em listas!'.format('\033[1m').center(60))
deco()

lista = []
for valores in range(0, 5):
    numero = int(input('Digite o valor da posição {}ª: '.format(valores)))

    if valores == 0 or numero > lista[-1]:
        lista.append(numero)

    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1

deco()
print('{}Os valores digitados na lista: {}{}'.format(cores['verde'], cores['padrao'], lista))
