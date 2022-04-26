from PythonExercicios.ex110 import moeda
moeda.titulo('Bem vindo a modularização em Python!')

valor = float(input("Digite o preço do produto: R$"))
moeda.resumo(valor, 80, 35, True)
