
cores = {'padrao':'\033[m',
         'amarelo':'\033[1;33m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('{}Bem vindo a calculadora Python!'.format('\033[1m').center(60))
print('Vamos somar os números em que você digitar.{}'.format(cores['padrao']).center(60))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

contador = soma = 0

while True:
    print('{}Caso deseja finalizar a soma digite [999]{}'.format('\033[1m', cores['padrao']))
    valor = int(input('Digite um número: '))
    print()
    if valor == 999:
        break

    contador += 1
    soma += valor

print('{}Você digitou {} números e a soma entre todos eles é de {}{}'
      .format(cores['amarelo'], contador, soma, cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
