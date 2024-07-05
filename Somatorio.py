# Crie um programa que pede dois números ao usuário, calcule o somatório de todos os números entre esses dois números.
soma = 0

n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))

if n1 < n2:
    for i in range(n1,n2 + 1):
        soma += i
        
else:
    for i in range(n1,n2 + 1):
        soma += i
        
print(f"O somatório de todos os números entre {n1} e {n2} é: {soma}")