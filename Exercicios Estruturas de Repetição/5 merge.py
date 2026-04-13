# Leia 2 listas e retorne uma única lista juntando ambas, mas sem alterar as listas de entrada.
# Dica: precisará de uma nova lista que acumulará valores ao longo do processo
# Não utilize .extende()

numeros_inteiros = [4, 5, 6]
numeros_inteiros2 = [1, 2, 3]
nova_lista = []

for n in numeros_inteiros:
    nova_lista.append(n)
for n2 in numeros_inteiros2:
    nova_lista.append(n2)    

print(nova_lista)

nova_lista.sort()
print(f"nova lista: {nova_lista}")