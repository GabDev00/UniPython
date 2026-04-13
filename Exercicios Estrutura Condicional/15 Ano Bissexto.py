# Exercício 15
# Leia um ano e informe se é bissexto.

# escreva seu código abaixo

ano = int(input("Informe um ano: "))

# if (ano % 100 != 0 and ano % 4 == 0) or ano % 400 == 0:
#     print(ano,"é ano Bissexto.")
# else:
#     print(ano,"não é Bissexto.")    

def ano_bissexto(ano):
    if (ano % 100 != 0 and ano % 4 == 0) or ano % 400 == 0:
        return f"{ano} é ano bissexto"
    else:
        return f"{ano} não é bissexto"
    
print(ano_bissexto(ano))    