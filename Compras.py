totalDaCompra = 0
historico = ""

for i in range(5):
    
    nomeDoProduto = input("Digite o nome do produto:\n")
    valorDoProduto = float(input("Digite o valor do produto:\n"))
    quantidade = int(input("Digite a quantidade:\n"))
    
    totalDaCompra += valorDoProduto * quantidade
    historico += f"{nomeDoProduto} - R$ {valorDoProduto:.2f} - x{quantidade} - R$ {(valorDoProduto*quantidade):.2f}\n"
    
if (totalDaCompra >= 200):
    desconto = 0.1
else:
    desconto = 0
    
valorDesconto = totalDaCompra * desconto

valorFinal = totalDaCompra - valorDesconto

print(f'''
---------- Nota Fiscal ----------

{historico}

Valor Original: R$ {totalDaCompra}

Valor do Desconto: - R$ {valorDesconto}

Valor Final: R$ {valorFinal} 
      ''')