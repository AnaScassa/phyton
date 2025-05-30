nota1 = float(input("Entre com a nota 1: "))
nota2 = float(input("Entre com a nota 1: "))
frequencia = float(input("Entre com a frequência: "))

media = (nota1 + nota2)/ 2

if media >= 6 and frequencia >= 75: #nao precisa do parantese/chaves, mas precisa seguir o espaçamento
    print("Aluno aprovado")
    print("Sua média foi: ", media)
    print("Sua frequência foi ", frequencia)
elif media >= 4 and media < 6 and frequencia >= 75:
    print("Aluno de exame")
    print("Sua média foi: ", media)
    print("Sua frequência foi ", frequencia)
else :
    print("Aluno reprovado")
    print("Sua média foi: ", media)
    print("Sua frequência foi ", frequencia)