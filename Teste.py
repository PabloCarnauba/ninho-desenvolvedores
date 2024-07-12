def numeros():
        num1 = int(input("Digite um número inteiro para verificação: "))
        num2 = int(input("Digite um número inteiro para verificação: "))

        if (num1 % 2) == 0 and (num2 % 2) == 0:
            print(f"A soma dos números é {num1 + num2}")
numeros()