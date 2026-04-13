# Exercício 16
# Leia o preço e classifique: barato(<50), médio(<100), caro.

# escreva seu código abaixo

preco = float(input("Informe o valor do produto R$"))

# if preco < 50:
#     print("O valor do produto está barato.")
# elif preco < 100:
#     print("O valor do produto está na média.")    
# else:
#     print("O valor do produto está caro.")    

def class_valor(preco):
    if preco <=50:
        return f"R${preco} - está barato"
    elif preco <= 100:
        return f"R${preco} - está na média"
    else:
        return f"R${preco} - está caro"
    
print(class_valor(preco))    