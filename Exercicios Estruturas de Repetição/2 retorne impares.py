# Crie um aplicativo que leia uma lista de inteiros 
# e retorne todos os números ímpares

numeros_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numeros_inteiros:
    if n % 2 != 0:
        print(f"{n} é impar")