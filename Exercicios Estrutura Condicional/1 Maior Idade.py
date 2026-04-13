# Exercício 1
# Peça a idade do usuário e informe se ele é maior ou menor de idade.

# escreva seu código abaixo

idade = int(input("Informe sua Idade: "))

#       **Código sem DEF**
# if idade >= 18:
#     print("Você é maior de idade!")
# else:
#     print("Você não é maior de idade!")    

#      **Código com DEF**
def menor_maior_idade(idade):
    if idade >= 18:
        return "Maior de idade!"
    else:
        return "Menor de idade!"   
    

print(menor_maior_idade(idade))    
    