from time import sleep

cores = {'padrao':'\033[m',
         'amarelo':'\033[1;33m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*70)

print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(70))
print('Desta vez iremos calcular a progressão arentimetica de 10 termos.{}'.format(cores['padrao']))

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*70)

termo = int(input('Digite o valor do 1º termo: '))
razao = int(input('Digite o valor da razão: '))

print('Aguarde, calculando...\n')

decimo = termo + (10 - 1) * razao

for pa in range(termo, decimo + razao, razao):
    print('{}'.format(pa), end=' -> ')
    sleep(0.3)
print('ACABOU')
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*70)
