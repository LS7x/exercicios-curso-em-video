cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m',
         'amarelo': '\033[1;33m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["verde"]}-{cores["padrao"]}'*70)


deco()
print(f'{cores["negrito"]}Eligibilidade de votos utilizando funções!'.center(70))
deco()


def voto(ano):
    from datetime import datetime
    day = datetime.today().year

    idade = day-ano

    if idade < 0:
        idade = 0

    print(f'Com idade de {idade} anos seu voto se torna: ', end='')

    if 18 <= idade < 70:
        return f'{cores["verde"]}OBRIGATORIO!{cores["padrao"]}'

    elif 16 <= idade < 18 or idade >= 70:
        return f'{cores["amarelo"]}OPCIONAL!{cores["padrao"]}'

    else:
        return f'{cores["vermelho"]}NEGADO!{cores["padrao"]}'


escolha = voto(int(input('Digite o ano de nascimento: ')))
print(escolha)
deco()
