import moeda
moeda.titulo('Bem vindo a modularização em Python!')

valor = float(input("Digite o preço do produto: R$"))
print(f'A metade de R${valor} será {moeda.metade(valor)} reais.')
print(f'O dobro de R${valor} será {moeda.dobro(valor)} reais.')
print(f'O valor de R${valor} com aumento de 10% será de {moeda.aumentar(valor, 10):.2f} reais')
print(f'O valor de R${valor} com redução de 13% será de {moeda.diminuir(valor, 13):.2f} reais')
moeda.deco()
