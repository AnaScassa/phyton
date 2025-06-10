import array

def adicionar_numero(numeros, numero, maior, menor, media):
    numeros.append(numero)
    print(f"Número {numero} adicionado.")

def main():
    numeros = []
    numero = array.array('i', [])
    maior = 0
    menor = 999
    media = 0

    while True:
        print("\nLista de Números")
        print("1. Adicionar número a lista")
        print("2. Ver média dos números")
        print("3. Ver maior e menos número")
        print("4. Sair")
        opcao = int(input("Entre com a opção: "))

        if opcao == 1:
            numero = int(input("Digite o número: "))
            adicionar_numero(numeros, numero, maior, menor, media)
            media += numero

            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

        elif opcao == 2:
            print(f"A média está {media}")

        elif opcao == 3:
            print(f"O maior é {maior} e o menor é {menor}")

        elif opcao == 4:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()