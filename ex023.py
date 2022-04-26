numero = int(input('Digite um número de no maximo 4 casas decimais: '))

'''numeroc = str(numero)
print('A unidade a e que vale á: {}'.format(numeroc[3]))
print('A dezena a e que vale á: {}'.format(numeroc[2]))
print('A centena a e que vale á: {}'.format(numeroc[1]))
print('A milhar a e que vale á: {}'.format(numeroc[0]))'''

# O objeto está como string (Necessita da obrigação dos 4 DIGITOS)
# Não podendo haver menos ou mais digitos!
# Para não exigir a obrigação utilize em valor matematico (INTEIRO)
# E somente faça a conversão do valor adquirindo o resto da divisão!

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('A unidade a e que vale á: {}'.format(unidade))
print('A dezena a e que vale á: {}'.format(dezena))
print('A centena a e que vale á: {}'.format(centena))
print('A milhar a e que vale á: {}'.format(milhar))
