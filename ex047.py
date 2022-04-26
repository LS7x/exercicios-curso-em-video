
cores = {'padrao':'\033[m',
         'ciano':'\033[1;36m'}

print('{}-{}'.format(cores['ciano'], cores['padrao'])*100)
print('{}Está é uma lista de todos os numeros pares até 50!'.format('\033[1m'))
print('Os numeros são:{}'.format(cores['padrao']), end="")

# Posso utilizar a função if para calcular os numeros pares!
# Caso 'Numeros' Seja divisivel por 2 ele é par

'''for numeros in range(1, 50+1):
    if numeros % 2 == 0:
        print(' {}'.format(numeros), end="")'''

# Modelo logico que funciona tambem!
for numeros in range(2, 50+1, 2):
    print(' {}'.format(numeros), end="")

print()
print('{}-{}'.format(cores['ciano'], cores['padrao'])*100)
