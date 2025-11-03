with open("meu_arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
    numero_linhas = len(linhas)
    print(f"O arquivo possui {numero_linhas} linhas.")