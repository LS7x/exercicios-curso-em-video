from random import randint
from time import sleep
from operator import itemgetter

cores = {'padrao': '\033[m', 'ciano': '\033[1;36m', 'negrito': '\033[1m'}


def deco():
    print(f'{cores["ciano"]}-{cores["padrao"]}'*60)


deco()
print(f'{cores["negrito"]}Sorteador de posições automatico!{cores["padrao"]}'.center(60))
deco()

print('Você esta preparado? Então vamos começar!')
deco()
print(f'{cores["negrito"]}Valores sorteados:')

dicionario = {'Jogador 1': randint(1, 6),
              'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6),
              'Jogador 4': randint(1, 6)}

for keys, values in dicionario.items():
    sleep(1)
    print(f'    O {keys}ª tirou {values} no dado!')
deco()

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse= True)
print(f'{cores["negrito"]}A ordem correta de incio sera:')

for posicao, valor in enumerate(ranking):
    sleep(1)
    print(f'    {posicao+1}ª Lugar: {valor[0]} com {valor[1]} pontos!')

deco()
