
cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m'}


def deco():
    print('{}-{}'.format(cores['amarelo'], cores['padrao'])*70)


deco()
print('{}Seja bem vindo ao leitor de tuplas'.format('\033[1m').center(70))
print('Informe alguns números e iremos trazer informações a respeito dele!{}'.format(cores['padrao']).center(70))
deco()

tupla = (int(input('Informe o 1ª valor:')),
         int(input('Informe o 2ª valor:')),
         int(input('Informe o 3ª valor:')),
         int(input('Informe o 4ª valor:')))
deco()
print('{}O número nove apareceu {} vezes{}'.format(cores['amarelo'], tupla.count(9), cores['padrao']))
deco()

if 3 in tupla:
    print('{}O primeiro número 3 apareceu na posição {}ª{}'.format(cores['amarelo'], tupla.index(3)+1, cores['padrao']))

else:
    print('{}O número 3 não foi digitado{}'.format(cores['vermelho'], cores['padrao']))

deco()
print('{}Os números pares digitados foram:'.format(cores['amarelo'], cores['padrao']), end=' ')

for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')

print()
deco()
