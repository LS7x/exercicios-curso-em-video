
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m'}


def deco(escreva):
    print(f'{cores["verde"]}-{cores["negrito"]}' * (len(escreva) + 10))
    print(escreva.center(len(escreva)+10))
    print(f'{cores["verde"]}-{cores["padrao"]}' * (len(escreva) + 10))


while True:
    deco(str(input('O que você deseja escrever: ')))
