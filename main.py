import json


def lista_tarefas(tarefas):
    while True:
        tarefa = input("Informe o tarefa que deseja realizar(ou digite 'v' para voltar): ")

        if tarefa.lower() == "v":
            break

        tarefas.append(tarefa)

        print("-------------------------")
        print("lista de tarefas atual:")
        for t in tarefas:
            print("-", t)
        print("-------------------------")

    return tarefas


def remover_tarefas(tarefas):
    while True:
        if not tarefas:
            print("Lista vazia!\n")
            return
        print("-------------------------")
        print("lista de tarefas atual:")

        for i in range (len(tarefas)):
            print(i + 1,"-", tarefas[i])

        print("-------------------------")
        remove = input("Informe o numero da tarefa(s) que deseja remover (ou 'v' para voltar): ")

        if remove.lower() == "v":
            break

        try:
            indice = int(remove)
            tarefas.pop(indice - 1) #Remove o item naquela posição
            print("Tarefa removida com sucesso!\n")
        except:
            print("Numero invalido!\n")


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

# ===== PROGRAMA PRINCIPAL =====

tarefas = carregar_tarefas() # carrega a lista principal

while True:
    print("""
MENU:
1 - ADICIONAR TAREFAS
2 - REMOVER TAREFAS
3 - LIMPAR LISTA DE TAREFAS 
4 - Salvar Lista de Tarefas
5 - Carregar Lista de Tarefas
6 - SAIR
7 - Ver Lista de Tarefas
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefas = lista_tarefas(tarefas)

    elif opcao == "2":
        remover_tarefas(tarefas)

    elif opcao == "3":
        tarefas.clear()
        print("Lista de tarefas limpada com sucesso!\n")

    elif opcao == "4":
        salvar_tarefas(tarefas)
        print("Tarefas salvas com sucesso!\n")

    elif opcao == "5":
        tarefas = carregar_tarefas()
        print("Tarefas carregadas com sucesso!\n")


    elif opcao == "6":
        salvar_tarefas(tarefas)
        print("Como sua lista de tarefas ficou:")
        for t in tarefas:
            print("-", t)
        print("encerrando...")
        break

    elif opcao == "7":
        print("lista de tarefas:")
        for t in tarefas:
            print("-", t)
