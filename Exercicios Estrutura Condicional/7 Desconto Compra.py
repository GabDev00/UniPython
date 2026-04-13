# Exercício 7
# Leia o valor de uma compra. Se for maior que 100, aplique 10% de desconto.

# escreva seu código abaixo

Valor_Compra = float(input("Informe o valor da compra R$ "))

# if Valor_Compra >= 100:
#     Valor_Compra = Valor_Compra - (10/100 * Valor_Compra)
#     print("Com desconto sua compra ficou R$",Valor_Compra)
# else:
#     print("Sua compra não teve desconto, valor a pagar R$", Valor_Compra)    

def desconto(Valor_Compra):
    if Valor_Compra >= 100:
        Valor_Compra = Valor_Compra - (0.1 * Valor_Compra)
        return f"Desconto aplicado! Valor da compra: R${Valor_Compra}"
    else:
        return f"Desconto não aplicado, valor da compra: R${Valor_Compra}"
    
print(desconto(Valor_Compra))    
