from datetime import date

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

#Função para Adicionar peças
def opcao_1 ():
    #Variável que vai receber a quantidade de peças
    quantidade = int(input("Quantas peças voce gostaria de inserir? \n"))

    #For para adicionar a quantidade de peças informada
    for i in range(quantidade):
        #Abre o arquivo
        arquivo_armario = open("armario.txt", "r")

        #Lê a primeira linha e armazena
        conteudo = arquivo_armario.readline()
        #Transforma conteudo em lista de lista
        list_conteudo = conteudo.split()

        arquivo_armario.close()

        #Abre o arquivo idpecas.txt e armazena na variável
        arquivo_id = open("idpecas.txt", "r")

        #Armazena na variável conteudo_id o conteudo do arquivo
        conteudo_id = arquivo_id.readline()
        #Transforma o conteudo do arquivo de string para int
        cont_id = int(conteudo_id)
        #Acresce em um o valor máximo de ID
        cont_id += 1
        #Transforma de volta em string
        cont_id = str(cont_id)

        arquivo_id.close()

        #Sobrescreve o arquivo com o novo ID máximo
        with open("idpecas.txt", "w") as arquivo_id:
            arquivo_id.write(cont_id)
                
        #Retira a coluna do ID da lista
        list_conteudo.pop(0)

        arq = open("validacao_opt_1.txt", "r")

        list_sit = arq.readlines()
        list_sit = list_sit.pop(2)
        list_sit = list_sit.split()
        del(list_sit[0])
        print(list_sit)

        arq.close()

        #Declara uma lista vazia para acrescentar uma peça
        list_info = []
        #Preenche as informações de cada coluna exceto ID que não recebe entrada do usuário
        for j in range(7):
            print(list_info)
            #IF para quando sitação for = venda ou ficar adiciona - a coluna de preço se não o usuário insere o valor
            if j == 6 and list_info[5][0:6] in list_sit:
                print(len(list_info))
                info = "- "
                list_info.append(info)
            #ELIF para fazer com que o preço seja formatado para float e casas decimais
            '''elif j == 7 and list_info[6] in list_sit:
                print("Digite a informação seguinte: ", list_conteudo[j])
                info = float(input())
                info = round(info, 2)
                info = str(info)
                info = info + " "'''
            else:
                print("Digite a informação seguinte: ", list_conteudo[j])
                info = input()
                info = info + " "
                #Recebe as informações formatada em lista e adiciona a variável
                list_info.append(info)

        #Adiciona um espaço após o ID para formatar
        cont_id = cont_id + " "
        list_info.insert(0, cont_id)

        #Abre o arquivo e insere a peça
        arquivo_armario = open("armario.txt", "a")

        arquivo_armario.write("\n" + "".join(list_info))

        arquivo_armario.close()
    #Volta ao menu principal
    menu_principal()


# def opcao_2():


#Função para remoção de dados
def opcao_3():
    #Chama a função para imprimir o arquivo
    lista_armario = imprimir_arq_arm()

    #Pede o ID da peça a ser removida
    remov_id = int(input("Digite o ID da peça a ser removida: "))

    #For para percorrer as informações
    for i in range(len(lista_armario)-1):
        #Se ID informado for igual ao primeiro elemento da linha na coluna 0 então:
        if str(remov_id) in lista_armario[i][0]:
            #Del para excluir a linha do ID informado
            del (lista_armario[i])

    #Sobrescreve o arquivo com as alterações realizadas e volta ao menu principal
    arq = open("armario.txt", "w")

    arq.writelines(lista_armario)

    arq.close()

    #Pergunta se o usuário deseja excluir outra peça e valida a resposta
    while True:
        remover_outra = input("Deseja remover outra peça? ")
        if remover_outra == 'sim' or remover_outra == 'nao' or remover_outra == 'não':
            break
        else:
            print("Entrada inválida. Digite 'sim' ou 'não'")

    #Se não, vai para o menu principal
    if remover_outra == 'nao' or remover_outra == 'não':
        menu_principal()
    #Se sim, repete a função opcao_3()
    else:
        opcao_3()

#Função para alteração de dados
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

    #Converte de lista de lista para lista de strings
    for i in range(len(lista_armario2)):
        if i == len(lista_armario2) - 1:
            lista_armario2[i] = " ".join(lista_armario2[i])
        else:
            lista_armario2[i] = " ".join(lista_armario2[i]) + "\n"

    #Sobrescreve o arquivo com a informação alterada
    print(lista_armario2)

    arq = open("armario.txt", "w")

    arq.writelines(lista_armario2)

    arq.close()


    #While para tratar as respostas do usuário
    while True:
        alterar_mesma = input("\nVocê gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")

    #Se não, o programa direciona para alteração de outra peça.
    if alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
        #While para tratar as respostas do usuário
        while True:
            alterar_outra = input("Você gostaria de alterar outra peça? ")
            if alterar_outra.lower() == "sim" or alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
                break
            else:
                print("Entrada inválida. Porfavor digitar sim ou não.")
        #Se o usuário digita 'não' ele é direcionado ao menu principal
        if alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
            menu_principal()
        #Se o usuário digita 'sim' ele retorna a função opção_5()
        else:
            opcao_5()
    #Se sim ele executa a função alteração_arm() passando o id_alter e lista_armario2 como parametros.
    else:
        alteracao_arm(id_alter, lista_armario2)



