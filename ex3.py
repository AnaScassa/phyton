def adicionarLista(vetor, item):
    vetor.append(item)
    print(f"Item {item} adicionado.")

def listar(vetor, item):
    if vetor:
        print("Lista:")
        for i, item in enumerate(vetor, start=1):
            print(f"{i}. {item}")

def main():
    vetor = []
    i = 1

    print("***Lista de compras***")
    while True:
        print("1. Adicionar item a lista")
        print("2. Exibir lista")
        print("3. Sair")
        opcao = int(input("Entre com a opção: "))

        if opcao == 1:
            item = input(f"{i}. ")
            i += 1
            adicionarLista(vetor, item)

        elif opcao == 2:
            listar(vetor, item)

        elif opcao == 3:
            print("Saindo do programa...")
            break
main()