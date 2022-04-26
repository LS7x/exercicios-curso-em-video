from time import sleep

cores = {'padrao':'\033[m',
         'roxo':'\033[35m'}

print('{}-{}'.format(cores['roxo'], cores['padrao'])*70)
print('{}Seja bem-vindo a calculadora Python!'.format('\033[1m').center(70))
print('Desta vez iremos somar seis numeros seu! Mas apenas os numeros pares.'
      '\nMas fique avontade para digitar qualquer numero, eu irei organizar!{}'.format(cores['padrao']))
print('{}-{}'.format(cores['roxo'], cores['padrao'])*70)

soma = 0
contador = 0

for valor in range(1, 6 + 1):
    numeros = int(input('Digite o {}º numero inteiro: '.format(valor)))
    if numeros % 2 == 0:
        contador += 1
        soma = soma + numeros

print('Aguarde, organizando...\n')
sleep(3)

print('{}Você informou {} numeros pares!{}'.format(cores['roxo'], contador, cores['padrao']))
print('{}E a soma de todos os valores pares serão de {}!{}'.format(cores['roxo'], soma, cores['padrao']))
