
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'amarelo': '\033[1;33m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}'*60)


deco()
print(f'{cores["negrito"]}Informando dados atraves de bibliotecas em listas!'.center(60))
deco()

dicionario = dict()
lista = list()
soma = media = 0

while True:
    dicionario['nome'] = str(input('Digite o nome da pessoa: '))

    while True:
        dicionario['sexo'] = str(input('Digite o sexo da pessoa [M/F]: ').strip().upper())

        if dicionario['sexo'] == 'M' or dicionario['sexo'] == 'F':
            break

        else:
            print(f'{cores["vermelho"]}Valor invalido, tente novamente...{cores["padrao"]}')

    while True:
        dicionario['idade'] = int(input('Digite a idade da pessoa: '))

        if dicionario['idade'] > 0:
            soma += dicionario['idade']
            break

        else:
            print(f'{cores["vermelho"]}Idade invalida, tente novamente...{cores["padrao"]}')
    deco()

    while True:
        continuar = str(input('Você deseja continuar [S/N]: ').strip().upper())

        if continuar == 'S' or continuar == 'N':
            break

        else:
            print(f'{cores["vermelho"]}Valor invalido, tente novamente...{cores["padrao"]}')
    deco()
    lista.append(dicionario.copy())

    if continuar == 'N':
        break

media = soma / len(lista)
print(f'{cores["negrito"]}      --> O grupo possue {len(lista)} pessoas!')
print(f'      --> A média de idades no grupo é de {media:.0f} anos!')
print(f'      --> As mulheres cadastradas foram:', end=' ')

for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], '-->', end=' ')
print(f'{cores["vermelho"]}Acabou{cores["padrao"]}')

print(f'{cores["negrito"]}      --> Lista de pessoas que estão acima da média!')

for pessoa in lista:
    if pessoa['idade'] >= media:
        print(f'{cores["amarelo"]}            + Nome: {pessoa["nome"]} | Sexo: '
              f'{pessoa["sexo"]} | Idade: {pessoa["idade"]}{cores["padrao"]}')
deco()
