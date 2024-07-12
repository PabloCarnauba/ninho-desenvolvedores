def vogais():

    for i in range(4):
        palavra = input("Digite uma palavra: ")
        contador = 0
        listaPalavra = []
    
# Verificação das vogais:
        for letra in palavra:
            if letra.lower() in ("a", "e", "i", "o", "u"):
                contador+=1
                listaPalavra.append(palavra)
        print(f"A palavra {palavra} possuí {contador} vogais")
vogais()