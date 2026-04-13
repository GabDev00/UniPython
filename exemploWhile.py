# Enquanto o usuário não digitar 0 continue somando todos os números digitados
# n é um número informado pelo usuário
# dicas:
# - estrutura do while: while condição:
# - use input para ler o número n

x = int(input("Informe um valor inteiro: "))
soma = 0

while x != 0:
    soma = soma + x
    print(soma)
    x = int(input("Informe um valor inteiro: "))

print("Finalizado")    