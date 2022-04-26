from time import sleep
cores = {'padrao':'\033[m',
         'roxo':'\033[1;35m'}

print('{}-{}'.format(cores['roxo'], cores['padrao'])*50)
print('{}Bem vindo a calculadora Python!'.format('\033[1m').center(50))
print('Vamos somar os números em que você digitar.{}'.format(cores['padrao']))
print('{}-{}'.format(cores['roxo'], cores['padrao'])*50)

valor = 0
contador = 0
resultado = 0


while valor != 999:
    print('{}\nPara finalizar a soma digite [999]!{}'.format('\033[1m', cores['padrao']))
    valor = int(input('Digite o numero que deseja somar: '))
    contador += 1
    resultado += valor

    if valor == 999:
        contador -= 1
        resultado -= 999

print('\nAguarde, calculando e finalizando...')
sleep(3)

print('{}Você digitou {} números e a soma entre eles é de {}{}'
      .format(cores['roxo'], contador, resultado, cores['padrao']))
print('{}-{}'.format(cores['roxo'], cores['padrao'])*50)
