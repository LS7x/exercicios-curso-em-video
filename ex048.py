cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 330)
print('{}Esta sera uma lista de numeros impares!'
      '\nQue são múltiplos de três no intervalo de 1 a 500{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 330)

print('Valores aseguir:', end="")
soma = 0
contador = 0
for numeros in range(1, 500 + 1, 2):
    if numeros % 3 == 0:
        contador += 1 # (Contador = contador + 1) Ou (Contador += 1)
        soma = soma + numeros
        print(' {}'.format(numeros), end="")

print()
print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 330)

print('{}A soma entre os {} números impares divisiveis por 3 é de {}!{}'
      .format(cores['amarelo'], contador, soma, cores['padrao']))

print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 330)
