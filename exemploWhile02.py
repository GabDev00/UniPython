# Peça a senha ao usuário e continue pedindo até ele digitar: unifecaf
# - estrutura do while: while condição:
# - use input para ler a senha

senha = input("Digite a senha: ")

while senha != "unifecaf":
    senha = input("Senha incorreta, digite novamente: ")

print("Senha Correta")



