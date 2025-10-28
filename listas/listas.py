lista_nomes = ["Pedro", "Ana", "Maria"]

lista_nomes.append("Gabriel") # Adicona um elemento ao final da lista
lista_nomes.insert(1, "Carla") # Adiciona um elemento na posição desejada

print(lista_nomes)

lista_nomes.remove("Ana") # Remove o elemento pelo nome
del lista_nomes[0] # Remove o elemento pela posição
lista_nomes.pop() # Remove o último elemento da lista
lista_nomes.clear() # Remove todos os elementos da lista

print(lista_nomes)

print()

lista_numeros = [10, 20, 30, 40, 50]

lista_numeros.append(60)
lista_numeros.insert(1, 15)
del lista_numeros[3]

print(lista_numeros)