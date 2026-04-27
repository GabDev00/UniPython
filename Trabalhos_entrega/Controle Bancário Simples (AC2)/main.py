# DESCRIÇÃO DO PROBLEMA

# Crie um programa em Python que simule um sistema bancário com as seguintes funcionalidades:

# 1 - Adicionar dinheiro (Depósito)
# 2 - Sacar dinheiro
# 3 - Mostrar extrato

# O sistema não deve permitir a realização de saques quando o saldo for insuficie

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

conta = 0.0
historico = []

def AdicionarDinheiro(conta, valor_deposito):
    if valor_deposito > 0:
        conta += valor_deposito
        print("\nDepósito realizado com sucesso!")
        print(f"\nSaldo atual R${conta:.2f}")  
        historico.append(f"Depósito: R${valor_deposito:.2f}")    
    return conta

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def SacarDinheiro(conta, valor_saque):
    if valor_saque > conta:
        print("Valor insuficente para saque!")    
    elif valor_saque <= 0:
        print("Valor digitado é negativo")
    else:
        conta -= valor_saque
        print("\nSaque realizado com sucesso!")  
        print(f"\nSaldo atual: R${conta:.2f}")
        historico.append(f"Saque: R${valor_saque:.2f}")
    return conta
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def MostrarExtrato(conta):
    if historico == []:
        print("Não foram realizadas movimentações.")
    else:    
        for m in historico:
            print(m)
    print(f"\nSaldo atual R${conta:.2f}")
    return conta
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------    

escolha = None

while escolha != "4":

    print("\n==== MENU =====\n")
    print("1 - Adicionar Dinheiro")
    print("2 - Sacar Dinheiro")
    print("3 - Mostrar Extrato")
    print("4 - Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        print("\n==== ADICIONAR DINHEIRO =====\n")
        valor_deposito = float(input("Digite o valor: ")) 
        conta = AdicionarDinheiro(conta, valor_deposito)
        print("=============================")                  

    elif escolha == "2":
        print("\n==== SACAR DINHEIRO =====\n")
        valor_saque = float(input("Digite o valor para Saque: "))
        conta = SacarDinheiro(conta, valor_saque)
        print("=========================")                  
        

    elif escolha == "3":
        print("\n==== EXIBIR EXTRATO =====\n")
        MostrarExtrato(conta)
        print("=========================")                  

    elif escolha == "4":
        print("Obrigado!")
        continue

    else:
        print("Opção invalida!")      

    input("\nAperte enter para voltar ao menu ")

