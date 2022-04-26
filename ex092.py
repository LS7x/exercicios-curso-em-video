import datetime
from time import sleep
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'ciano': '\033[1;36m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["ciano"]}-{cores["padrao"]}'*80)


deco()
print(f'{cores["negrito"]}Bem vindo a previdencia social!'.center(80))
deco()

dicionario = dict()
yearToday = datetime.date.today().year

dicionario['nome'] = str(input('Digite o seu nome: '))

while True:
    nascimento = int(input('Digite o seu ano de nascimento: '))

    if nascimento > 1910:
        break

    else:
        print(f'{cores["vermelho"]}Ano de nascimento invalido!{cores["padrao"]}')

idade = yearToday - nascimento
dicionario['idade'] = idade

ctps = ' '
while ctps not in 'NS':
    ctps = str(input('Você possui CTPS? (Carteira de Trabalho e Previdência Social)[S/N]: ').upper().strip())

    if ctps == 'N':
        break

if ctps == 'N':
    dicionario['CTPS'] = 'não possui'

else:
    dicionario['CTPS'] = int(input('Digite sua CTPS (Carteira de Trabalho e Previdência Social): '))
    while True:
        contribuicao = int(input('Digite o ano de contratação: '))

        if contribuicao > nascimento + 10:
            break

        else:
            print(f'{cores["vermelho"]}Ano de contratação invalido!{cores["padrao"]}')

    dicionario['salário'] = float(input('Digite o seu salário: R$'))
    dicionario['ano de contratação'] = contribuicao

    aposentadoria = 35 - (yearToday - contribuicao)
    idadeAposentadoria = idade + aposentadoria

    dicionario['aposentadoria'] = f'{idadeAposentadoria} anos'
deco()

for keys, values in dicionario.items():
    sleep(1)
    print(f'    -{cores["negrito"]} {keys} é {values}'.capitalize())

# ---------------------------------------------------------------------------------------
# Metodo não utilizando todas as funcões da biblioteca porem mais organziado!
'''print(f'{cores["negrito"]}O seu nome é {dicionario["nome"]}!')
sleep(1)
print(f'Você tem {dicionario["idade"]} anos de idade!')
sleep(1)
print(f'A sua CTPS é {dicionario["CTPS"]}!')
sleep(1)
print(f'O seu salário é {dicionario["salário"]:.2f}!')
sleep(1)
print(f'O seu ano de contratação é {dicionario["ano de contratação"]}')
sleep(1)
print(f'A sua aposentadoria sera com {dicionario["aposentadoria"]} anos de idade!')'''
# ---------------------------------------------------------------------------------------
deco()
