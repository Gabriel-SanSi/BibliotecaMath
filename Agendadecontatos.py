import os # modulo os fornece funções para interagir com sistema operacional

#função carrega arquivo de contatos se tiver algum
def carregar_contatos():
    contatos = {}
    if os.path.exists("contatos.txt"):
        with open("contatos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, telefone, email = linha.strip().split(",")
                contatos[nome] = {"telefone": telefone, "email": email}

    return contatos # retornar a lista


def salvar_contatos(contatos):
    with open("contatos.txt", "w") as arquivo:
        for nome, dados in contatos.itens():
            arquivo.write(f"{nome};{dados['telefone']};{dados['email']}\n")

#função adicionar um contato
def adicionar_contatos(contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contatos {nome} adicionado com sucesso!")


#função para remover um contatos
def remove_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ")
    if nome in contatos: #se tiver o contato, então remove
        del contatos[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:#se não tiver, não faz nada
        print("Contato não encontrado")

#função para atualizar um contato
def atualizar_contato(contatos):
    nome = input("Digite o nome do contato a ser atualizado: ")
    if nome in contatos:
        telefone = input("Digite o novo  telefone: ")
        email = input("Digite o novo email: ")
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"Contatos {nome} atualizado com sucesso!")
    else:
        print("Nenhum contato cadastrado.")

#função para exibir todos os contatos
def exibir_contatos(contatos):
    if contatos:
        for nome, dados in contatos.itens():
            print(f"Nome: {nome}, telefone: {dados['telefone']}, email: {dados['email']}")
        else:
            print("Nenhum contatos cadastrodo.")

    #menu principal
def menu():
    contatos = carregar_contatos()
    
    while True: #while True em Python é uma estrutura de loop que cria um loop infinito
        print("\n1. Adicionar contato")
        print("2. Remover contato")
        print("3. Atualizar contato")
        print("4. Exibir contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contatos(contatos)
        elif opcao == "2":
            remove_contato(contatos)
        elif opcao == "3":
            atualizar_contato(contatos)
        elif opcao == "4":
            exibir_contatos(contatos)
        elif opcao == "5":
            salvar_contatos(contatos)
            print("Contatos salvos. Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    menu()