def saudar(nome):
    print(f"Ola {nome}, seja bem-vindo!")

def multiplicacao(numero1):
    resultado = numero1 * 10
    print(f"O resultado da multiplicação é: {resultado}")

def boas_vindas(nome, cidade):
    print(f"{nome} seja bem-vindo(a) a {cidade}!")

def area_retangulo():
    valor_largura = input("Digite a largura do retângulo: ")
    valor_altura = input("Digite a altura do retângulo: ")

    valor_altura_float = float(valor_altura)
    valor_largura_float = float(valor_largura)

    area = valor_altura_float * valor_largura_float

    print(f"A área do retângulo é: {area}")

def par_impar():
    numero_par = input("Digite um número para verificar se é par ou ímpar: ")
    numero_par_float = float(numero_par)

    if numero_par_float % 2 == 0:
        print(f"O número {numero_par_float} é par.")
    elif numero_par_float % 2 != 0:
        print(f"O número {numero_par_float} é ímpar.")
    else:
        print("Valor inválido.")

par_impar()