# precos = {
#     100: 1.10,
#     101: 1.30,
#     102: 1.50,
#     103: 1.10,
#     104: 1.30,
#     105: 1.00
# }
# p
# def main():
#     while True:
#         try:
#             codigo = int(input("Digite o código do item:\n"))
#             quantidade = int(input("Digite a quantidade:\n"))
#         except ValueError:
#             print("Entrada inválida. Por favor, digite números inteiros.")
#             continue

#         if codigo in precos:
#             valor_total = precos[codigo] * quantidade
#             print(f"O valor a ser pago é: R${valor_total:.2f}")
#             break
#         else:
#             print("Código do item inválido. Tente novamente.")

# main()#

codigo = int(input("Digite o código do item que você deseja: "))

cardapio = {
100: 1.10, # Cachorro quente
101: 1.30, # Bauru simples
102: 1.50, # Bauru c/ovo
103: 1.10, #Hamburguer
104: 1.30, #Cheeseburguer
105: 1.00, #Refrigerante
}
Quantidade = int(input("Digite a quantidade do item: "))
valor = cardapio[codigo] * Quantidade
print(f"Valor a ser pago R$ {valor:.2f}")






