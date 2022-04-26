km = int(input('Insira quantos KM foram percorridos: '))
dias = float(input('Insira por quantos dias foram alugados: '))
valor = (km * 0.15) + (dias * 60)
print('O valor total a pagar é de: R${:.2f}'.format(valor))
