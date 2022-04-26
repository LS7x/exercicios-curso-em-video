import moeda
moeda.titulo('Bem vindo a modularização em Python!')

valor = float(input("Digite o preço do produto: R$"))
print(f'A metade de {moeda.moeda(valor)} será {moeda.moeda(moeda.metade(valor))}.')
print(f'O dobro de {moeda.moeda(valor)} será {moeda.moeda(moeda.dobro(valor))}.')
print(f'O valor de {moeda.moeda(valor)} com aumento de 10% será de {moeda.moeda(moeda.aumentar(valor, 10))}.')
print(f'O valor de {moeda.moeda(valor)} com redução de 13% será de {moeda.moeda(moeda.diminuir(valor, 13))}.')
moeda.deco()
