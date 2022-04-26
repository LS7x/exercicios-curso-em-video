nome = str(input('Informe seu nome completo: ')).strip()
print('O nome em maiúsculo é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {}'.format(nome.lower()))

print('A quantidade de letras ao todo (sem considerar espaços): {}'.format(len(nome)-nome.count(' ')))
print('A quantidade de letras somente no primeiro nome é de: {}'.format(nome.find(' ')))
