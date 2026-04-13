# SOBRE A APLICAÇÃO
# Desenvolva um CRUD de produtos utilizando while no menu e 
# for para listar ou buscar produtos
# Apenas serão permitidos os métodos de lista 
# append (adicionar) e pop (remover a partir de um índice)
# A aplicação deve ser executada até que o valor da opção seja 0
# Caso o valor da opção não exista, informar ao usuário


# DADOS
# O produto deve ter os dados Nome (string) e Preço (float)


# FUNCIONALIDADES
# O sistema deve ter as funções:

# 1 - listarProdutos: Retorna todos os produtos cadastrados 
#       > Dados de entrada: nenhum
#       > Leia todos os produtos
#       > Retorno: lista de produtos

# 2 - adicionarProduto: 
#       > Dados de entrada: dict Produto(nome, preco)
#       > Adiciona um produto (use append)
#       > Retorno: True ou False

# 3 - buscarProduto: 
#       > Dados de entrada: nome do produto (string)
#       > Retorne o índice do produto encontrado, ou None se não for encontrado nenhum item
#       > Retorno: o índice do produto

# 4 - atualizarProduto: Atualiza os dados de um produto
#       > Dados de entrada: índice (int), dict do novo Produto(nome, preco)
#       > Atualiza os dados de um produto já existente
#       > Retorno: True ou False

# 5 - removerProduto: Dado o índice do produto, ele deve ser removido da lista 
#       > Dados de entrada: índice (int)
#       > Remove o produto do índice
#       > Retorno: True ou False

# IMPORTANTE: Ignore os erros de execução. Em funções como atualizar e remover, apenas passe como
# parâmetros índices de produtos existentes.


produtos = [
    {"nome": "iphone 15", "preco": 4500.00},
    {"nome": "macbook air", "preco": 8500.00},
    {"nome": "playstation 5", "preco": 3800.00},
    {"nome": "kindle paperwhite", "preco": 750.00},
    {"nome": "monitor gamer", "preco": 1200.50}
] #Exemplo de item {nome: Arroz, preco: 30.00}


# 1 - listarProdutos: Retorna todos os produtos cadastrados 
#       > Dados de entrada: nenhum
#       > Leia todos os produtos
#       > Retorno: lista de produtos
def listarProdutos():
        if(len(produtos) == 0):
            print('Não tem produtos cadastrados')
            return produtos
        for indice, p in enumerate(produtos):
            print(f'{indice+1} - {p["nome"].capitalize()} ... R$ {p["preco"]:.2f}')
        return produtos

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# 2 - adicionarProduto: 
#       > Dados de entrada: dict Produto(nome, preco)
#       > Adiciona um produto (use append)
#       > Retorno: True ou False
def adicionarProduto(produto):
    produtos.append(produto)
    return True

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# 3 - buscarProduto: 
#       > Dados de entrada: nome do produto (string)
#       > Retorne o índice do produto encontrado, ou None se não for encontrado nenhum item
#       > Retorno: o índice do produto
def buscarProduto(produtoNome):
    for indice, p in enumerate(produtos):
        if produtoNome == p["nome"]:
            print(f"O produto de n°{indice+1} {p['nome'].capitalize()} - foi encontado!") 
            return indice

    print("Produto informado não foi encontrado!")
    return None

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# 4 - atualizarProduto: Atualiza os dados de um produto
#       > Dados de entrada: índice (int), dict do novo Produto(nome, preco)
#       > Atualiza os dados de um produto já existente
#       > Retorno: True ou False
def atualizarProduto(indice, produto):
    if indice <= len(produtos):
        produtos[indice-1] = produto 
        return True
    else:
        print("Produto não encontrado, nada foi atualizado.")
        return False

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# 5 - removerProduto: Dado o índice do produto, ele deve ser removido da lista 
#       > Dados de entrada: índice (int)
#       > Remove o produto do índice
#       > Retorno: True ou False
def removerProduto(indice):
    if indice <= len(produtos):
        produtos.pop(indice-1)
        print("Produto removido")
        return True
    else:
        print(f"Produto {indice} não encontrado, nada foi removido")  
        return False 

#----------------------------------------------------------------------------------------------------------------------------------------------------------

opcao = None
while(opcao != '0'):
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Listar Produtos')
    print('2 - Adicionar Produto')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('0 - Sair')
    print('========================================')
    
    if(opcao == '1'): 
        print()
        print('LISTA DE PRODUTOS ========================')
        listarProdutos()
    
    elif(opcao == '2'): 
        print()
        print('ADICIONAR DE PRODUTOS ==================')
        nome = input('Nome: ').lower()
        preco = float(input('Preço: '))
        adicionarProduto({'nome': nome, 'preco': preco})
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '3'): 
         print('BUSCAR PRODUTO =========================')
         produtoNome = input("Informe o nome do produto: ").lower()
         buscarProduto(produtoNome)
    
    elif(opcao == '4'): 
         print('ATUALIZAR PRODUTO ======================')
         listarProdutos()
         print("========================================")
         print("")

         indice = int(input("Informe o indice/número do produto: "))
         novo_nome = input("Novo nome: ").lower()
         novo_valor = float(input("Novo Valor: "))
         produto = {"nome": novo_nome, "preco": novo_valor} 
         atualizarProduto(indice, produto)

         print("")
         print('LISTA ATUALIZADA =======================')
         listarProdutos()
         print("========================================")
         print("")
    
    elif(opcao == '5'): 
         print('REMOVER PRODUTO ========================')
         listarProdutos()
         print("========================================")
         print("")

         indice = int(input("Informe o indice/número do item: "))
         removerProduto(indice)

         print("")
         print('LISTA ATUALIZADA =======================')
         listarProdutos()
         print("========================================")
         print("")
    
    elif(opcao != None): 
        print('Opção não existe')    
    
    print()
    opcao = input('Opção desejada: ')