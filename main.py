from tkinter import N


def menu_principal():

    titulos = ["1- Inserir nova peça","2- Inserir novo estilo","3- Remover peça",
    "4- Remover estilo","5- Alterar peça","6- Procurar peça", "7- Finalizar programa"]

    for i in range(7):
        print(titulos[i])

    while True:
        opcao_escolhida = int(input("\nDigite um número correspondente a opção do menu: "))
        if opcao_escolhida < 1 or opcao_escolhida > 7:
            print("Entrada inválida. Digite um número válido.\n")
        else:
            break
    
    if opcao_escolhida == 1:
        opcao_1()
    
    elif opcao_escolhida == 3:
        opcao_3()

    elif opcao_escolhida == 5:
        opcao_5()

    elif opcao_escolhida == 7:
        exit()


def opcao_1 ():
    quantidade = int(input("Quantas peças voce gostaria de inserir? \n"))
    for i in range(quantidade):
        arquivo_armario = open("armario.txt", "r")

        conteudo = arquivo_armario.readline()
        list_conteudo = conteudo.split()

        arquivo_armario.close()

        arquivo_id = open("idpecas.txt","r")

        conteudo_id = arquivo_id.readline()
        cont_id = int(conteudo_id)
        cont_id += 1
        cont2_id = str(cont_id)

        arquivo_id.close()

        with open("idpecas.txt","w") as arquivo_id:
            arquivo_id.write(cont2_id)
                

        list_conteudo.pop(0)

        list_info = []
        for j in range(7):
            print("Digite a informação seguinte: ", list_conteudo[j])
            info = input()
            info2 = info + " "
            list_info.append(info2)
        id_str = str(cont_id) + " "
        list_info.insert(0, id_str)

        arquivo_armario = open("armario.txt","a")

        arquivo_armario.write("\n" + "".join(list_info))

        arquivo_armario.close()

    menu_principal()


# def opcao_2():



def opcao_3():
    lista_armario = imprimir_arq_arm()

    remov_id = int(input("Digite o ID da peça a ser removida: "))

    for i in range(len(lista_armario)-1):
        if str(remov_id) in lista_armario[i][0]:
            del (lista_armario[i])
    
    arq = open("armario.txt", "w")

    arq.writelines(lista_armario)

    arq.close()

    menu_principal()


def opcao_5():
    #Mostrar as peças presentes no armário
    lista_armario = imprimir_arq_arm()
    
    #Lista para as categorias 
    cat = ["1- Tipo","2- Tamanho","3- Padrao",
    "4- Cor","5- Data","6- Situacao", "7- Preco\n"]

    #ID para localizar a peça a ser alterada
    id_alter = int(input("Digite o ID da peça a ser alterada: "))
    
    #Imprimir a lista de categorias
    for i in range(7):
        print(cat[i])

    #Digitar o número da opção a ser alterada
    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    #Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    #Criação de uma lista para conter todo o armário em forma de lista de strings
    lista_armario2 = []

    #Preenchimento da lista
    for i in range(len(lista_armario)):
        lista_armario2.append(lista_armario[i].split())

    #For para percorrer a lista de strings e substituir a informação antiga pela nova
    for i in range(len(lista_armario2)):
        #Se o ID da peça estiver na linha verificada, então
        if str(id_alter) in lista_armario2[i][0]:
            #O elemento da lista na linha i e na coluna cat_alter(característica a ser alterada) irá receber a alteração
            #através do método replace
            lista_armario2[i][cat_alter] = lista_armario2[i][cat_alter].replace(lista_armario2[i][cat_alter], alteracao)

    for i in range(len(lista_armario2)):
        if i == len(lista_armario2) - 1:
            lista_armario2[i] = " ".join(lista_armario2[i])
        else:
            lista_armario2[i] = " ".join(lista_armario2[i]) + "\n"


    print(lista_armario2)

    arq = open("armario.txt", "w")

    arq.writelines(lista_armario2)

    arq.close()



    while True:
        alterar_mesma = input("\nVocê gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")


    if alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
        while True:
            alterar_outra = input("Você gostaria de alterar outra peça? ")
            if alterar_outra.lower() == "sim" or alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
                break
            else:
                print("Entrada inválida. Porfavor digitar sim ou não.")
        if alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
            menu_principal()   
        else:
            opcao_5()

    else:
        alteracao_arm(id_alter, lista_armario2)




def alteracao_arm(id_alter, lista_armario2):

    lista_armario3 = []

    for i in range(len(lista_armario2)):
        lista_armario3.append(lista_armario2[i].split())


    cat = ["1- Tipo","2- Tamanho","3- Padrao",
    "4- Cor","5- Data","6- Situacao", "7- Preco\n"]

    for i in range(7):
        print(cat[i])

    #Digitar o número da opção a ser alterada
    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    #Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    #For para percorrer a lista de strings e substituir a informação antiga pela nova
    for i in range(len(lista_armario3)):
        #Se o ID da peça estiver na linha verificada, então
        if str(id_alter) in lista_armario3[i][0]:
            #O elemento da lista na linha i e na coluna cat_alter(característica a ser alterada) irá receber a alteração
            #através do método replace
            lista_armario3[i][cat_alter] = lista_armario3[i][cat_alter].replace(lista_armario3[i][cat_alter], alteracao)


    for i in range(len(lista_armario3)):
        if i == len(lista_armario3) - 1:
            lista_armario3[i] = " ".join(lista_armario3[i])
        else:
            lista_armario3[i] = " ".join(lista_armario3[i]) + "\n"


    print(lista_armario3)

    arq = open("armario.txt", "w")

    arq.writelines(lista_armario3)

    arq.close()
    

    while True:
        alterar_mesma = input("Você gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")


    if alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
        while True:
            alterar_outra = input("Você gostaria de alterar outra peça? ")
            if alterar_outra.lower() == "sim" or alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
                break
            else:
                print("Entrada inválida. Porfavor digitar sim ou não.")
        if alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
            menu_principal()   
        else:
            opcao_5()

    else:
        alteracao_arm(id_alter, lista_armario3)





def imprimir_arq_arm():
    arq = open("armario.txt", "r")
    
    lista_armario = arq.readlines()
    print("".join(lista_armario) + "\n")

    arq.close()

    return lista_armario









# def opcao_4():

# def opcao_6():



#MENU DE ESCOLHA (FUNCAO MENU)


'''
    elif opçao_escolhida == 2:
        #inserir novo estilo

    elif opçao_escolhida == 4:
        #remover estilo

    elif opçao_escolhida == 6:
        #procurar peça

        '''


#VARIAVEIS

opcao_escolhida = menu_principal()