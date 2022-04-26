nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(nome.split()[0]))

nome = nome.split()
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
