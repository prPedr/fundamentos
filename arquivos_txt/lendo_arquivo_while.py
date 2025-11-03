# ABRINDO O ARQUIVO EM MODO LEITURA
arquivo = open("meu_arquivo.txt", "r")

# LENDO O ARQUIVO USANDO WHILE
linha = arquivo.readline()
while linha:
    print(f"Conteúdo da linha: {linha.strip()}")  # .strip() remove espaços em branco extras
    linha = arquivo.readline()

# FECHAMENTO DO ARQUIVO
arquivo.close()
