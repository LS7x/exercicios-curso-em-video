
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'ciano': '\033[1;36m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["ciano"]}-{cores["padrao"]}'*80)


deco()
print(f'{cores["negrito"]}Emitindo dados e realizando levantamento dos jogadores de futebol!'.center(80))
deco()

dicionario = dict()
lista = list()
jogadores = list()

while True:
    dicionario.clear()
    lista.clear()

    dicionario['nome'] = str(input('Digite o nome do jogador: ').capitalize())
    partidas = int(input('Digite quantas partidas foram jogadas: '))

    if partidas > 0:
        for quantidade in range(1, partidas + 1):
            while True:
                acertos = int(input(f'Digite quantos gols foram feitos na partida Nª{quantidade}: '))

                if acertos >= 0:
                    lista.append(acertos)
                    break

                else:
                    print(f'{cores["vermelho"]}Valor invalido, tente novamente...{cores["padrao"]}')

    if partidas > 0:
        dicionario['gols'] = lista.copy()

    else:
        dicionario['gols'] = '-----'

    if partidas > 0:
        dicionario['total'] = sum(lista.copy())

    else:
        dicionario['total'] = '-----'

    jogadores.append(dicionario.copy())

    deco()
    while True:
        continuar = str(input('Você deseja continuar [S/N]: ').upper().strip())

        if continuar == 'S' or continuar == 'N':
            break

        else:
            print(f'{cores["vermelho"]}Opção invalida, tente novamente...{cores["padrao"]}')
    deco()

    if continuar == 'N':
        break

print(f'{cores["negrito"]}{"COD":<10} {"NOME":<20} {"GOLS":<20} {"TOTAL":<20}')
deco()

for keys, values in enumerate(jogadores):
    print(f'{cores["negrito"]}{keys + 1:<11}', end='')
    for dado in values.values():
        print(f'{str(dado):<21}', end='')
    print()
deco()

while True:
    while True:
        continuarLevan = str(input('Deseja visualizar os dados dos jogadores [S/N]: ').upper().strip())

        if continuarLevan == 'S' or continuarLevan == 'N':
            break

        else:
            print(f'{cores["vermelho"]}Opção invalida, tente novamente...{cores["padrao"]}')

    if continuarLevan == 'N':
        deco()
        break

    while True:
        levantamento = int(input('Digite o codigo do jogador que deseja visualizar: ')) - 1

        if levantamento < len(jogadores):
            break

        else:
            print(f'{cores["vermelho"]}Valor invalido, tente novamente...{cores["padrao"]}')

    deco()
    print(f'{cores["negrito"]}', end='')
    print(f'    --> Levantamento do jogador {jogadores[levantamento]["nome"]}'.upper())

    for keys, values in enumerate(jogadores[levantamento]["gols"]):
        print(f'         + No jogo {keys + 1} ele(a) fez {values} gols!')
    deco()
