# Exercício 12
# Leia um número e informe se está entre 10 e 20.

# escreva seu código abaixo

num = int(input("Informe um número: "))

# if num >= 10 and num <= 20:
#     print("Este Número está entre 10 e 20. Número:", num)
# else:
#     print("Este número não está entre 10 e 20. Número:", num)    

def num_entre_10_20(num):
    if num >= 10 and num <= 20:
        return f"O número {num} está entre 10 e 20."
    else:
        return f"O número {num} não está entre 10 e 20"
    
print(num_entre_10_20(num))    