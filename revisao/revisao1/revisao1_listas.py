lista_nomes = ["Pedro", "Ana", "Maria"]

# ADICIONANDO ELEMENTOS EM UMA LISTA 
print(lista_nomes)

print()

lista_nomes.append("Gabriel") # Adicona um elemento ao final da lista

print(lista_nomes)

print()

lista_nomes.insert(1, "Carla") # Adiciona um elemento na posição desejada

print(lista_nomes)

print()

# REMOVENDO ELEMENTOS DE UMA LISTA

lista_nomes.remove("Ana") # Remove o elemento pelo nome

print(lista_nomes)

print()

del lista_nomes[0]

print(lista_nomes) # Remove o elemento pela posição

print()

lista_nomes.pop() # Remove o último elemento da lista

print(lista_nomes)

print()

lista_nomes.clear() # Remove todos os elementos da lista

print(lista_nomes)