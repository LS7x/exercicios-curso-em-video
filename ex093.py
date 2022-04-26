
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'roxo': '\033[1;35m'}


def deco():
    print(f'{cores["roxo"]}-{cores["padrao"]}'*60)


deco()
print(f'{cores["negrito"]}Estatísticas de um jogador de futebol!'.center(60))
deco()

dicionario = dict()
lista = list()
total = 0

dicionario['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite quantas partidas ele jogou: '))

for gols in range(1, partidas + 1):
    acertos = int(input(f'Digite quantos gols foram feitos na partida Nª {gols}: '))
    lista.append(acertos)
    total = total + acertos
    # Poderia somar atraves de: dicionario['total] = sum(lista)

dicionario['gols'] = lista
dicionario['total'] = total
deco()

for keys, values in dicionario.items():
    print(f'{cores["negrito"]}O campo {keys} tem o valor {values}')
deco()

print(f'{cores["negrito"]}O jogador {dicionario["nome"]} jogou {partidas} partidas!')
for indice, valor in enumerate(dicionario['gols']):
    print(f'     --> Na partida Nª {indice + 1} ele fez {valor} gols!')
print(f'Foi realizado um total de {dicionario["total"]} gols!')
deco()
