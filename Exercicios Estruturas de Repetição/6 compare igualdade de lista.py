# Leia 2 listas e retorne quantos valores existem em. ambas a listas
# Dica: nesse caso será necessário um for dentro de outro for

lista1 = [1, 2, 3, 4]
lista2 = [2, 4, 8]
listas = [lista1, lista2]
contador = 0

for lista in listas:
    for item in lista:
        contador += 1

print(contador)        