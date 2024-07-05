# Crie um programa que pede 10 nomes porém só imprime a frase, se o nome começar com a letra "A"
nomes = [input(f"Digite o nome {i+1}: ") for i in range(10)]

# Imprime a saudação para nomes que começam com "a"
for nome in nomes:
    if nome and nome[0].lower() == 'a':  # Verifica se o primeiro caractere é "a"
        print(f"Olá, {nome}!")