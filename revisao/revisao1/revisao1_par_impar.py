numero1 = input("Digite um numero: ")

numero1_int = int(numero1)

numero_par = numero1_int % 2 == 0

numero_impar = numero1_int % 2 != 0

if numero_par:
    print(f"O numero {numero1_int} é par")
elif numero_impar:
    print(f"O numero {numero1_int} é impar")
else:
    print("Não foi possível determinar se o numero é par ou impar")