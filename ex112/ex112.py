from PythonExercicios.utilidadesCeV import moeda, dado

moeda.titulo('Bem vindo a modularização em Python!')

valor = dado.leiaDinheiro("Digite o preço do produto: R$")
moeda.resumo(valor, 80, 35, True)
