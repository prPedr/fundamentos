soma = 0
numero_while = 1

while True:
    soma += numero_while
    if soma  > 100:
        break
    numero_while += 1

print(f"A soma dos numeros de 1 ate {numero_while - 1} e {soma}")