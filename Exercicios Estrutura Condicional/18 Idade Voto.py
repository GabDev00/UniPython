# Exercício 18
# Leia idade e informe se pode votar.

# escreva seu código abaixo

idade = int(input("Informe sua idade: "))

# if idade >= 16:
#     print("Você tem idade para votar.")
# else:
#     print("Você não tem idade para votar.")    

def pode_votar(idade):
    if idade >= 16:
        return f"Pode votar"
    else:
        return f"Não pode votar"
    
print(pode_votar(idade))    