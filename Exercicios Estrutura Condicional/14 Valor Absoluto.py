# Exercício 14
# Leia um número e mostre seu valor absoluto.

# escreva seu código abaixo

num = float(input("Informe um qualque número: "))

# num_abs = abs(num)

# print("O valor absluto de", num, "é", num_abs)


def valor_absoluto(num):
    num_abs = abs(num)
    return f"O valor absoluto de {num} é {num_abs}"
    
print(valor_absoluto(num))