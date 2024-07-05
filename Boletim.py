n1 = float(input("Digite a nota 1:\n"))
n2 = float(input("Digite a nota 2:\n"))
n3 = float(input("Digite a nota 3:\n"))
n4 = float(input("Digite a nota 4:\n"))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7 and media <= 10:
    print("Você passou! :)")
elif media >= 4 and media < 7:
    print("Você está de recuperação! :(")
elif media < 4 and media <= 0:
    print("Você está reprovado! >:(")
else:
    print("Valor não encontrado!")