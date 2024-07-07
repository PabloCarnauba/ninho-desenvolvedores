# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
valor1 = float(input("Digite o valor 1:\n"))
valor2 = float(input("Digite o valor 2:\n"))
valor3 = float(input("Digite o valor 3:\n"))

soma = valor1 + valor2

if soma < valor3:
    print("A soma do 1° e 2° valor é menor que o 3° valor")
elif soma > valor3:
    print("A soma do 1° e 2° valor é maior que o 3° valor")
    
# Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.
valor = int(input("Digite o número:\n"))

if (valor % 2)==0:
    print("O número é par")
else:
    print("O número é impar")

# Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá somar os dois, caso contrário multiplique
# A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.
A = int(input("Digite o valor de A:\n"))
B = int(input("Digite o valor de B:\n"))

if A == B:
    C = A + B

else:
    C = A * B

print("O resultado é:", C)

# Escreva um algoritmo que leia três valores inteiros
# e diferentes e mostre-os em ordem decrescente.
A = int(input("Digite o primeiro valor inteiro:\n"))
B = int(input("Digite o segundo valor inteiro:\n"))
C = int(input("Digite o terceiro valor inteiro:\n"))

if A != B and A != C and B != C:
    maior = A
    if B > maior:
        maior = B
    if C > maior:
        maior = C

    menor = A
    if B < menor:
        menor = B
    if C < menor:
        menor = C

    meio = (A + B + C) - maior - menor

    print("Valores em ordem decrescente:", maior, meio, menor)
else:
    print("Os valores devem ser diferentes.")

# Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o 
# semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado 
# (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9)
somaNotas = 0
qtdNotas = 0

for i in range(3):
    nota = float(input(f"Digite a nota {i+1}:\n"))
    if nota >= 0 and nota <= 10:
        somaNotas += nota
        qtdNotas += 1
    else:
        print("Nota inválida")

media = somaNotas / qtdNotas

if media >=7 and media <=10:
    print(f"Sua média foi: {media:.2f}, você foi Aprovado!")
elif media <7 and media >=5:
    print(f"Sua média foi: {media:.2f}, você ficou de Recuperação!")
elif media <5 and media >=0:
    print(f"Sua média foi: {media:.2f}, você foi Reprovado!")
    
# Calcule a tabuada do 13
tabuada_13 = {}

for i in range(1, 11):
    tabuada_13[i] = 13 * i

for i in tabuada_13:
    print(f"13 x {i} = {tabuada_13[i]}")
    
# Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50

numero = [input(f"Digite o número {i+1}: ") for i in range (5)]
