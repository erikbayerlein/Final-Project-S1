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


#def opcao_2():



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
    lista_armario = imprimir_arq_arm()
    
    cat = ["1- Tipo","2- Tamanho","3- Padrao",
    "4- Cor","5- Data","6- Situacao", "7- Preco", "8- Estilos\n"]


    id_alter = int(input("Digite o ID da peça a ser alterada: "))
    
    for i in range(8):
        print(cat[i])


    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    alteracao = input("Digite a nova informação: ")

    lista_armario2 = []

    for i in range(len(lista_armario)-1):
        lista_armario2.append(lista_armario[i].split())
    print(lista_armario2)

    for i in range(len(lista_armario2)-1):
        for j in range(len(lista_armario2))
        if str(id_alter) in lista_armario2[i][0]:
            lista_armario2.pop([i][cat_alter])
            lista_armario2.insert([i][cat_alter], alteracao)
    print(lista_armario2)



def imprimir_arq_arm():
    arq = open("armario.txt", "r")
    
    lista_armario = arq.readlines()
    print("".join(lista_armario) + "\n")

    arq.close()

    return lista_armario









#def opcao_4():

#def opcao_6():



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