# Exercício 13
# Leia uma letra e informe se é vogal ou consoante.

# escreva seu código abaixo

letra = input("Informe uma letra: ")

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("é uma vogal")
# else:
#     print("É uma consoante")

def vogal_consoante(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return f"A letra '{letra}' é uma vogal"
    else:
        return f"A letra '{letra}' é uma consoante"

print(vogal_consoante(letra))    