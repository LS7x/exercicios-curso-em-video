import time

print(('\033[0;36m-\033[m'*60))
print('{}Seja muito bem vindo ao Python Bank!'.format('\033[1;37m'))
print('Iremos fazer o calculo para seu emprestimo bancario :)')
print(('\033[0;36m-\033[m'*60))

casa = float(input('\nQual é o valor da casa: {}R${}'.format('\033[0;32m', '\033[m')))
salario = float(input('Qual é o valor do salario: {}R${}'.format('\033[0;32m', '\033[m')))
anuidade = int(input('Em quantos anos as prestações: '))

mes = anuidade * 12
excesso = salario * 0.30
porcento = casa / mes
print('\nAguarde, calculando emprestimo...')
time.sleep(3)

if porcento <= excesso:
    print('{}Sim, é possivel aprovar o emprestimo!{}'.format('\033[0;32m', '\033[m'))
    print('As parcelas ficaram no total de R${:.2f} por {} Meses'.format(porcento, mes))

else:
    print('{}Infelizmente não é possivel aprovar o emprestimo!{}'.format('\033[0;31m', '\033[m'))
    print('O valor de R${:.2f} por {} meses, sai fora dos nossos padroes'.format(porcento, mes))
