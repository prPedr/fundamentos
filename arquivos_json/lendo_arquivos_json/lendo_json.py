import json

with open("livros.json", "r") as arquivo:
    livros = json.load(arquivo) # Carrega o conteúdo do arquivo JSON em um dicionário

    for livro in livros:
        print(livro)

    print("")
    print(livros[0]["titulo"])  # Acessa o título do primeiro livro
    print(livros[1]["titulo"])  # Acessa o título do segundo livro
    print(livros[2]["titulo"])  # Acessa o título do terceiro livro
    print(livros[3]["titulo"])  # Acessa o título do quarto livro
    print(livros[4]["titulo"])  # Acessa o título do quinto livro