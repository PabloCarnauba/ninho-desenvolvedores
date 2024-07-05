raioCirculo = float(input("Digite o raio da base:\n"))
alturaCilindro = float(input("Digite a altura do cilindro:\n"))

pi = 3.14159

areaBase = pi * (raioCirculo * 2)

volumeCilindro = areaBase * alturaCilindro
areaCilindro = pi * (raioCirculo * raioCirculo)

print(f"O volume do cilindro especificado é: {volumeCilindro:.2f}")
print(f"A área do cilindro especificado é: {areaCilindro:.2f}")