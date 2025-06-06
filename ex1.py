
def main():
    vetor = []
    numeroMenor = 0
    numeroMaior = 0
    zeros = 0

    opcao = int(input("Quantos número deseja colocar: "))
    for i in range(opcao):
        numero = int(input(f"Digite o número: "))
        vetor.append(numero)
        print("Vetor Números: ", vetor)
        if numero < 0:
            numeroMenor = numeroMenor + 1
        elif numero == 0:
            zeros = zeros + 1
        else:
            numeroMaior = numeroMaior + 1

        print(f"Contagem de números, Negativos '{numeroMenor}'. Positivos '{numeroMaior}'. ZEROS '{zeros}'")


main()
