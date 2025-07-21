def main():
    opcao = 1 
    while opcao == 1:
        num = int(input("Insira um número: "))
        if num % 2 == 0:
            print("O número é par")
        else:
            print("O número é impar")
        opcao = int(input("Deseja continuar? 1- sim / 2- não"))

main()
