def adicionar_veiculos(nomes, nome):
    if nome in nomes:
        print("Nome já cadastrado.")
    else:
        nomes.append(nome)
        print(f"Veículo {nome} adicionado.")

def listar_veiculos(nomes):
    if nomes:
        print("\nNomes cadastrados:")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")
    else:
        print("Nenhum nome cadastrado.")

def main():
    nomes = []

    while True:
        print("\nMenu de Opções")
        print("1. Adicionar nome")
        print("2. Listar nomes")
        print("3. Sair")
        opcao = input("Entre com a opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ").strip()
            adicionar_veiculos(nomes, nome)

        elif opcao == '2':
            listar_veiculos(nomes)

        elif opcao == '3':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
