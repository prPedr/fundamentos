lista_numeros = [5, 6, 9, 3, 10, 2, 8, 1, 4, 7]
lista_nomes = ["Pedro", "Ana", "Maria", "Carla", "Gabriel", "Lucas", "Mariana", "Rafael", "Beatriz", "Fernando", "Pedro", "Pedro"]

soma = 0

for numeros in lista_numeros:
    soma += numeros

    print(f"Número atual: {numeros} | Soma parcial: {soma}")

print()

while "Pedro" in lista_nomes:
    lista_nomes.remove("Pedro")

print(f"Lista atualizada: {lista_nomes}")