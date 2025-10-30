def par_impar():
    try:
        numero_par_impar = input("Digite um numero para conferir se e par ou impar: ")
        numero_par_impar_float = float(numero_par_impar)

        if numero_par_impar_float % 2 == 0:
            print(f"O numero {numero_par_impar_float} e par")
        elif numero_par_impar_float % 2 != 0:
            print(f"O numero {numero_par_impar_float} e impar")
    except:
        print("Digite apenas numeros.")

par_impar()