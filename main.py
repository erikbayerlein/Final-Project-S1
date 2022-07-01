def opcao_1 ():
    quantidade = int(input("Quantas peças voce gostaria de inserir?"))
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

    return quantidade, info

#def opcao_2():



def opcao_3():
    with open("armario.txt", "r") as arquivo_armario:
        armario = "".join(arquivo_armario.readlines())
        print (armario)
        remov_id = int(input("Digite o ID da peça que você gostaria de remover: "))
        with open("armario.txt", "r") as arquivo_armario2:
            arquivo_armario3 = list(arquivo_armario2)
            arquivo_armario3.pop(remov_id)
            with open("armario.txt", "w") as arquivo:
                arquivo.write("".join(arquivo_armario3))


    return 


#def opcao_4():

#def opcao_5():

#def opcao_6():



#MENU DE ESCOLHA (FUNCAO MENU)
def menu_principal():

    titulos = ["1- Inserir nova peça","2- Inserir novo estilo","3- Remover peça",
    "4- Remover estilo","5- Alterar peça","6- Procurar peça", "7- Finalizar programa"]

    for i in range(7):
        print(titulos[i])

    while True:
        opcao_escolhida = int(input("Digite um número correspondente a opção do menu: "))
        if opcao_escolhida < 1 or opcao_escolhida > 7:
            print("Entrada inválida. Digite um número válido.")
        else:
            break
    
    if opcao_escolhida == 1:
        opcao_1()
    
    elif opcao_escolhida == 3:
        opcao_3()

    return opcao_escolhida
'''
    elif opçao_escolhida == 2:
        #inserir novo estilo

    elif opçao_escolhida == 4:
        #remover estilo

    elif opçao_escolhida == 5:
        #alterar peca

    elif opçao_escolhida == 6:
        #procurar peça

    elif opçao_escolhida == 7:
        exit()
    '''


#VARIAVEIS

opcao_escolhida = menu_principal()