dicionario_produto = {
    "nome": "Notebook",
    "marca": "Dell",
    "preco": 3500.00,
    "estoque": 15
}

soma_vendas = 0

while dicionario_produto["estoque"] > 0:
    print(f"Tenho estoque de {dicionario_produto['estoque']} unidades do produto {dicionario_produto['nome']}.")
    venda = int(input("Quantas unidades você deseja comprar? "))
    if venda <= dicionario_produto["estoque"]:
        dicionario_produto["estoque"] -= venda
        total_venda = venda * dicionario_produto["preco"]
        soma_vendas += total_venda
        print(f"Você comprou {venda} unidades do produto {dicionario_produto['nome']} por R$ {total_venda:.2f}.")
    else:
        print("Desculpe, não temos estoque suficiente para essa quantidade.")