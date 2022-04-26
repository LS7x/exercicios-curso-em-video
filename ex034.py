import math
import time

salario = float(input('\nDigite o valor do salario: R$'))
aumento = salario

if salario > 1250.00:
    aumento = salario * 1.10

if salario <= 1250.00:
    aumento = salario * 1.15

print('\nAguarde processando aumento...')
time.sleep(3)
print('O aumento do salario ficara em R${:.2f}'. format(aumento))
