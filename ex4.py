def main():
    vetor = []
    impar = 0
    par = 0
    contagem = int(input("Digite quantos numeros deseja colocar: "))
    for i in range(contagem):
        vetor = int(input("Digite o número: "))
        if vetor % 2 == 0:
            print("O número é par.")
            par += 1
        else:
            print("O número é ímpar.")
            impar += 1

    print(f"Números PAR {par}. Números IMPAR {impar}")

main()