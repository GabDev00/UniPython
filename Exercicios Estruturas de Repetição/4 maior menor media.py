# Desenvolva um algoritmo que leia uma lista de inteiros
# e retorne o maior valor, o menor valor e a média de valores
 
numeros_inteiros = [1, 2, 3, 4, 5, 6, 7]

maior = numeros_inteiros[0]
menor = numeros_inteiros[0]



for n in numeros_inteiros:
    print(n)
    if maior < n:
        maior = n
    if menor > n:
        menor = n
        print(menor)           


media = (maior + menor) / 2
print(f"maior: {maior}")
print(f"menor: {menor}")
print(f"media: {media}")


print(max(numeros_inteiros))
print(min(numeros_inteiros))