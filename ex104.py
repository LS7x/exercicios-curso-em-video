
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'amarelo': '\033[1;33m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}'*70)


deco()
print(f'{cores["negrito"]}Resumo de validação de dados em números inteiros!'.center(70))
deco()


def leiaInt(string):
    while True:
        valor = str(input(string))

        if valor.isnumeric():
            valor = int(valor)
            return valor

        else:
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro valido!{cores["padrao"]}')
            deco()


numero = leiaInt('Digite o número para verificação: ')
print(f'Você acabou de digitar o número {numero}')
deco()
