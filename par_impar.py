num1 = input("Informe um numero: ")

num1_int = int(num1)

comparacao_par = num1_int % 2 == 0
comparacao_impar = num1_int % 2 != 0

if comparacao_par:
  print(f"O numero {num1_int} e par")
elif comparacao_impar:
  print(f"O numero {num1_int} e impar")
else:
  print("Informe um numero valido")