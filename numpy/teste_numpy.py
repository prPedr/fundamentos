import numpy as np

minha_lista = [1, 2, 3]

minha_matriz = [[1, 2, 3], [4, 5, 6]]

print(np.array(minha_lista))

print(sum(minha_lista))

print()

print(np.array(minha_matriz))

print()

print(np.sum(minha_matriz))

print()

print(np.arange(0, 10))

print()

print(np.zeros(3))

print(np.zeros([2, 4]))

print()

print(np.ones(3))

print(np.ones([3, 5]))

print()

print(np.eye(4))

print()

print(np.linspace(0, 100, 50))

print()

print(np.random.random(2)) # Gera uma lista de numeros aleatotios

print()

lista_teste = np.zeros(8)

lista_teste.shape

print(lista_teste.reshape([2, 4]))