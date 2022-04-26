from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipo = (co ** 2) + (ca ** 2)
print('O comprimento da hipotenusa é de: {:.2f}'. format(sqrt(hipo)))
