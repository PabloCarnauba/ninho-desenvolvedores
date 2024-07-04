# Questão 01) Palíndromo:
# Descrição: Crie uma função chamada Epalindromo que peça ao usuário para digitar
# Uma string e retorne True se a string for um palíndromo e False caso contrário.
# Exemplo: Se o usuário digitar "radar", a função deve retornar True.

def palindromo():
    palavra = input("Digite uma palavra: ")
    
    if palavra == palavra[::-1]:
        return print("Verdadeiro")
    else:
        return print("Falso")
    
palindromo()

# Questão 02) Máximo de uma lista:
# Descrição: Crie uma função chamada maximo que peça ao usuário para 
# Digitar uma lista de números (separados por espaços) e retorne o maior número.
# Exemplo: Se o usuário digitar 1 3 2 5 4, a função deve retornar 5.

def maiorNumero():
    numeros = input("Digite uma lista de números separada por espaço: ")
    
    listaNumeros = numeros.split(" ")
        
    listaNumerosFinal = []
    for numero in listaNumeros:
        listaNumerosFinal.append(int(numero))
        
    maior = listaNumerosFinal[0]
    for numero in listaNumerosFinal:
        if numero > maior:
            maior = numero
            
    return print(maior)

maiorNumero()

# Questão 03) Calcular a média:
# Descrição: Crie uma função chamada media que peça ao usuário para digitar 
# Uma lista de números (separados por espaços) e retorne a média dos números.
# Exemplo: Se o usuário digitar 1 2 3 4 5, a função deve retornar 3.

def mediaNumero():
    numeros = input("Digite uma lista de números separada por espaço: ")
    
    listaNumeros = numeros.split(" ")
        
    listaNumerosFinal = []
    for numero in listaNumeros:
        listaNumerosFinal.append(float(numero))
        
    media = sum(listaNumerosFinal) / len(listaNumerosFinal)
    
    return print(media)

mediaNumero()

# Questao 04) Contar caracteres:
# Descrição: Crie uma função chamada contarCaracteres que peça ao usuário para digitar 
# Uma string e retorne um dicionário com a contagem de cada caractere na string.
# Exemplo: Se o usuário digitar "hello", a função deve retornar {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

def ContarCaracteres():
    
    letra = input("Digite uma palavra: ")    
    letraDicionario = {}
    
    for letra in letra:
        if letra in letraDicionario:
            letraDicionario[letra] += 1
        else:
            letraDicionario[letra] = 1
            
    return print(letraDicionario)

ContarCaracteres()