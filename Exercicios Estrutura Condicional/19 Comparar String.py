# Exercício 19
# Leia duas palavras e informe se são iguais.

# escreva seu código abaixo

texto1 = input("Digite uma palavra: ")
texto2 = input("Digite outra palavra: ")

# if texto1 == texto2:
#     print("São as mesmas palavras.")
# else:    
#     print("As palavras não são as mesmas."  )

def palavras_iguais(texto1, texto2):
    if texto1 == texto2:
        return f"Palavras iguais"
    else:
        return f"Palavras não são iguais"
    
print(palavras_iguais(texto1, texto2))    