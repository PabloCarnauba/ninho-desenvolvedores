def gerenciarLivros():
    livros = []

    while True:
        codigo = input("Digite o código do livro (ou 'sair' para parar): ")
        if codigo == 'sair' or codigo == 'SAIR':
            break
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")

        livro = {"codigo": codigo, "titulo": titulo, "autor": autor, "ano": ano}
        livros.append(livro)

    print("\nLista de Livros Cadastrados:")
    for livro in livros:
        print(f"\nCódigo: {livro['codigo']}\nTítulo: {livro['titulo']}\nAutor: {livro['autor']}\nAno de Publicação: {livro['ano']}")

    while True:
        print("\n----- Remoção de Livros -----")
        for livro in livros:
            print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")
        
        codigoRemover = input("Digite o código do livro para remover (ou 'sair' para parar): ")
        if codigoRemover == 'sair' or codigoRemover == 'SAIR':
            break
        
        livroEncontrado = None
        for livro in livros:
            if livro["codigo"] == codigoRemover:
                livroEncontrado = livro
                break
        
        if livroEncontrado:
            livros.remove(livroEncontrado)
            print(f"Livro com código '{codigoRemover}' removido com sucesso.")
        else:
            print("Código inválido!")

gerenciarLivros()