# Exercício 6
# Leia dois números e mostre qual é o maior.

# escreva seu código abaixo

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

# if num1 > num2:
#     print("O número",num1," é o maior")
# else:
#     print("Número",num2, "é o maior ")    


def num_maior(num1, num2):
    if num1 > num2:
        return f"O número {num1} é o maior"
    else:
        return f"Número {num2} é o maior"
    

print(num_maior(num1,num2))    
