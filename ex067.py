
cores = {'padrao':'\033[m',
         'verde':'\033[1;32m'}

print('{}-{}'.format(cores['verde'], cores['padrao'])*60)
print('{}Bem-vindo a tabuada do Python!'.format('\033[1m').center(60))
print('{}-{}'.format(cores['verde'], cores['padrao'])*60)

while True:
    print('{}Lembre-se para finalizar a tabuada digite um valor negativo!{}'.format('\033[1m', cores['padrao']))
    valor = int(input('Digite o numero da tabuada: '))
    print('{}-{}'.format(cores['verde'], cores['padrao']) * 60)

    if valor < 0:
        print('{}Tabuada finalizada!{}'.format(cores['verde'], cores['padrao']))
        break

    print('{}Tabuada de {}{}'.format(cores['verde'], valor, cores['padrao']))

    for tabuada in range (1, 10 + 1):
        resultado = valor * tabuada
        print(f'{valor} x {tabuada} = {resultado}')
    print('{}-{}'.format(cores['verde'], cores['padrao']) * 60)
