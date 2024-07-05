import opcode


n1 = input("digite um numero: ")
n2 = input("digite outro numero: ")
print("a soma dos números é:", float(n1) + float(n2))

print("a subtração dos números é:", float(n1) - float(n2))

print("a multiplicação dos números é:", float(n1) * float(n2))

print("a divisão dos números é:", float(n1) / float(n2))

if (opcode == "+"):
    soma = n1 + n2
    print(f"Soma: {soma}") 

op = input("Digite o operador (+, -, /, *):")
if (op == "+"):
    soma = n1 + n2
    print(f"Soma: {soma}")
if (op == "-"):
    subtração = n1 - n2
    print(f"Subtração: {subtração}")
    