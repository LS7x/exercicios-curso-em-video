
cores = {'padrao':'\033[m',
         'amarelo':'\033[1;33m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(60))
print('Dessa vez iremos verificar a sequência de Fibonacci{}'.format(cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

quantidade = int(input('Digite a quantidade de termos que desejar visualizar: '))

ultimoValor = 0
penultimoValor = 1
termo = 1

print('{}'.format(ultimoValor), end=' -> ')
contador = 2

while contador <= quantidade:
    termo = ultimoValor + penultimoValor
    print('{}'.format(termo), end=' -> ')
    contador += 1

    penultimoValor = ultimoValor
    ultimoValor = termo

print('{}FIM{}'.format(cores['amarelo'], cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
