from time import sleep

cores = {'padrao':'\033[m',
         'ciano':'\033[36m'}

print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)
print('{}Seja bem-vindo a calculadora Python!'
      '\nDesta vez iremos verificar uma tabuada a sua escolha!{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)

valor = int(input('Digite o numero da tabuada a sua escolha: '))

print('\n{}A tabuada de {} é:{}'.format(cores['ciano'], valor, cores['padrao']))

for tabuada in range(1, 10 + 1):
    resultado = tabuada * valor
    sleep(0.5)
    print('{} x {} = {}'.format(tabuada, valor, resultado))

print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)
