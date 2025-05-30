numeros = [10, 20, 30, 40, 50]

print("Vetor numeros: ", numeros)
numeros.append(60) #apende add elementos no vetor

print("Vetor após a inserção: ", numeros)
numeros.remove(30) #remove remove elementos

print("Vetor após a remoção: ", numeros)
print("Elemento no índice 2: ", numeros[2]) #numeros[2] ele busca o que esta guardado no segundo índice

soma = sum(numeros) #sum soma os elementos do vetor
print("Soma dos elemtos do vetor: ", soma)

#função max e min determina o maior e menor elemento dentro do vetor
maior = max(numeros)
menor = min(numeros)
print(f'Maior {maior} // Menor {menor}')

#a função sorte organiza os números dentro do vetor
numeros.sort()
print("Vetor ordenado crescente: ", numeros)
numeros.sort(reverse=True)
print("Vetor ordenado decrescente: ", numeros)
numeros.sort(reverse=False)
