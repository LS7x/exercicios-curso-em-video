n1 = float(input('\nDigite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
n3 = float(input('Digite o 3º numero: '))

# Verificando o menor valor:

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('\nO numero com menor valor é: {}'.format(menor))

# Verificando o maior valor:

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O numero com maior valor é: {}'.format(maior))
