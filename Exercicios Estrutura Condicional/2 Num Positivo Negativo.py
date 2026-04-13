# Exercício 2
# Leia um número e informe se ele é positivo, negativo ou zero.

# escreva seu código abaixo

num = int(input("Informe um número: "))


#       **Código sem DEF**
# if num > 0:
#     print("Número positivo")
# elif num == 0:
#     print("Seu número é 0")
# else:
#     print("Seu número é negativo")            

#       **Código com DEF**
def num_posivo_negatico_zero(num):
    if num > 0:
        return "Número positivo"
    elif num < 0:
        return "Número Negativo"    
    else:
        return "O número é igula a Zero"        
    

print(num_posivo_negatico_zero(num))