num1 = input("Digite um numero: ")
operador = input("Digite um operador: ")
num2 = input("Digite outro numero: ")

num1_float = float(num1)
num2_float = float(num2)

soma = num1_float + num2_float
subtracao = num1_float - num2_float
multiplicacao = num1_float * num2_float
divisao = num1_float / num2_float
divisao_inteira = num1_float // num2_float
resto_divisao = num1_float % num2_float
potencia = num1_float ** num2_float

if operador == "+":
  print(f"{num1_float} + {num2_float} = {soma:.2f}")
elif operador == "-":
  print(f"{num1_float} - {num2_float} = {subtracao:.2f}")
elif operador == "*":
  print(f"{num1_float} * {num2_float} = {multiplicacao:.2f}")
elif operador == "/":
  print(f"{num1_float} / {num2_float} = {divisao:.2f}")
elif operador == "//":
  print(f"{num1_float} // {num2_float} = {divisao_inteira}")
elif operador == "%":
  print(f"{num1_float} % {num2_float} = {resto_divisao}")
elif operador == "**":
  print(f"{num1_float} ** {num2_float} = {potencia:.2f}")
else:
  print("Operador invalido")