from time import sleep
cores = {'padrao': '\033[m',
         'roxo': '\033[1;35m'}

def deco():
    print('{}-{}'.format(cores['roxo'], cores['padrao'])*130)

deco()
print('{}Tabela dos finalistas do CBF'.format('\033[1m').center(130))
print('Campeonato Brasileiro de Futebol!{}'.format(cores['padrao']).center(130))
deco()

lista = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino',
         'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás',
         'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo')

print('{}Os 5º Primeiros colocados são:{}'.format(cores['roxo'], cores['padrao']))
print(lista[:5])
deco()
sleep(0.5)

print('{}Os 4º Ultimos colocados são:{}'.format(cores['roxo'], cores['padrao']))
print(lista[-4:])
deco()
sleep(0.5)

print('{}Times ordenados em ordem alfabética:{}'.format(cores['roxo'], cores['padrao']))
print(sorted(lista[:10]))
print(sorted(lista[-10:]))
deco()
sleep(0.5)

print('{}O time corinthiano se encontra na posição:{} {}ª'
      .format(cores['roxo'], cores['padrao'], lista.index('Corinthians')+1))
deco()
