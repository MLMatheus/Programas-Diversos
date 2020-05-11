def listarProdutos():
    for i in range(0, len(produtos)):
        print("Produto {} - {} - R${:.2f} - Quantidade em estoque, {}".format(i, produtos[i][0], produtos[i][1], produtos[i][2]))

produtos = []

while True:
    opcao = int(input("Tecle sua opção:\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Vender\n4 - Sair do programa"))

    if opcao == 1:
        nome = input("Qual o nome do produto?")
        preco = float(input("Qual o preço do produto?"))
        quantidade = int(input("Qual a quantidade em estoque?"))

        produto = []

        produto.append(nome)
        produto.append(preco)
        produto.append(quantidade)
        produtos.append(produto)

    if opcao == 2:
        listarProdutos()

    if opcao == 3:
        print("Escolha um produto a baixo:")
        listarProdutos()

        numero = int(input("Informe o número do produto"))

        quantidade = int(input("Qual a quantidade?"))

        if produtos[numero][2] >= quantidade:
            print("Produto vendido com sucesso! Informações da venda:\nProduto: {}\nQuantidade: {}\nValor total da venda: R${:.2f}".format(produtos[numero][0], quantidade, quantidade*produtos[numero][1]))
            produtos[numero][2] -= quantidade
        else:
            print("Quantidade indisponível em estoque")

    if opcao == 4:
        print("Fim do programa!")
        break