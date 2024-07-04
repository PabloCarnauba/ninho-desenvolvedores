import os

lanchonete = {
    "01": {'nome': 'Sorvete', 'preco': 5},
    "02": {'nome': 'Açai', 'preco': 12},
    "03": {'nome': 'Banana', 'preco': 4},
}

def clear():
    print("\n" * os.get_terminal_size().lines)

def exibirMenu(tipo):
    print('====== LANCHONETE ======')
    if(tipo == 'admin'):        
        print('1 - Adicionar um novo produto')
        print('2 - Remover um produto')
        print('3 - Sair')
        
    elif(tipo == 'user'):
        print('1 - Comprar produto')
        print('2 - Sair')
        
    return input("---- Resposta: ")

def perguntarInformacoes():
    codigo = input("Digite o código: ")
    nome = input("Digite o nome: ")
    preco = float(input("Digite o preço: "))

    return codigo, nome, preco

def exibirProduto(codigo, nome, preco):
    clear()
    print('======== PRODUTO ========')
    print(f'ID: {codigo}')
    print(f'Nome: {nome}')
    print(f'Preço: R$ {preco}')
    print('======== ======== ========')

def exibirProdutos(produtos):
    if produtos:
        for i in produtos:
            print(f'ID: {i} | Nome: {produtos[i]["nome"]} | Preço: {produtos[i]["preco"]}')
    else:
        clear()
        print("Nenhum produto encontrado")
    print('======== ======== ========')

fluxoUsuario = 'login'
email = 'admin@gmail.com'
usuario = input("Insira seu email: ")

if usuario == email:
    print("Bem-vindo, ADM!")
    fluxoUsuario = 'admin'

else:
    print("Bem-vindo, cliente!")
    fluxoUsuario = 'usuario'


while fluxoUsuario == 'admin':
    resposta = exibirMenu('admin')

    if resposta == '1':   
        print("====== ADIÇÃO DE PRODUTO ====== ")
        produto = perguntarInformacoes()
        exibirProduto(produto[0], produto[1], produto[2])
        
    elif resposta == '2':
        print("====== REMOÇÃO DE PRODUTO ====== ")
        exibirProdutos(lanchonete)

        produtoEscolhido = input("Digite o ID do produto a ser removido: ")
        lanchonete.pop(produtoEscolhido)

        exibirProdutos(lanchonete)
    
    elif resposta == '3':
        break
    else:
        print("Opção inválida")

while fluxoUsuario == 'usuario':
    resposta = exibirMenu('user')

    if resposta == '1':        
        clear()
        print("====== ESCOLHA O PRODUTO ====== ")
        exibirProdutos(lanchonete)

        produtoId = '666'
        produtosId = []
        precos = []
        iterator = 1


        while produtoId != 'Sair' or 'sair':                   
            print(f'\n====== PEDIDO {iterator} ======\n')
            produtoId = input("Digite o ID do produto a ser Comprado ou digite 'Sair/sair': ")
            if produtoId == 'Sair' or produtoId == 'sair':
                break

            iterator += 1

            if lanchonete[produtoId] != None:
                produto = lanchonete[produtoId]

                
                quantidadeProduto = float(input("Digite a quantidade do produto: "))
                produtosId.append(produtoId)
                precos.append(quantidadeProduto)
            else:
                print("Opção inválida")

        clear()
        valorTotal = []
        for i in range(len(produtosId)):
            print('--------------------------\n')
            valor = lanchonete[produtosId[i]]['preco'] * precos[i]
            valorTotal.append(valor)
            print(f' Código: {produtosId[i]} | Nome: {lanchonete[produtosId[i]]['nome']} \nQuantidade: {precos[i]} | Valor Total: R$ {valor}\n')

        print('------------ MERCADINHO XAOLIN MATADOR DE PORCO -------------\n')
        print("Compra efetuada com sucesso!")
        print(f'Valor Final: R$ {sum(valorTotal)}\n')

    elif resposta == '2':
        break