def main ():
    media = 0 #não esquecer de inicializar a variavel antes de usa ela
    contagem = int(input("Digite quantas notas deseja colocar: "))
    for i in range(contagem):
        nota = 0
        nota = int(input("Digite a nota: "))

        while nota > 10 or nota < 0:
            nota = int(input("Nota invalida. Digite novamente: "))

        media +=  nota
    media = media / contagem

    print(f"A média final foi {media}")

    if media >= 7:
        print("Aluno aprovado")
    elif media >= 5 or media < 7:
        print("Aluno de recuperação")
    else:
        print("Aluno reprovado")
        
main ()