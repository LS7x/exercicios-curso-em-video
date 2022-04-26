
cores = {'padrao': '\033[m',
         'ciano': '\033[1;36m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Selecionador de valores em listas!'.format('\033[1m').center(60))
deco()

lista = []
contador = 1
continuar = ' '


lista.append(int(input('Digite o {}ª valor: '.format(contador))))
print('{}Valor adicionado com sucesso!{}'.format(cores['verde'], cores['padrao']))
contador += 1

while continuar not in 'SN':
    continuar = str(input('Deseja continuar [S/N]: ').strip().upper())

    if continuar == 'N':
        deco()
        break

    if continuar == 'S':
        deco()
        while True:
            numero = int(input('Digite o {}ª valor: '.format(contador)))
            contador += 1

            if numero not in lista:
                lista.append(numero)
                print('{}Valor adicionado com sucesso!{}'.format(cores['verde'], cores['padrao']))

            else:
                print('{}Este valor esta duplicado! Não sera adicionado.{}'.format(cores['vermelho'], cores['padrao']))
                contador -= 1
            break

    continuar = ' '

print('{}Os valores digitados na lista foram:{} {}'.format(cores['ciano'], cores['padrao'], sorted(lista)))
