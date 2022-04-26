
cores = {'padrao': '\033[m', 'amarelo': '\033[1;33m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}


def deco():
    print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)


deco()
print('{}Validando expressões matematicas!'.format('\033[1m').center(65))
deco()

contador = 0
expressao = input('Digite a sua expressão: ')
# ---------------------------------------------------------------------------------------
for numero in expressao:
    if numero == '(':
        contador += 1

    elif numero == ')':
        if contador > 0:
            contador -= 1

        else:
            contador += 1

if contador == 0:
    print('{}Essa expressão é valida!{}'.format(cores['verde'], cores['padrao']))

else:
    print('{}Essa expressão é invalida!{}'.format(cores['vermelho'], cores['padrao']))

# ---------------------------------------------------------------------------------------
# Expressão proposta pelo professor:

'''lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')

    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()

        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('{}Essa expressão é valida!{}'.format(cores['verde'], cores['padrao']))

else:
    print('{}Essa expressão é invalida!{}'.format(cores['vermelho'], cores['padrao']))'''
# ---------------------------------------------------------------------------------------
