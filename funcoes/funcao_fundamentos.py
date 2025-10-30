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

area_retangulo()