def main():
    opcao = 1
    while opcao == 1:
        a = 0
        somaNotas = 0
        numNotas = int(input("Digite quantas notas deseja adicionar: "))
        while a < numNotas:
            somaNotas += float(input("Digite a nota: "))
            a += 1
        media = somaNotas / numNotas
        print("A média final foi", media)
        if media >= 7:
            print("Aluno aprovado")
        elif media >= 5:
            print("Aluno de recuperação")
        else:
            print("Aluno reprovado")
        opcao = int(input("Deseja ver a media de mais um aluno? 1- Sim / 2- Não: "))

main()
