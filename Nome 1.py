# Crie um programa que pede 10 nomes e imprime a frase "Olá, fulano!"

nomes = [input(f"Digite o nome {i+1}: ") for i in range (10)]

for nome in nomes:
    print(f"Olá, {nomes}!")