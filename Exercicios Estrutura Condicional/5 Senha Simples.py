# Exercício 5
# Peça uma senha e verifique se ela é igual a '1234'.

# escreva seu código abaixo

senha = input("Informe a Senha: ")

# if senha == "1234":
#     print("Senha Valida!")
# else:
#     print("Senha Invalida!")    

def senha_igual(senha):
    if senha == "1234":
        return "Senha Correta"
    else:
        return "Senha Incorreta"

print(senha_igual(senha))            