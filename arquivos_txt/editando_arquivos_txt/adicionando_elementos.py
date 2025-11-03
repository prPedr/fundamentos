frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

with open("frutas.txt", "a") as arquivo_frutas:
    for fruta in frutas:
        arquivo_frutas.write(fruta + "\n")