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





