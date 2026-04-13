# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

# escreva seu código abaixo

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

# if media >= 7:
#     print("Aluno Aprovado!")
# else:
#     print("Aluno Reprovado!")  
 
# print(media)    

def aprovado_reprovado(nota1, nota2):
    if media >= 7:
        return f"Aprovado, media: {media}"
    else:
        return f"Reprovado, media: {media}"
    

print(aprovado_reprovado(nota1,nota2))