
cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'amarelo': '\033[1;33m'}


def deco():
    print(f'{cores["amarelo"]}-{cores["padrao"]}'*70)


deco()
print(f'{cores["negrito"]}Calculando a área de um terreno atraves de funções!'.center(70))
deco()


def area(lar, comp):
    total = lar * comp
    print(f'A área do terreno com proporções de {lar:.2f} x {comp:.2f} é de {total:.2f}m².')
    deco()


area(float(input('Digite a largura em M²: ')), float(input('Digite o comprimento em M²: ')))
