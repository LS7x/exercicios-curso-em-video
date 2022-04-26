from time import sleep
cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m'}

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('{}Seja bem-vindo a calculadora Python'.format('\033[1m').center(60))
print('Desta vez vamos as compras no mercado!{}'.format(cores['padrao']).center(60))
print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

print('{}Siga as instruções a seguir:{}'.format('\033[1m', cores['padrao']))
print('Informe o nome do produto!'
      '\nInforme um preço valido igual ou acima de 50 centavos!(RS0.5)\n'
      '\nPara continuar digite:'
      '\n[S] Sim, para continuar'
      '\n[N] Não, para parar.')

contador = menorValor = produtoCaro = valorTotal = 0
produtoMenor = ''

while True:

    print('{}-{}'.format(cores['amarelo'], cores['padrao']) * 60)
    nome = str(input('Digite o nome do produto: '))

    # Efetuar um looping caso valor seja invalido menor que R$0.50 ou menor que 50 centavos!
    valor = 0
    while valor < 0.5:
        valor = float(input('Digite o valor do produto: R$'))

    # Efetuar um looping caso valor seja invalido para continuar [S/N]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a lista?: ').strip().upper())

    valorTotal += valor
    contador += 1

    if valor > 1000:
        produtoCaro += 1

    if contador == 1 or valor < menorValor:
        menorValor = valor
        produtoMenor = nome

    if continuar == 'N':
        break

print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)
print('Aguarde, calculando...\n')
sleep(3)
print('{}Total da compra saira entorno de R${:.2f}'.format(cores['amarelo'], valorTotal))
print(f'{produtoCaro} produtos estão custando valor superior á R$1.000')
print('Produto mais barato foi {} que custa R${}{}'.format(produtoMenor, menorValor, cores['padrao']))
