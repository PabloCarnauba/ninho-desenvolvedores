valor = float(input("Digite o valor da compra:\n"))

if valor > 200:
    valorDesconto1 = (valor * 0.1)
    print("Parabéns! Desconto de 10% em suas compras! ;D")
    print(f"O valor total do seu desconto foi: {valorDesconto1} $")
    valorFinal1 = valor - valorDesconto1 
    print(f"O valor final da sua compra foi: {valorFinal1} $")

elif valor >= 100 and valor <= 200:
    valorDesconto2 = (valor * 0.05)
    print("Parabéns! Desconto de 5% em suas compras! ;D")
    print(f"O valor total do seu desconto foi: {valorDesconto2} $")
    valorFinal2 = valor - valorDesconto2
    print(f"O valor final da sua compra foi: {valorFinal2} $")

elif valor < 100:
    print("Não há desconto para sua compra >:(")
    print(f"O valor final da sua compra foi: {valor}")

else:
    print("Digite um valor válido!")