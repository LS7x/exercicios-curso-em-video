from time import sleep
cores = {'padrao': '\033[m',
         'roxo': '\033[1;35m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

print('{}-{}'.format(cores['azul'], cores['padrao'])*65)
print('{}Bem-vindo ao Python Bank'.format('\033[1m').center(65))
print('Este caixa esta funcionando somente para saque!{}'.format(cores['padrao']).center(65))
print('{}-{}'.format(cores['azul'], cores['padrao'])*65)

print('{}Este caixa possue somente notas nos valores asseguir:'.format(cores['azul']).center(70))
print('R$ 50, R$20, RS10 e R$1{}'.format(cores['padrao']).center(65))
print('{}-{}'.format(cores['azul'], cores['padrao'])*65)

valor = 0

while valor <= 0:
    valor = int(input('Digite o valor do saque: '))

# Resolvido para retirada de 50!
cinquenta = int(valor / 50)
valor -= (cinquenta * 50)

# Resolvido para retirada de 20!
vinte = int(valor / 20)
valor -= (vinte * 20)

# Resolvido para retirada de 10!
dez = int(valor / 10)
valor -= (dez * 10)

# Resolvido para retirada de 1!
um = valor

# Segredo, divide o valor do saque pelo valor da nota! utilizando o int para não ocorrer valor float
# Gerando o valor de quantas notas serão utlizados na str!

# Depois multiplica a (str da nota)!!! e o valor da nota em si, e subtrai pelo valor trazendo o restante da divisão!

print('Aguarde, calculando valores...')
sleep(2)

print('{}-{}'.format(cores['azul'], cores['padrao'])*65)
print('{}Asseguir o total de celulas que serão liberadas:'.format(cores ['azul']))
sleep(0.5)
print(f'Celulas nos valores de R$50: {cinquenta}')
sleep(0.5)
print(f'Celulas nos valores de R$20: {vinte}')
sleep(0.5)
print(f'Celulas nos valores de R$10: {dez}')
sleep(0.5)
print(f'Celulas nos valores de R$1: {um}')
print('{}-{}'.format(cores['azul'], cores['padrao'])*65)

print('{}Volte sempre!{}'.format(cores['verde'], cores['padrao']))
