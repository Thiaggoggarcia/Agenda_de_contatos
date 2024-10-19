def criar_contato():
    contato = []
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    print(f"""
    Favoritar Contato do {nome} ?
    1 - SIM
    2 - NÃO
    """)
    favorito = input("Digite a Opção: \n")
    
    if favorito == "1":
        favorito = True
        print(f"{nome} Foi Adicionado com Favorito!")
        
    elif favorito == "2":
        favorito = False
    else:
        favorito = False
        print("Opção inválida: Contato salvo como não favorito")
    contato.append(nome.strip())
    contato.append(telefone)
    contato.append(email)
    contato.append(favorito)
    
    return contato

def edita_contato(nome, lista_contatos):
    
    for indice,lista in enumerate(lista_contatos):
        if lista[0] == nome.strip():
            print("ESCOLHA O CAMPO A SER ALTERADO ?")
            print(
    """
    1 - NOME
    3 - EMAIL
    2 - TELEFONE
    """)
            opcao = int(input("DIGITE UMA OPÇÃO: "))

            if opcao == 1:
                novo_nome = input("DIGITE O NOVO NOME: ")
                lista[0] = novo_nome
                print("ALTERADO COM SUCESSO!")
                return
            
            elif opcao == 2:
                novo_email = input("DIGITE O NOVO EMAIL: ")
                lista[1] = novo_email
                print("ALTERADO COM SUCESSO!")
                return
            
            elif opcao == 3:
                novo_telefone = input("DIGITE O NOVO NUMERO: ")
                lista[2] = novo_telefone
                print("ALTERADO COM SUCESSO!")
                return
            
            else:
                print("OPÇÃO INVÁLIDA!")

        if indice == len(lista_contatos) - 1: 
            print("CONTATO NÃO LOCALIZADO")

def remover_contato(nome, lista_contatos):
    for indice,lista in enumerate(lista_contatos):             
                
        if lista[0] == nome.strip():
            print(f"REMOVENDO O CONTATO DE {lista[0]}")
            lista_contatos.pop(indice)  
            break
            
        if indice == len(lista_contatos) - 1: 
            print("CONTATO NÃO LOCALIZADO")

lista_de_contatos = []

while True:
    print(
"""          
ESCOLHA UMA DAS OPÇÕES ABAIXO:

1 - ADICIONAR NOVO CONTATO
2 - VISUALIZAR LISTA DE CONTATOS EXISTENTES
3 - EDITAR CONTATO
4 - EXCLUIR CONTATO
5 - FAVORITAR CONTATO
6 - LISTA DE CONTATOS FAVORITOS
7 - SAIR
""")
    try:
        opcao_escolhida = int(input("Digite uma das opções: "))
        
        if opcao_escolhida == 1:
            contato = criar_contato()
            
            print("Novo Contato Adicionado!")
            print(contato)
            
            lista_de_contatos.append(contato)
        
        # VISUALIZAR LISTA DE CONTATOS EXISTENTES
        if opcao_escolhida == 2:
            print("###### LISTA DE CONTATOS ######")
            cont = 1
            for lista in lista_de_contatos:
                print(f"{cont} - {lista}")
                cont += 1
            
        # EDITAR CONTATO
        if opcao_escolhida == 3:
            
            print("QUAL CONTATO DESEJA EDITAR: ")
            pesquisa_nome_contato = input()

            edita_contato(pesquisa_nome_contato,lista_de_contatos)
            
        # REMOVER CONTATO
        if opcao_escolhida == 4:
            if lista_de_contatos == []:
                print("OPERAÇÃO INDISPONÍVEL, LISTA VAZIA!")
                break
            
            remove_nome = input("QUAL CONTATO IRÁ REMOVER? ")

            remover_contato(remove_nome, lista_de_contatos)
            
            for indice_excluir,lista_excluir in enumerate(lista_de_contatos):             
                
                if lista_excluir[0] == remove_nome.strip():
                    print(f"Excluindo o contado de {lista_excluir[0]}")
                    lista_de_contatos.pop(indice_excluir)  
                    break
                  
                if indice_excluir == len(lista_de_contatos) - 1: 
                    print("Contato não localizado")
         
        #FAVORITAR CONTATO
        if opcao_escolhida == 5:
            
            favoritar_nome = input("Qual O Nome Do Contato Que Deseja Adicionar ao Favoritos? ")
            
            for indice_favoritar,lista_favoritar in enumerate(lista_de_contatos):
                
                if lista_favoritar[0] == favoritar_nome.strip():
                    print(f"{lista_favoritar[0]} Foi Adicionado aos Favoritos")
                    lista_favoritar[3] = True 
                    break
                  
                if indice_favoritar == len(lista_de_contatos) - 1: 
                    print("Contato não localizado")
                
        #LISTA DE CONTATOS FAVORITOS
        if opcao_escolhida == 6:
            if lista_de_contatos == []:
                print("Operação indisponível, lista vazia")
                continue
            
            cont = 1
            print("###### LISTA DE CONTATOS FAVORITOS ######")
            for lista_favoritos in lista_de_contatos:             
                
                if lista_favoritos[3] == True:
            
                    for indice_excluir,lista_excluir in enumerate(lista_de_contatos):             
                    
                        if lista_excluir[0] == remove_nome.strip():
                            print(f"Excluindo o contado de {lista_excluir[0]}")
                            lista_de_contatos.pop(indice_excluir)  
                            break
                        
                        if indice_excluir == len(lista_de_contatos) - 1: 
                            print("Contato não localizado")
                            print(f"{cont} - {lista_favoritos}")
                            cont += 1
                  
            if cont == 1: 
                print("Sem Contatos Favoritos")
        
        if opcao_escolhida == 7:
            print("Saindo...")
            break
        
        
    except ValueError as e:
        print("\nmensagem de erro: ", e)