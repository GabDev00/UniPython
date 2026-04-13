# Exercício 9
# Leia a idade e classifique: criança (<12), adolescente (<18), adulto.

# escreva seu código abaixo

idade = int(input("Informe a sua idade: "))

# if idade < 12:
#     print("Você é uma Criança")
# elif idade < 18:
#     print("Você é um Adolecente")    
# else:
#     print("Você é um Adulto")    

def classificao_idade(idade):
    if idade <= 12:
        return f"{idade} anos, você é uma criança."
    elif idade <= 18:
        return f"{idade} anos, você é um adolecente."
    else:
        return f"{idade} anos, você é um adulto."
    
print(classificao_idade(idade))    