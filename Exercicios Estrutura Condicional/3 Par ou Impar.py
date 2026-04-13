# Exercício 3
# Leia um número inteiro e informe se ele é par ou ímpar.

# escreva seu código abaixo

num = int(input("Informe um número: "))


#       código sem DEF
# if num % 2 == 0:
#     print("Este Número é Par")
# else:
#     print("Este número é Impar")


def par_impar(num):
    if num % 2 == 0:
        return f"{num} é Par" 
    else:
        return f"{num} é Impar"
    
print(par_impar(num))


