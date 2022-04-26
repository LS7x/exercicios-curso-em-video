
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'amarelo': '\033[1;33m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}'*70)


deco()
print(f'{cores["negrito"]}Tratamento de erros, em numeração!'.center(70))
deco()


def leiaInt(valor):
    while True:
        try:
            valor = int(input(valor))

        except KeyboardInterrupt or valor == '':
            print(f'{cores["vermelho"]}Valores estão em branco!{cores["padrao"]}')

        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Os tipos de dados informados não corresponde á um valor inteiro!'
                  f'{cores["padrao"]}')

        else:
            return valor


def leiaFloat(valor):
    while True:
        try:
            valor = float(input(valor).replace(',', '.'))

        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Os tipos de dados informados não corresponde á um valor real!'
                  f'{cores["padrao"]}')

        except KeyboardInterrupt:
            print(f'{cores["vermelho"]}Valores estão em branco!{cores["padrao"]}')

        else:
            return valor


numeroInt = leiaInt('Digite um número inteiro para verificação: ')
numeroFloat = leiaFloat('Digite um número real para verificação: ')

print(f'Você acabou de digitar o número no valor inteiro de {numeroInt}!')
print(f'Você acabou de digitar o número no valor real de {numeroFloat}!')
deco()
