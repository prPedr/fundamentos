# ABERTURA DO ARQUIVO EM MODO LEITURA
arquivo = open("meu_arquivo.txt", "r")

# LENDO O ARQUIVO INTEIRO
conteudo = arquivo.read()
print(conteudo)

# FECHAMENTO DO ARQUIVO
arquivo.close()