#Função para executar alteração da mesma peça
def alteracao_arm(id_alter, lista_armario2):
    #Inicializa lista_armario3 como vazia para ela receber a lista_armario2 após um split que é feito no FOR.
    lista_armario3 = []

    for i in range(len(lista_armario2)):
        lista_armario3.append(lista_armario2[i].split())

    # Lista para as categorias
    cat = ["1- Tipo","2- Tamanho","3- Padrao",
    "4- Cor","5- Data","6- Situacao", "7- Preco\n"]

    #Printa a lista de categorias
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

    #Converte lista de lista para lista de strings
    for i in range(len(lista_armario3)):
        if i == len(lista_armario3) - 1:
            lista_armario3[i] = " ".join(lista_armario3[i])
        else:
            lista_armario3[i] = " ".join(lista_armario3[i]) + "\n"

    # Sobrescreve o arquivo com a informação alterada
    print(lista_armario3)

    arq = open("armario.txt", "w")

    arq.writelines(lista_armario3)

    arq.close()

    #While para tratar as respostas do usuário
    while True:
        alterar_mesma = input("Você gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")

    #Se não, o programa direciona para alteração de outra peça.
    if alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
        while True:
            alterar_outra = input("Você gostaria de alterar outra peça? ")
            if alterar_outra.lower() == "sim" or alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
                break
            else:
                print("Entrada inválida. Porfavor digitar sim ou não.")
        # Se o usuário digita 'não' ele é direcionado ao menu principal
        if alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
            menu_principal()
        #Se o usuário digita 'sim' ele retorna a função opção_5()
        else:
            opcao_5()
    #Se sim ele executa a função alteração_arm() passando o id_alter e lista_armario3 como parametros.
    else:
        alteracao_arm(id_alter, lista_armario3)




#Função para imprimir o arquivo armario.txt
def imprimir_arq_arm():
    arq = open("armario.txt", "r")
    
    lista_armario = arq.readlines()
    print("".join(lista_armario) + "\n")

    arq.close()

    return lista_armario



def tratamento_preco(j, info, list_conteudo, list_info):

    arq = open("validacao_opt_1.txt", "r")
    list_sit = arq[2].strip()
    arq.close()

    if list_sit[0] == list_info[-1]:
        print("Digite a informação seguinte: ", list_conteudo[j])
        info = float(input())
        info = round(info, 2)
        info = str(info) + " "
        #Recebe as informações formatada em lista e adiciona a variável
        list_info.append(info)
        return list_info
    else:
        info = "-"
        list_info.append(info)
        return list_info



def tratamento_cadastro(j,info):

    #Tipo
    if j == 1:

        arq = open("validacao_opt_1.txt", "r")
        lista_tipos = arq[1].strip()
        arq.close()

        info = info.lower().strip()
        while True:
            if info not in lista_tipos:
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")
                info = input("Digite o tipo da peça: ")
                info = info.lower().strip()
            else:
                return info

    #Tamanho
    if j == 2:
        info = info.lower().strip()
        while True:
            if info != 'p' or info != 'm' or info != 'g':
                print("Entrada inválida. Informe se é p, m ou g!")
                info = input("Digite o tamanho da peça: ")
                info = info.lower().strip()
            else:
                return info

    #Padrão
    if j == 3:
        info = info.lower().strip()
        while True:
            if info != 'masculino' or info != 'feminino' or info != 'unissex':
                print("Entrada inválida. Informe se é masculino, feminino ou unissex!")
                info = input("Digite o padrão da peça: ")
                info = info.lower().strip()
            else:
                return info

    #Cor
    if j == 4:

        arq = open("validacao_opt_1.txt", "r")
        lista_cores = arq[0].strip()
        arq.close()

        info = info.lower().strip()
        while True:
            if info not in lista_cores:
                print("Entrada inválida. Informe uma cor presente na lista!")
                print("\n " * lista_cores)
                info = input("\nDigite a cor da principal da peça: ")
                info = info.lower().strip()
            else:
                return info

    #TRATAMENTO DE DADOS DIA/MES/ANO
    if j == 5:
        info = info.lower().strip()
        while True:
            if info != 'superior' or info != 'inferior' or info != 'calcado' or info != 'calçado':
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")
                info = input("Digite o tipo da peça: ")
                info = info.lower().strip()
            else:
                return info

    #Situação
    if j == 6:

        arq = open("validacao_opt_1.txt", "r")
        lista_sit = arq[2].strip()
        arq.close()

        info = info.lower().strip()
        while True:
            if info not in lista_sit:
                print("Entrada inválida. Informe se é venda, doação ou ficar!")
                info = input("Digite a situação da peça: ")
                info = info.lower().strip()
            else:
                return info

    #TRATAMENTO DE PREÇO(TRATAR TAMBÉM QUANDO PEÇA É PARA DOAÇÃO E PULAR O PREÇO)
    if j == 7:
        info = info.lower().strip()
        while True:
            if info != 'superior' or info != 'inferior' or info != 'calcado' or info != 'calçado':
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")
                info = input("Digite o tipo da peça: ")
                info = info.lower().strip()
            else:
                return info

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
menu_principal()

'''TRATAMENTO PARA PREÇO DA PEÇA SE TIVER PREÇO str(float(round(info,2)))'''