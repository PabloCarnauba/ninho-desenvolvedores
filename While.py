# Imprimir na tela os números de 0 a 500
numero = 0
while numero <= 500:
    print(numero)
    numero += 1

# Imprimir na tela somente os pares de 0 a 500
numero = 0
while numero <= 500:
    if (numero % 2)==0:
        print(numero)
    numero += 1

# Imprimir a soma dos números de 0 a 500
soma = 0
numero = 0

while numero <= 500:
    soma += numero
    numero += 1
print("A soma dos números de 0 a 500 é:", soma)