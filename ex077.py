from time import sleep
cores = {'padrao': '\033[m',
         'roxo': '\033[1;35m'}


def deco():
    print('{}-{}'.format(cores['roxo'], cores['padrao'])*60)


deco()
print('{}SEPARADOR DE VOGAIS'.format('\033[1m').center(60))
deco()

lista = ('celular', 'delay', 'computador', 'fone', 'prato', 'fonte', 'praia', 'cachoeira', 'paralelepipedo', 'oculos',
         'capa', 'bau', 'engenheiro', 'universidade', 'programador', 'repetidor', 'controleo', 'console', 'derrota')

vogais = 'AaEeIiOoUu'

for palavras in lista:
    print('A palavra {} temos como vogais: '.format(palavras.upper()), end='')

    for letra in palavras:
        if letra.lower() in 'AaEeIiOoUu':
            print('{}{}{}'.format(cores['roxo'], letra, cores['padrao']), end=' ')
    print()
    sleep(0.3)
deco()
