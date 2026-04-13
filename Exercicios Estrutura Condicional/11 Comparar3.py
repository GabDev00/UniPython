# Exercício 11
# Leia três números e mostre o maior.

# escreva seu código abaixo

num1 = int(input("Informe o primeiro número "))
num2 = int(input("Informe o segundo número "))
num3 = int(input("Informe o terceiro número "))

#maior = num1

# if num2 > maior:
#     maior = num2
    
# if num3 > maior:
#     maior = num3
    
# print("O maior número é:", maior)         

def maior_de_tres(num1, num2, num3):
    maior = num1
    if num2 > maior:
        maior = num2

    if num3 > maior:
        maior = num3

    return f"O maior número é {maior}"   

print(maior_de_tres(num1, num2, num3))     