while True:
    opcao = input("Digite uma nova tarefa ou 'sair' para encerrar: ")
    if opcao.lower() == "sair":
        print("Programa encerrado.")
        break
    tarefa = opcao

    print(f"Nova tarefa adicionada: {tarefa}")

print(f"Ultima tarefa adicionada foi: {tarefa}")