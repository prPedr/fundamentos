# UTILIZANDO O 'with' PARA GERENCIAR O ARQUIVO
with open("meu_arquivo_teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(f"Conteúdo da linha: {linha.strip()}")  # .strip() remove espaços em branco extras
