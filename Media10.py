somaNotas = 0
qtdNotas = 0

for i in range(10):
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