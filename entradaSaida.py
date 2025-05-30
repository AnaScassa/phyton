nome = input("Entre com seu nome: ") #tudo que vem via input é string

#saídas
print("Seu nome é: ", nome)
print("Seu nome é %s", nome)
print("Seu nome é {}" .format(nome))

#entrada de dados int
idade= int(input("Entre com a idade: "))
media = 7.5 #Aqui ele entende que a variavel é float

#Saída com concatenação de variavel. Feito para mostrar mais variaveis em uma lingus
print(f'Seu nome é {nome} e sua idade é {idade}')