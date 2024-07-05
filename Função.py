def maior_numero_v2():
    numeros = input("Digite uma lista de números separada por espaço: ")
    
    listaNumeros = numeros.split(" ")
        
    listaNumerosFinal = []
    for numero in listaNumeros:
        listaNumerosFinal.append(float(numero))
        
    maior = listaNumerosFinal[0]
    for numero in listaNumerosFinal:
        if numero > maior:
            maior = numero
            
    return maior
maior_numero_v2