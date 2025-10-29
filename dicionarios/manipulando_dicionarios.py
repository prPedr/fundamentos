dicionario_animais = {
    "animal": "Cachorro",
    "idade": 5,
    "nome": "Rex",
    "cor": "Marrom"
}

dicionario_animais["idade"] = 6 # Muda o valor da chave idade
dicionario_animais["peso"] = 20.5 # Adiciona uma nova chave peso
del dicionario_animais["cor"] # Remove a chave cor

procurar_chave = "cor" in dicionario_animais
print(f"A chave 'nome' existe no dicionario? {procurar_chave}")
print(dicionario_animais)