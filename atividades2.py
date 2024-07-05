#Lê os valores A, B, C e imprime na tela se a soma de A + B é menor que C.
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite mais um numero: "))

soma = int(a + b)
if soma < c:
    print(f"A soma de {a} + {b} é menor que {c}")
elif soma >c:
    print(f"A soma de {a} + {b} é maior que {c}")
    

#Recebe um número qualquer e informa se é par ou ímpar.
    n = int(input("Digite um numero: "))
if n % 2 ==0:
    print(f"O numero {n} é par") 
else:
    print(f"O numero {n} é ímpar")
    
#Leia dois valores inteiros A e B se os valores forem iguais
#deverá somar os dois, caso contrário multiplique A por B. Ao final de qualquer um
#dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

if a == b:
    print("Valor:", a + b)
elif a != b:
    print("Valor", a * b)

#Lê três valores inteiros e diferentes e mostre-os em ordem decrescente. 
A = int(input("Digite o primeiro valor inteiro: "))
B = int(input("Digite o segundo valor inteiro: "))
C = int(input("Digite o terceiro valor inteiro: "))

if A != B and A != C and B != C:
    maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C
menor = A
if B < maior:
    menor = B
if C < menor:
    menor = C
    
    meio = (A+B+C) - maior - menor
    print("Valores em ordem decrescente:", maior, meio, menor)
else:
    print("Os valores devem ser diferentes")


#Ler o nome e as três notas obtidas por um aluno durante o semestre.
#Calcular a média, informar o nome e a menção Aprovado, Reprovado e Recuperação.
nome = input("Digite seu nome: ")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

media = (n1+n2+n3) / 3 

if media>=7:
    print(f"{nome}, Voce foi aprovado(a) com média {media}!")

elif media<=5:
    print(f"{nome}, Voce foi reprovado(a) com média {media} :(")
else:
    print(f"{nome}, Voce está de recuperação com média {media} ")
    
#Lanchonete(código)
precos = {
    100: 1.10,
    101: 1.30,
    102: 1.50,
    103: 1.10,
    104: 1.30,
    105: 1.00
}

def main():
    while True:
        try:
            codigo = int(input("Digite o código do item:\n"))
            quantidade = int(input("Digite a quantidade:\n"))
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")
            continue

        if codigo in precos:
            valor_total = precos[codigo] * quantidade
            print(f"O valor a ser pago é: R${valor_total:.2f}")
            break
        else:
            print("Código do item inválido. Tente novamente.")

main()

# Calcule a tabuada do 13 
tabuada_13 = {}

for i in range(1, 11):
     tabuada_13[i] = 13 * i

for i in tabuada_13:
     print(f"13 x {i} = {tabuada_13[i]}")
    
# Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50
contador = 0

for i in range(10):
    numero = int(input("Digite um número:\n"))
    if 10 <= numero <= 50:
        contador += 1

print("Quantidade de números entre 10 e 50:", contador)

#Ler do teclado uma lista com 5 números inteiros e imprimir o menor valor
numeros = [int(input(f"Digite o {i+1} número:\n")) for i in range (5)]

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(f"O menor valor é: {menor}")

#Calcule o somatório dos números de 1 a 100 e imprima o resultado
soma = 0

for i in range(1, 100):
    soma += i

print("O somatório dos números de 1 a 100 é:")

#Calcule a área do retângulo, imprimindo caracteres
largura = int(input("Digite a largura do Retângulo:\n"))
altura = int(input("Digite a altura do Retângulo:\n"))

for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura -1:
            print("#", end = "")
        else:
            print(" ", end = "")
    print()

#Ler do teclado um número inteiro e imprimir se ele é primo ou não
def primo():
    numero = int(input("Digite um número:\n"))
    divisores = 0
    for i in range(1, numero + 1):

        if (numero % i == 0):
            divisores += 1

    if (divisores > 2):
        print("Não é primo!")
    else:
        print("È primo")
primo()
