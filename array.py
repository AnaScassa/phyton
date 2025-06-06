import array

def adicionar_veiculos(nomes, anos, nome, ano):
    nomes.append(nome)
    anos.append(ano)
    print(f"Veículo {nome} do ano {ano} adicionado.")

def listar_veiculos(nomes, anos):
    if nomes:
        print("Veículos cadastrados:")
        for i in range(len(nomes)):
            print(f"Nome: {nomes[i]}, Ano: {anos[i]}")
    else:
        print("Nenhum veículo cadastrado.")

def remover_veiculos(nomes, anos, nome):
    if nome in nomes:
        indice = nomes.index(nome)
        nomes.pop(indice)
        anos.pop(indice)
        print(f"Veículo {nome} removido.")
    else:
        print(f"Veículo {nome} não encontrado.")

def main():
    nomes = []
    anos = array.array('i', [])

    while True:
        print("\nLista de Carros")
        print("1. Adicionar carros")
        print("2. Remover carros")
        print("3. Listar carros")
        print("4. Sair")
        opcao = int(input("Entre com a opção: "))

        if opcao == 1:
            nome = input("Digite o nome do veículo: ")
            ano = int(input("Digite o ano de fabricação: "))
            adicionar_veiculos(nomes, anos, nome, ano)

        elif opcao == 2:
            nome = input("Digite o veículo a ser removido: ")
            remover_veiculos(nomes, anos, nome)

        elif opcao == 3:
            listar_veiculos(nomes, anos)

        elif opcao == 4:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
