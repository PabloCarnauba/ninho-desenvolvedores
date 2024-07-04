def calcular_media(notas):
    return sum(notas) / len(notas)

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome == "sair" or nome == "SAIR":
        break
    
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    
    aluno = {
        'nome': nome,
        'notas': [nota1, nota2, nota3, nota4]
    }
    
    alunos.append(aluno)

aprovados = []
reprovados = []

for aluno in alunos:
    media = calcular_media(aluno['notas'])
    if media >= 6.0:
        aprovados.append({'nome': aluno['nome'], 'media': media})
    else:
        reprovados.append({'nome': aluno['nome'], 'media': media})

print("\nAprovados:")
print("Nome | Média")
print("-------------")
for aluno in aprovados:
    print(f"{aluno['nome']} | {aluno['media']:.2f}")

print("\nReprovados:")
print("Nome | Média")
print("-------------")
for aluno in reprovados:
    print(f"{aluno['nome']} | {aluno['media']:.2f}")