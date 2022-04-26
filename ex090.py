
cores = {'padrao': '\033[m', 'amarelo': '\033[1;33m', 'verde': '\033[1;32m', 'padraoN': '\033[1m',
         'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}'*60)


deco()
print('{}Informações através de bibliotecas!'.format('\033[1m').center(60))
deco()

dicionario = dict()

dicionario['nome'] = str(input('Digite o seu nome: '))
dicionario['média'] = float(input('Digite sua média: '))

if dicionario['média'] >= 7:
    dicionario['situação'] = f'{cores["verde"]}aprovado'

elif dicionario['média'] < 7:
    dicionario['situação'] = f'{cores["vermelho"]}reprovado'

deco()
print(f'{cores["padraoN"]}O nome do aluno(a) é {dicionario["nome"]}')
print(f'A média do aluno(a) é {dicionario["média"]}')
print(f'A situação do aluno(a) é {dicionario["situação"]}{cores["padrao"]}')
deco()
