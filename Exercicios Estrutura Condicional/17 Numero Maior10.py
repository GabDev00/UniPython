# Exercício 17
# Leia um número e informe se é maior que 10.

# escreva seu código abaixo

num = float(input("Informe um número: "))

# if num > 10:
#     print("Este número é maior que 10")
# else:
#     print("Este número não é maior que 10")    

def maior_que_dez(num):
    if num > 10:
        return f"O número {num} é maior que dez"
    else:
        return f"O número {num} não é maior que dez"
    
print(maior_que_dez(num))    