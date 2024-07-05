idade = float(input("Digite sua idade: "))
if idade >= 10 and idade < 17:
    print("Você é adolescente!")
elif idade >= 18 and idade < 30:
    print("Você é jovem!")
elif idade >= 30 and idade <= 100:
    print("Você é adulto!")
else:
    print("Valor não encontrado!")