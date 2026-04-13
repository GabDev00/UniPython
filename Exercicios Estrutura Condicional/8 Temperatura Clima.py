# Exercício 8
# Leia uma temperatura e classifique: frio (<15), ameno (15-25), quente (>25).

# escreva seu código abaixo

temperatura = float(input("Informe a temperatura: "))

# if temperatura <15:
#     print("A Clima está Frio")
# elif temperatura < 26:
#     print("O clima está Ameno")    
# else:
#     print("O Clima está Quante")    

def ler_temperatura(temperatura):
    if temperatura <= 15:
        return f"{temperatura}°c A temperatura está frio"
    elif temperatura <=25:
        return f"{temperatura}°c A temperatura está amena"
    else:
        return f"{temperatura}°c A temperatura está quente"
    
print(ler_temperatura(temperatura))    