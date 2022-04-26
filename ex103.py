
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m'}


def deco():
    print(f'{cores["verde"]}-{cores["padrao"]}'*80)


deco()
print(f'{cores["negrito"]}Demonstração de uma ficha de jogador de futebol, utilizando funções!'.center(80))
deco()


def ficha(name='DESCONHECIDO', valores=0):
    print(f'O jogador {name} fez {valores} gol(s) no campeonato!')


nome = str(input('Digite o nome do jogador: ').strip())
gols = str(input('Digite a quantidade de gols: '))
deco()
# --------------------------------------------------------------------
# Verificando se o a string gols é um numeral!
if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0
# --------------------------------------------------------------------
# Verificando se a string nome esta vazia, se não, não enviamos!
if nome == '':
    ficha(valores=gols)

else:
    ficha(nome, gols)
# --------------------------------------------------------------------
deco()
