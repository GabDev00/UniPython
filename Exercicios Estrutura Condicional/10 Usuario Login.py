# Exercício 10
# Peça usuário e informe se é 'admin'.

# escreva seu código abaixo

usuario = input("Informe o Usuário: ")

# if usuario == "admin":
#     print("Bem-vindo Admin")
# else:
#     print("Não é o Admin")    

def verifique_admin(usuario):
    if usuario == "admin":
        return f"Usuário {usuario} está correto"
    else:
        return f"Usuário {usuario} não está correto"

print(verifique_admin(usuario))    