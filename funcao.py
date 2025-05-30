def adicionar_nome(vetor, nome):
        vetor.append(nome)
        print("Vetor Nomes: ", vetor)

def remover_nome(vetor, nome):
    if nome in vetor:
        vetor.remove(nome)
        print("Nome removido", nome)
    else:
        print(f'Nome {nome} não encontrado')

def listar_nomes(vetor):
    if vetor:
        print("Nomes na lista: ")
        for nome in vetor:
            print(f'- {nome}')
    else: print("A lista esta vazia")

def main():
    vetor = []

    while True:
        print("Lista de Nomes")
        print("1. Adicionar nomes")
        print("2. Remover nomes")
        print("3. Listar nomes")
        print("4. Sair")
        opcao = int(input("Entre com a opção: "))

        if opcao == 1:
            numero = int(input("Quantos nomes deseja adicionar: "))
            for i in range(numero):
                nome = input("Digite o nome: ")
                adicionar_nome(vetor, nome)

        elif opcao == 2:
            nome = input("Digite o nome: ")
            remover_nome(vetor, nome)

        elif opcao == 3:
            listar_nomes(vetor)

        else:
            print("Saindo do programa...")
            break
main()