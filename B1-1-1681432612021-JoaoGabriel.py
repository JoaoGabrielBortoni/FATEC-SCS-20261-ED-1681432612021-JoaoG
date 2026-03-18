'''
*----------------------------------------------------------------------------------*
*                           FATEC São Caetano do Sul                               *
*                                Atividade B1 - 1                                  *
*  Autor: 1681432612021 - João Gabriel Bortoni                                     *
*  Objetivo: Executar operações de cadastro, busca, remoção e listagem de filmes   *
*  Data: 24/02/2026                                                                *
*----------------------------------------------------------------------------------*
'''


catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
       
       if id_filme in catalogo:
        print("\n O Filme ja está no catálogo")
       else:
        catalogo[id_filme] = {titulo, diretor}
        print("\n Filme Adicionado com Sucesso!")

def buscar_filme(id_filme):
    if id_filme not in catalogo:
        print("\n Esse Filme não está no catálogo")
    else:
        print(catalogo.get(id_filme))

def remover_filme(id_filme):
    if id_filme not in catalogo:
        print("\n Esse Filme não está no catálogo")
    else:
        catalogo.pop(id_filme)

def listar_todos():
    if not catalogo:
        print("\n --- Catalogo está vazio ---")
    else :
        print("\n --- Listagem de Filme ---") 
        for id_filme in catalogo.items():
          print(f"ID: {id_filme} | Titulo: {titulo} | Diretor: {diretor}")

      
while True:
         print("\n--- Menu de Opcoes ---")
         print("1. Adicionar Filme")
         print("2. Buscar Filme")
         print("3. Remover Filme")
         print("4. Listar Todos os Filmes")
         print("5. Sair")

         opcao = input("Escolha uma opcao: ")

         if opcao == "1":
              id_filme = input("Digite o ID: ")
              titulo = input("Digite o Título: ")
              diretor = input("Digite o Diretor: ")

              adicionar_filme(id_filme, titulo, diretor)

         if opcao == "2":
             id_filme = input("Digite o ID: ")
             buscar_filme(id_filme)

         if opcao == "3":
             id_filme = input("Digite o ID: ")
             remover_filme(id_filme)

         if opcao == "4":
             listar_todos()

         if opcao == "5":
            exit() 
          