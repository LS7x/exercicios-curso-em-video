import moeda
moeda.titulo('Bem vindo a modularização em Python!')

valor = float(input("Digite o preço do produto: R$"))
print(f'A metade de {moeda.moeda(valor)} será {moeda.metade(valor, True)}.')
print(f'O dobro de {moeda.moeda(valor)} será {moeda.dobro(valor, True)}.')
print(f'O valor de {moeda.moeda(valor)} com aumento de 10% será de {moeda.aumentar(valor, 10, True)}.')
print(f'O valor de {moeda.moeda(valor)} com redução de 13% será de {moeda.diminuir(valor, 13, True)}.')
moeda.deco()
