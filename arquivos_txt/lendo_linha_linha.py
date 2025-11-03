# ABERTURA DO ARQUIVO EM MODO LEITURA
arquivo = open("meu_arquivo.txt", "r")

# LENDO ARQUIVO LINHA A LINHA
for linha in arquivo:
    print(f"Conteúdo da linha: {linha.strip()}") # .strip() remove espaços em branco extras

# FECHAMENTO DO ARQUIVO
arquivo.close()