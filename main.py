################# Importações de bibliotecas #################
from datetime import date
################# ########################## #################


################ FUNÇÕES PRINCIPAIS #################

# Função para chamar o menu principal
def menu_principal():

    # Inicializa uma variável que vai mostrar as opções do menu principal
    titulos = ["1- Inserir nova peça", "2- Inserir novo estilo ou adicionar peça a um estilo", "3- Remover peça",
               "4- Remover estilo", "5- Alterar peça", "6- Procurar peça", "7- Selecionar estilo", "8- Finalizar programa"]

    print("\n**************** ARMÁRIO VIRTUAL ****************\n")

    for i in range(8):
        print(titulos[i])

    #Aqui sera tratada a entrada do usuário quanto a opção escolhida
    while True:
        opcao_escolhida = int(input("\nDigite um número correspondente a opção do menu: "))
        if opcao_escolhida >= 1 and opcao_escolhida <= 8:
            break
        else:
            print("Entrada inválida. Digite um número válido.\n")

    # IF que seleciona qual função a ser executada
    if opcao_escolhida == 1:
        opcao_1()

    elif opcao_escolhida == 2:
        opcao_2()

    elif opcao_escolhida == 3:
        opcao_3()

    elif opcao_escolhida == 4:
        opcao_4()

    elif opcao_escolhida == 5:
        opcao_5()

    elif opcao_escolhida == 6:
        opcao_6()

    elif opcao_escolhida == 7:
        opcao_7()

    elif opcao_escolhida == 8:
        exit()

#----------------------------------------------------

# Função para Adicionar peças
def opcao_1():
    # Variável que vai receber a quantidade de peças
    quantidade = int(input("Quantas peças voce gostaria de inserir? \n"))

    # For para adicionar a quantidade de peças informada
    for i in range(quantidade):
        # Abre o arquivo
        arquivo_armario = open("armario.txt", "r")

        # Lê a primeira linha e armazena
        conteudo = arquivo_armario.readline()
        # Transforma conteudo em lista de lista
        list_conteudo = conteudo.split()

        arquivo_armario.close()

        # Abre o arquivo idpecas.txt e armazena na variável
        arquivo_id = open("idpecas.txt", "r")

        # Armazena na variável conteudo_id o conteudo do arquivo
        conteudo_id = arquivo_id.readline()
        # Transforma o conteudo do arquivo de string para int
        cont_id = int(conteudo_id)
        # Acresce em um o valor máximo de ID
        cont_id += 1
        # Transforma de volta em string
        cont_id = str(cont_id)

        arquivo_id.close()

        # Sobrescreve o arquivo com o novo ID máximo
        with open("idpecas.txt", "w") as arquivo_id:
            arquivo_id.write(cont_id)

        # Retira a coluna do ID da lista
        list_conteudo.pop(0)

        # Lista para guardar a validação de situação para quando não há venda
        arq = open("validacao_opt_1.txt", "r")

        list_sit = arq.readlines()
        list_sit = list_sit.pop(2)
        list_sit = list_sit.split()
        del (list_sit[0])

        arq.close()

        # Declara uma lista vazia para acrescentar uma peça
        list_info = []
        # Preenche as informações de cada coluna exceto ID que não recebe entrada do usuário
        for j in range(7):
            ## TRATAMENTO DE DATA ##
            if j == 4:
                info = tratamento_data()
                info = info + " "
                # Recebe as informações formatada em lista e adiciona a variável
                list_info.append(info)

            # IF para quando situação = doação ou ficar adiciona - a coluna de preço se não o usuário insere o valor
            elif j == 6 and (list_info[5][0:6] in list_sit or list_info[5][0:5] in list_sit):
                info = "- "
                list_info.append(info)

            # ELIF para quando situação = venda recebe do usuário a entrada em float, formata e insere
            elif j == 6 and list_info[5][0:5] == 'venda':
                print("Digite a informação seguinte: ", list_conteudo[j])
                info = float(input())
                info = round(info, 2)
                info = str(info)
                info = info + " "
                list_info.append(info)

            # Todos os outros casos
            else:
                print("Digite a informação seguinte: ", list_conteudo[j])
                info = input()
                info = tratamento_cadastro(j, info)
                info = info + " "
                # Recebe as informações formatada em lista e adiciona a variável
                list_info.append(info)

        # Adiciona um espaço após o ID para formatar
        cont_id = cont_id + " "
        list_info.insert(0, cont_id)
        list_info.insert(8,"-")

        # Abre o arquivo e insere a peça
        arquivo_armario = open("armario.txt", "a")
        arquivo_armario.write("\n" + "".join(list_info))
        arquivo_armario.close()
        
    # Volta ao menu principal
    menu_principal()

#----------------------------------------------------

# Função para Adicionar estilos
def opcao_2():

    # Cria uma lista com as opções disponiveis na função adicionar estilos e as printa em sequência
    opcoes = ["1- Criar estilo", "2- Inserir peça a um estilo", "3- Voltar ao menu principal"]

    for i in opcoes:
        print(i)

    # Validação de dados
    while True:
        opcao_escolhida = int(input("\nDigite um número correspondente a opção do menu: \n"))
        if opcao_escolhida >= 1 and opcao_escolhida <= 3:
            break
        else:
            print("Entrada inválida. Digite um número válido.\n")

    # Se opção 1 escolhida, o usuário irá criar um novo nome de estilo
    if opcao_escolhida == 1:

        nome = input("Digite o nome do estilo: ")
        new_estilo = f"NOME = {nome.lower()}; CONTADOR = 0; PECAS = "

        # Abre o arquivo e adiciona o novo estilo criado
        arq = open("estilos.txt", "a")
        arq.write("\n" + new_estilo)
        arq.close()

        opcao_2()

    # Se opção 2 escolhida o usuário irá adicionar uma peça em algum dos estilos já criados ou disponíveis
    elif opcao_escolhida == 2:

        # le e guarda o arquivo estilos.txt em nome_estilos
        arq = open("estilos.txt", "r")
        nomes_estilos = arq.readlines()
        arq.close()

        # os elementos de nome_estilos são transformados em dicionários e são armazenados em lista_dic
        lista_dic = []
        for i in nomes_estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)
        
        # lista_comp_nomes recebe apenas os nomes dos estilos
        lista_comp_nomes = []
        for i in range(len(lista_dic)):
            lista_comp_nomes.append(lista_dic[i]["NOME "])


        # while true para verificar a existência do nome dentro de lista_comp_nomes
        while True:
            # Pede a entrada do usuário para saber em qual estilo ele quer adicionar
            nome_estilo = input("Em qual estilo você gostaria de adicionar? ")
            if " " + nome_estilo.lower() in lista_comp_nomes:
                break
            else:
                print("Digite um nome de estilo válido.")
                print(*lista_comp_nomes)

        print("\n")

        lista_arm = imprimir_arq_arm()


        # Agora ele informa o ID da peça que passará a ser daquele estilo
        id_peca = input("Digite o ID da peça a ser adicionada: ")

        # Pegaremos o arquivo armario transformamos em lista e iremos comparar a entrada do usuário com os IDs já presentes na lista
        lista_arm_2 = []
        for i in range(len(lista_arm)):
            lista_arm_2.append(lista_arm[i].split())

        for i in range(len(lista_arm_2)):
            # Se a entrada estiver na lista na coluna dos IDs então nos armazenamos a linha correspondente em 'peca'
            if id_peca in lista_arm_2[i][0]:
                peca = lista_arm[i]

        # Retira \n e - (estilo vazio)
        peca = peca[0:-2]

        # Abrimos o arquivo de estilos para armazenar as informações dele em 'lista_estilos'
        arq = open("estilos.txt", "r")
        lista_estilos = arq.readlines()
        arq.close()

        # For para dar split nas string dos dicionario
        lista_dic = []
        for i in lista_estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)

        # se o estilo referido é o ultimo não há qubra de linha
        if lista_dic[-1]['NOME '] == " " + nome_estilo:     
            # For para adicionar a peça ao estilo informado
            for i in range(len(lista_dic)):
                if lista_dic[i]['NOME '] == " " + nome_estilo:
                    peca = " " + peca + "|"       
                    lista_estilos[i] = lista_estilos[i][:-1] + peca
        
        # se o estilo referido não é o útilmo
        else:
            # For para adicionar a peça ao estilo informado
            for i in range(len(lista_dic)):
                if lista_dic[i]['NOME '] == " " + nome_estilo:
                    peca = " " + peca + "|"       
                    # recorte no -1 para cortar o \n ja existente
                    lista_estilos[i] = lista_estilos[i][:-1] + peca + "\n"


        # Sobrescreve o arquivo com a peça já adicionada
        arq = open("estilos.txt", "w")
        arq.writelines(lista_estilos)
        arq.close()


        ########### Alterar estilo no armário

        lista_armario2 = []

        # Preenchimento da lista
        for i in range(len(lista_arm)):
            lista_armario2.append(lista_arm[i].split())

        # For para percorrer a lista de strings e substituir a informação antiga pela nova
        for i in range(len(lista_armario2)):
            # Se o ID da peça estiver na linha verificada, então
            if str(id_peca) in lista_armario2[i][0]:
                # O elemento da lista na linha i e na coluna cat_alter(característica a ser alterada) irá receber a alteração
                # através do método replace
                lista_armario2[i][8] = lista_armario2[i][8].replace(lista_armario2[i][8], nome_estilo)

        # Converte de lista de lista para lista de strings
        for i in range(len(lista_armario2)):
            if i == len(lista_armario2) - 1:
                lista_armario2[i] = " ".join(lista_armario2[i])
            else:
                lista_armario2[i] = " ".join(lista_armario2[i]) + "\n"

        # Sobrescreve o arquivo com a informação alterada
        arq = open("armario.txt", "w")
        arq.writelines(lista_armario2)
        arq.close()


        opcao_2()

    # Se opção 3 escolhida, volta ao menu principal
    elif opcao_escolhida == 3:
        menu_principal()

#----------------------------------------------------

# Função para Remoção de dados
def opcao_3():

    # Chama a função para imprimir o arquivo
    lista_armario = imprimir_arq_arm()

    # Abre o arquivo e o armazena em lista_trat
    arq = open("armario.txt", "r")
    lista_trat = arq.readlines()
    arq.close()

    # lista_trat recebe as linhas divididas
    for i in range(len(lista_trat)):
        lista_trat[i] = lista_trat[i].split()

    # salva apenas os IDs de cada roupa
    for i in range(len(lista_trat)):
        lista_trat[i] = lista_trat[i][0]
        lista_trat[i].strip()
    
    # pop na string "ID"
    lista_trat.pop(0)

    # while true verificando a entrada com a lista de IDs existentes
    while True:
        remov_id = int(input("Digite o ID da peça a ser removida: "))
        if str(remov_id) in lista_trat:
            break
        else:
            print("Entrada inválida. Digite um ID existente.")
            print(*lista_trat)

    # For para percorrer as informações
    for i in range(len(lista_armario) - 1):
        # Se ID informado for igual ao primeiro elemento da linha na coluna 0 então:
        if str(remov_id) in lista_armario[i][0]:
            # Salva a linha a ser removida em uma variavel para ser gaurdada no histórico
            historico = lista_armario[i]
            # Del para excluir a linha do ID informado
            del (lista_armario[i])

    # Variável que vai receber a informação para quem foi vendida ou doada a peça
    para = input("Digite para quem foi vendida ou doada: ")

    #Adiciona a informação a linha da peça e recorte no -1 para tirar \n
    historico = "\n" + historico[:-1] + " " + para

    print(historico)
    
    # Sobrescreve o arquivo com as alterações realizadas e volta ao menu principal
    arq = open("armario.txt", "w")
    arq.writelines(lista_armario)
    arq.close()

    # Append da peça retirada no histórico
    arq = open("historico.txt", "a")
    arq.write(historico)
    arq.close()

    # Pergunta se o usuário deseja excluir outra peça e valida a resposta
    while True:
        remover_outra = input("Deseja remover outra peça? ")
        if remover_outra == 'sim' or remover_outra == 'nao' or remover_outra == 'não':
            break
        else:
            print("Entrada inválida. Digite 'sim' ou 'não'")

    # Se não, vai para o menu principal
    if remover_outra == 'nao' or remover_outra == 'não':
        menu_principal()

    # Se sim, repete a função opcao_3()
    else:
        opcao_3()

#----------------------------------------------------

# Função para Remoção de estilos
def opcao_4():

    lista_armario = imprimir_arq_arm()

    # Abre o arquivo e o armazena na variavel estilos
    arq = open("estilos.txt", "r")
    estilos = arq.readlines()
    arq.close()

    # Abre o arquivo e o armazena na variavel nome_estilos para o tratamento
    arq = open("estilos.txt", "r")
    nomes_estilos = arq.readlines()
    arq.close()

    # Split na lista de estilos (separa nos ;)
    for i in range(len(estilos)):
        estilos[i] = estilos[i].split(";")

    # Print na lista dos estilos (printa somente os nomes)
    for i in range(len(estilos)):
        print(estilos[i][0])

    # os elementos de nome_estilos são transformados em dicionários e são armazenados em lista_dic
    lista_dic = []
    for i in nomes_estilos:
        dictionary = dict(subString.split("=") for subString in i.split(";"))
        lista_dic.append(dictionary)

    #lista_comp_nomes recebe apenas os nomes dos estilos
    lista_comp_nomes = []
    for i in range(len(lista_dic)):
        lista_comp_nomes.append(lista_dic[i]["NOME "])

    # while true para verificar a existência do nome dentro de lista_comp_nomes
    while True:
        # Pede a entrada do usuário para saber qual estilo ele quer remover
        remov_estilo = input("\nDigite o nome do estilo a ser removido: ")
        if " " + remov_estilo.lower() in lista_comp_nomes:
            break
        else:
            print("Digite um nome de estilo válido.")
            print(*lista_comp_nomes)
    
    # For para procurar o estilo a ser removido e excluir a linha dele
    for i in range(len(estilos) -1):
        if remov_estilo in estilos[i][0]:
            del(estilos[i])

    # Transforma ele de volta em lista de strings
    for i in range(len(estilos)):
        estilos[i] = ";".join(estilos[i])

    # Abre o arquivo e sobrescreve com as alterações
    arq = open("estilos.txt", "w")
    arq.writelines(estilos)
    arq.close()


    lista_armario2 = []

    # Armazena a lista de peças na variável
    for i in range(len(lista_armario)):
        lista_armario2.append(lista_armario[i].split())

    # For para alterar as peças que tinham o estilo que foi excluido e alterar o estilo para vazio(-)
    for i in range(len(lista_armario2)):

        if str(remov_estilo) in lista_armario2[i][8]:
            
            lista_armario2[i][8] = lista_armario2[i][8].replace(lista_armario2[i][8], "-")

    # For para formatar a lista de peças
    for i in range(len(lista_armario2)):
        if i == len(lista_armario2) - 1:
            lista_armario2[i] = " ".join(lista_armario2[i])
        else:
            lista_armario2[i] = " ".join(lista_armario2[i]) + "\n"

    # Abre o arquivo e sobrescreve com as alterações realizadas
    arq = open("armario.txt", "w")
    arq.writelines(lista_armario2)
    arq.close()

    menu_principal()

#----------------------------------------------------

# Função para alteração de dados
def opcao_5():
    # Mostrar as peças presentes no armário
    lista_armario = imprimir_arq_arm()

    # Abre o arquivo e o armazena em lista_trat para tratamento
    arq = open("armario.txt", "r")
    lista_trat = arq.readlines()
    arq.close()

    # Lista para as categorias
    cat = ["1- Tipo", "2- Tamanho", "3- Padrão",
           "4- Cor", "5- Data", "6- Situação", "7- Preço", "8- Estilos\n"]

    # lista_trat recebe as linhas divididas
    for i in range(len(lista_trat)):
        lista_trat[i] = lista_trat[i].split()

    # salva apenas os IDs de cada roupa
    for i in range(len(lista_trat)):
        lista_trat[i] = lista_trat[i][0]
        lista_trat[i].strip()
    
    # pop na string "ID"
    lista_trat.pop(0)

    # while true verificando a entrada com a lista de IDs existentes
    while True:
        id_alter = int(input("Digite o ID da peça a ser alterada: "))
        if str(id_alter) in lista_trat:
            break
        else:
            print("Entrada inválida. Digite um ID existente.")
            print(*lista_trat)

    # Imprimir a lista de categorias
    for i in range(8):
        print(cat[i])

    while True:
        # Digitar o número da opção a ser alterada
        cat_alter = int(input("Digite o número da opção a ser alterada: \n"))
        if cat_alter >= 1 and cat_alter <= 8:
            break
        else:
            print("Entrada inválida. Escolhe uma das opções.")

    # Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    # Se a alteração é no estilo da peça é realizado um for para pegar a linha
    if cat_alter == 8:

        # lista armario2 vai ser a lista_armario com split em cada linha
        lista_armario2 = []
        for i in range(len(lista_armario)):
            lista_armario2.append(lista_armario[i].split())

        # For para armazenar o estilo da peça desejada
        for i in range(len(lista_armario2)):
            if str(id_alter) in lista_armario2[i][0]:
                estilo_alter = lista_armario2[i][8]
                break
        
        # lê o arquivo estilos
        arq = open("estilos.txt", "r")
        lista_estilos = arq.readlines()
        arq.close()

        # For para transformar o a lista em uma lista de dicionários
        lista_dic = []
        for i in lista_estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)

        # for 
        for i in range (len(lista_dic)):
            # se o estilo escolhido for igual ao valor da chave nome na linha i, então:
            if " " + estilo_alter == lista_dic[i]["NOME "]:
                # dic armazena o dicionario referido
                dic = lista_dic[i]
                # dic_pecas recebe as pecas desse estilo
                dic_pecas = dic[" PECAS "]
                # split na | para separar as pecas, ou seja, cada peça vai ser uma string
                dic_pecas = dic_pecas.split("|")
                for j in range(len(dic_pecas)):
                    # cada peça vai ser dividida em uma lista
                    dic_pecas[j] = dic_pecas[j].split()

        # tira o \n
        dic_pecas.pop(-1)


        # Depois de alterada vai excluir a peça do estilo
        for i in range(len(dic_pecas)):
            if dic_pecas[i][0] == str(id_alter):
                del(dic_pecas[i])
                break

        
        for i in range(len(dic_pecas)):
            # adiciona um "|\n", na ultima peca, se a peça for a ultima
            if i == len(dic_pecas) - 1:
                dic_pecas[i].insert(8, "|\n")
            # adiciona uma "|" se a peça não é a última
            else:
                dic_pecas[i].insert(8, "|")

        # transforma em uma lista com as strings restantes
        for i in range(len(dic_pecas)):
            dic_pecas[i] = " ".join(dic_pecas[i])

        # concatenação das peças em uma variável auxiliar (dic_pecas2)
        dic_pecas2 = ""
        for i in range(len(dic_pecas)):
            dic_pecas2 = dic_pecas2 + " " + dic_pecas[i]

        dic_pecas = dic_pecas2

        # o valor da chave PEÇAS recebe a string atualizada
        dic[" PECAS "] = dic_pecas

        # For para adicionar a peça alterada para o estilo que agora ela faz parte
        for i in range (len(lista_dic)):
            if " " + estilo_alter == lista_dic[i]["NOME "]:
                lista_dic[i] = dic

        # For para converter o dicionario em string
        new_list = []
        for i in range(len(lista_dic)):
            elemento_new_list = "NOME ="
            elemento_new_list = elemento_new_list + lista_dic[i]["NOME "] + ";"
            elemento_new_list = elemento_new_list + " CONTADOR =" + lista_dic[i][" CONTADOR "] + ";"
            elemento_new_list = elemento_new_list + " PECAS =" + lista_dic[i][" PECAS "]
            new_list.append(elemento_new_list)

        # cria uma lista provisória (prov_list) que receberá um split de cada elemento de new_list
        prov_list = []
        for i in range(len(new_list)):
            prov_list.append(new_list[i].split())

        # cria a lista id_trat para tratar a lista provisória, devido a erros na separação
        id_trat = []
        for i in range(len(prov_list)):
            if prov_list[i][7] == "=":
                prov_list[i][-1] = "|\n"
            else:
                # localização onde há erro
                id_trat.append(prov_list[i][7].split("="))
                id_trat = "".join(id_trat[0])
                # retirar a informação errada
                prov_list[i].pop(7)
                # insere a string correta
                prov_list[i].insert(7, str(id_trat))
                # insere o =
                prov_list[i].insert(7, "=")

        # new_list recebe a prov_list, já tratada, em forma de string
        for i in range(len(prov_list)):
            new_list[i] = " ".join(prov_list[i])

        # tratamento para não criar uma linha extra no arquivo
        ult_linha = new_list[-1]
        ult_linha = ult_linha.split(" ")

        # tira a o "|\n"
        ult_linha.pop(-1)
        # adiciona o "|"
        ult_linha.append("|")
        # transforma em string
        ult_linha = " ".join(ult_linha)

        # retira a string errada
        new_list.pop(-1)
        # append da linha correta
        new_list.append(ult_linha)


        # sobrescreve o arquivo com a lista
        arq = open("estilos.txt", "w")
        arq.writelines(new_list)
        arq.close()
        

    # Criação de uma lista para conter todo o armario em uma lista de strings
    lista_armario2 = []

    # Preenchimento da lista
    for i in range(len(lista_armario)):
        lista_armario2.append(lista_armario[i].split())

    # For para percorrer a lista de strings e substituir a informação antiga pela nova
    for i in range(len(lista_armario2)):
        # Se o ID da peça estiver na linha verificada, então
        if str(id_alter) in lista_armario2[i][0]:
            # O elemento da lista na linha i e na coluna cat_alter(característica a ser alterada) irá receber a alteração
            # através do método replace
            lista_armario2[i][cat_alter] = lista_armario2[i][cat_alter].replace(lista_armario2[i][cat_alter], alteracao)

    # Converte de lista de lista para lista de strings
    for i in range(len(lista_armario2)):
        # se é o último elemento, não adiciona o \n
        if i == len(lista_armario2) - 1:
            lista_armario2[i] = " ".join(lista_armario2[i])
        # se não é o último elemento, adiciona o \n
        else:
            lista_armario2[i] = " ".join(lista_armario2[i]) + "\n"

    # Sobrescreve o arquivo com a informação alterada
    arq = open("armario.txt", "w")
    arq.writelines(lista_armario2)
    arq.close()

    # While para tratar as respostas do usuário
    while True:
        alterar_mesma = input("\nVocê gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")

    # Se não, o programa direciona para alteração de outra peça.
    if alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
        # While para tratar as respostas do usuário
        while True:
            alterar_outra = input("Você gostaria de alterar outra peça? ")
            if alterar_outra.lower() == "sim" or alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
                break
            else:
                print("Entrada inválida. Porfavor digitar sim ou não.")
        # Se o usuário digita 'não' ele é direcionado ao menu principal
        if alterar_outra.lower() == "nao" or alterar_outra.lower() == "não":
            menu_principal()
        # Se o usuário digita 'sim' ele retorna a função opção_5()
        else:
            opcao_5()
    # Se sim ele executa a função alteração_arm() passando o id_alter e lista_armario2 como parametros.
    else:
        alteracao_arm(id_alter, lista_armario2)

#----------------------------------------------------

# Função para realizar busca
def opcao_6():

    lista_arm = imprimir_arq_arm()

    # Print das opções de filtragem
    titulos = ["1- Tipo", "2- Tamanho", "3- Padrão", "4- Situação", "5- Listar estilos", "6- Listar peças doadas"]

    for i in range(6):
        print(titulos[i])

    # Validação da entrada do usuário
    while True:
        opcao = int(input("Digite a opção a ser filtrada: "))
        if opcao >= 1 and opcao <= 6:
            break
        else:
            print("Entrada inválida. Digite um número válido.\n")

    # Se opção 1 (TIPO) escolhida
    if opcao == 1:

        # le a primeira linha do arquivo validacao_opt_1.txt 
        arq = open("validacao_opt_1.txt", "r")
        lista_tipos = arq.readlines()[0].split()
        arq.close()

        # Realiza a validação da entrada
        while True:
            tipo = input("Digite o tipo a ser filtrado: ")
            if tipo.lower() in lista_tipos:
                break
            else:
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")

        # Armazena a lista na variável
        lista_armario2 = []
        for i in range(len(lista_arm)):
            lista_armario2.append(lista_arm[i].split())

        # Se o tipo informado conter nas linhas com coluna fixada, irá armazenar a linha toda em uma nova lista
        lista_tipo_filt = []
        for i in range(len(lista_armario2)):
            if tipo in lista_armario2[i][1]:
                lista_tipo_filt.append(lista_armario2[i])

        # Converte a lista de lista para lista de strings
        for i in range(len(lista_tipo_filt)):
            lista_tipo_filt[i] = " ".join(lista_tipo_filt[i])

        print("\n")

        # Print da lista filtrada
        print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
        for i in range(len(lista_tipo_filt)):
            print(lista_tipo_filt[i])

    # Se opção 2 (TAMANHO) escolhida
    elif opcao == 2:

        lista_tamanho = ["p", "m", "g"]

        # Realiza a validação da entrada
        while True:
            tam = input("Digite o tamanho a ser filtrado: ")
            if tam.lower() in lista_tamanho:
                break
            else:
                print("Entrada inválida. Informe se é p, m ou g!")

        # Armazena a lista na variável
        lista_armario2 = []
        for i in range(len(lista_arm)):
            lista_armario2.append(lista_arm[i].split())

        # Se o tamanho informado conter nas linhas com coluna fixada, irá armazenar a linha toda em uma nova lista
        lista_tam_filt = []
        for i in range(len(lista_armario2)):
            if tam in lista_armario2[i][2]:
                lista_tam_filt.append(lista_armario2[i])

        # Converte a lista de lista para lista de strings
        for i in range(len(lista_tam_filt)):
            lista_tam_filt[i] = " ".join(lista_tam_filt[i])

        print("\n")

        # Print da lista filtrada
        print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
        for i in range(len(lista_tam_filt)):
            print(lista_tam_filt[i])

    # Se opção 3 (PADRÃO) escolhida
    elif opcao == 3:

        lista_padrao = ["masculino", "feminino", "unissex"]

        # Validação da entrada do usuário
        while True:
            padrao = input("Digite o padrão a ser filtrado: ")
            if padrao.lower() in lista_padrao:
                break
            else:
                print("Entrada inválida. Informe se é masculino, feminino e unissex!")

        # Armazena a lista numa varíavel
        lista_armario2 = []
        for i in range(len(lista_arm)):
            lista_armario2.append(lista_arm[i].split())

        # Se o padrão informado conter nas linhas com coluna fixada, irá armazenar a linha toda em uma nova lista
        lista_pad_filt = []
        for i in range(len(lista_armario2)):
            if padrao in lista_armario2[i][3]:
                lista_pad_filt.append(lista_armario2[i])

        # Converte a lista de lista para lista de strings
        for i in range(len(lista_pad_filt)):
            lista_pad_filt[i] = " ".join(lista_pad_filt[i])

        print("\n")

        # Print da lista filtrada
        print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
        for i in range(len(lista_pad_filt)):
            print(lista_pad_filt[i])

    # Se opção 4 (SITUAÇÃO) escolhida
    elif opcao == 4:

        # le a terceira linha do arquivo validacao_opt_1.txt 
        arq = open("validacao_opt_1.txt", "r")
        lista_sit = arq.readlines()[2].split()
        arq.close()

        # Validação da entrada
        while True:
            sit = input("Digite a situação a ser filtrado: ")
            if sit.lower() in lista_sit:
                break
            else:
                print("Entrada inválida. Informe se é venda, doação ou ficar!")

        # Se o padrão informado conter nas linhas com coluna fixada, irá armazenar a linha toda em uma nova lista
        if sit.lower() == "ficar":
            sit = sit.lower()
            lista_armario2 = []
            for i in range(len(lista_arm)):
                lista_armario2.append(lista_arm[i].split())

            lista_sit_filt = []
            for i in range(len(lista_armario2)):
                if sit in lista_armario2[i][6]:
                    lista_sit_filt.append(lista_armario2[i])

            # Converte a lista de lista para lista de strings
            for i in range(len(lista_sit_filt)):
                lista_sit_filt[i] = " ".join(lista_sit_filt[i])

            print("\n")

            # Print da lista filtrada
            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_sit_filt)):
                print(lista_sit_filt[i])

        # Se o padrão informado conter nas linhas com coluna fixada, irá armazenar a linha toda em uma nova lista
        elif sit.lower() == "venda":

            # separa a lista_arm e guarda em lista_armario2, transformando em uma lista de listas
            sit = sit.lower()
            lista_armario2 = []
            for i in range(len(lista_arm)):
                lista_armario2.append(lista_arm[i].split())

            # lista_sit_filt recebe a linha que possui venda
            lista_sit_filt = []
            for i in range(len(lista_armario2)):
                if sit in lista_armario2[i][6]:
                    lista_sit_filt.append(lista_armario2[i])

            # lista_precos recebe o valor do preco em float
            lista_precos = []
            for i in range(len(lista_sit_filt)):
                lista_precos.append(float(lista_sit_filt[i][7]))

            # lista_precos é ordenada em forma crescente
            lista_precos.sort()
            lista_precos = sorted(lista_precos)

            # lista_ordem recebe as linhas, do maior valor de preço para o menor, de acordo com a lista_precos
            lista_ordem = []
            for i in range(len(lista_sit_filt)):
                for j in range(len(lista_sit_filt)):
                    if lista_precos[i] == float(lista_sit_filt[j][7]):
                        lista_ordem.append(lista_sit_filt[j])

            # junta os elementos de lista_ordem
            for i in range(len(lista_ordem)):
                lista_ordem[i] = (" ".join(lista_ordem[i]))

            print("\n")
            # print em lista_ordem
            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_ordem)):
                print(lista_ordem[i])

        # ELIF DE DOAÇÃO
        elif sit.lower() == "doacao":


            sit = sit.lower()
            lista_armario2 = []
            for i in range(len(lista_arm)):
                lista_armario2.append(lista_arm[i].split())


            lista_sit_filt = []
            for i in range(len(lista_armario2)):
                if sit in lista_armario2[i][6]:
                    lista_sit_filt.append(lista_armario2[i])


            lista_data = []
            for i in range(len(lista_sit_filt)):
                lista_data.append(lista_sit_filt[i][5])

            # retira as barras, separando o dia, mes e ano
            for i in range(len(lista_data)):
                lista_data[i] = lista_data[i].split('/')


            lista_data_comp = []
            for i in range(len(lista_data)):
                result = int(lista_data[i][0]) + (int(lista_data[i][1]) * 100) + (int(lista_data[i][2]) * 1000)
                lista_data_comp.append(int(result))


            lista_data_comp.sort(reverse = True)


            lista_ordem = []
            for i in range(len(lista_data)):
                for j in range(len(lista_data)):
                    if lista_data_comp[i] == int(lista_data[j][0]) + (int(lista_data[j][1]) * 100) + (int(lista_data[j][2]) * 1000):
                        lista_ordem.append(lista_data[j])


            for i in range(len(lista_ordem)):
                lista_ordem[i] = "/".join(lista_ordem[i])


            lista_data_dec = []
            for i in range(len(lista_sit_filt)):
                for j in range(len(lista_sit_filt)):
                    if lista_ordem[i] == lista_sit_filt[j][5]:
                        lista_data_dec.append(lista_sit_filt[j])
            

            for i in range(len(lista_data_dec)):
                lista_data_dec[i] = " ".join(lista_data_dec[i])


            print("\n")


            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_data_dec)):
                print(lista_data_dec[i])

    # Se opção 5 (ESTILOS) escolhida
    elif opcao == 5:

        # abre o arquivo estilos.txt e guarda cada linha como uma string na lista estilos
        arq = open("estilos.txt", "r")
        estilos = arq.readlines()
        arq.close()

        # lista_dic será uma lista de dicionários dos estilos
        lista_dic = []
        for i in estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)
        
        # lista_cont será uma lista contendo apenas os valores dos contadores dos estilos
        lista_cont = []
        for i in range(len(lista_dic)):
            lista_cont.append(int(lista_dic[i][" CONTADOR "]))
        
        # sorted, reverse = True para ordenar os contadores de maneira decrescente
        lista_cont = sorted(lista_cont, reverse = True)

        # lista_ordem terá os dicionários organizados na forma decrescente de contadores
        lista_ordem = []
        for i in range(len(lista_dic)):
            for j in range(len(lista_dic)):
                # compara os contadores, do maior contador ao o menor contador, de acordo com a lista_cont
                if lista_cont[i] == int(lista_dic[j][" CONTADOR "]):
                    # quando achar o maior, o dicionario correspondente será adcionado à lista_ordem
                    lista_ordem.append(lista_dic[j])

        # \n para organização da saída
        print("\n")

        # "FREQ NOME" indicam a posição da frequência com que o estilo foi selecionado (contador) e o nome do estilo
        print("FREQ NOME")
        for i in range(len(lista_ordem)):
            print(lista_ordem[i][" CONTADOR "], lista_ordem[i]["NOME "])

    # Se opção 6 (LISTAR PEÇAS DOADAS) escolhida
    elif opcao == 6:
        
        # abre o arquivo historico.txt e armazena as cada linha como um elemento da lista historico
        arq = open("historico.txt", "r")
        historico = arq.readlines()
        arq.close()

        # retira os parametros
        historico.pop(0)

        # separa a lista historico em uma matriz de strings
        lista_hist2 = []
        for i in range(len(historico)):
            lista_hist2.append(historico[i].split())

        # busca a palavra "doacao" dentro da lista historico
        lista_hist_filt = []
        for i in range(len(lista_hist2)):
            if "doacao" in lista_hist2[i][6]:
                # quando achada, guarda a linha na lista_hist_filt
                lista_hist_filt.append(lista_hist2[i])

        # junta os elementos com espaços, criando uma lista de strings
        for i in range(len(lista_hist_filt)):
            lista_hist_filt[i] = " ".join(lista_hist_filt[i])

        # \n para melhor organização
        print("\n")

        # print nos parametros e na lista filtrada
        print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos Para")
        for i in range(len(lista_hist_filt)):
            print(lista_hist_filt[i])


    # volta para o menu principal
    menu_principal()

#----------------------------------------------------

# Função para selecionar estilo
def opcao_7():

    # Abre o arquivo e o armazena em estilos
    arq = open("estilos.txt", "r")
    estilos = arq.readlines()
    arq.close()

    # Abre o arquivo e o armazena na variavel nome_estilos para o tratamento
    arq = open("estilos.txt", "r")
    nomes_estilos = arq.readlines()
    arq.close()

    # os elementos de nome_estilos são transformados em dicionários e são armazenados em lista_dic
    lista_dic = []
    for i in nomes_estilos:
        dictionary = dict(subString.split("=") for subString in i.split(";"))
        lista_dic.append(dictionary)

    #lista_comp_nomes recebe apenas os nomes dos estilos
    lista_comp_nomes = []
    for i in range(len(lista_dic)):
        lista_comp_nomes.append(lista_dic[i]["NOME "])

    # split na lista estilos em ";" e guarda em lista_est_nome
    lista_est_nome = []
    for i in range(len(estilos)):
        lista_est_nome.append(estilos[i].split(";"))

    # Print na lista dos nomes dos estilos
    for i in range(len(lista_est_nome)):
        print(lista_est_nome[i][0])

    # while true para verificar a existência do nome dentro de lista_comp_nomes
    while True:
        # Pede a entrada do usuário para saber qual estilo ele quer remover
        nome = input("Digite o nome do estilo a ser selecionado: ")
        if " " + nome.lower() in lista_comp_nomes:
            break
        else:
            print("Digite um nome de estilo válido.")
            print(*lista_comp_nomes)

    # lista_dic recebe dicionarios de estilos como elementos
    lista_dic = []
    for i in estilos:
        dictionary = dict(subString.split("=") for subString in i.split(";"))
        lista_dic.append(dictionary)

    # For para pegar as peças do estilo que sofreram uma alteração e formatá-la de modo que possamos manipular
    for i in range (len(lista_dic)):
        if " " + nome == lista_dic[i]["NOME "]:
            dic = lista_dic[i]
            dic_pecas = dic[" PECAS "]
        
    # print na dic_pecas
    print("ID Tipo Tamanho Padrao Cor Data Situacao Preco")
    dic_pecas = dic_pecas.split("|")
    for i in range(len(dic_pecas)):
        print(dic_pecas[i])

    # lista para verificação de respostas
    val_resp = ["sim", "não", "nao"]

    # enquanto a resposta não estiver em val_resp, pedirá novamente
    while True:
        resposta = input("Você selecionou o estilo correto? ")
        if resposta.lower() not in val_resp:
            print("Entrada inválida. Digite sim ou não.\n")
        else:
            break

    # se a resposta for não
    if resposta in val_resp[1:]:

        # tratamento para resp
        while True:
            resp = input("Você gostaria de selecionar outro estilo? ")
            if resp.lower() not in val_resp:
                print("Entrada inválida. Digite sim ou não.\n")
            else:
                break
        # se a resposta for não, volta para o menu principal
        if resp in val_resp[1:]:
            menu_principal()
        # se a resposta for sim, chama novamente a função
        else:
            opcao_7()

    # se a resposta for sim
    else:

        # recebe o contador do estilo escolhido roda +1 e é guardado novamente na chave " CONTADOR "
        for i in range (len(lista_dic)):
            if " " + nome == lista_dic[i]["NOME "]:
                cont = int(lista_dic[i][" CONTADOR "])
                cont += 1
                lista_dic[i][" CONTADOR "] = " " + str(cont) 

        # transforma a lista de dicionários em lista de strings
        new_list = []
        for i in range(len(lista_dic)):
            elemento_new_list = "NOME ="
            elemento_new_list = elemento_new_list + lista_dic[i]["NOME "] + ";"
            elemento_new_list = elemento_new_list + " CONTADOR =" + lista_dic[i][" CONTADOR "] + ";"
            elemento_new_list = elemento_new_list + " PECAS =" + lista_dic[i][" PECAS "]
            new_list.append(elemento_new_list)

        # sobrescreve no arquivo estilos.txt com o contador atualizado
        arq = open("estilos.txt", "w")
        arq.writelines(new_list)
        arq.close()

        # volta para o menu principal
        menu_principal()


################# ################# #################

################ FUNÇÕES SECUNDÁRIAS ################

# Função para executar alteração da mesma peça
def alteracao_arm(id_alter, lista_armario2):

    # Inicializa lista_armario3 como vazia para ela receber a lista_armario2 após um split que é feito no FOR.
    lista_armario3 = []

    for i in range(len(lista_armario2)):
        lista_armario3.append(lista_armario2[i].split())

    # Lista para as categorias
    cat = ["1- Tipo", "2- Tamanho", "3- Padrao",
           "4- Cor", "5- Data", "6- Situacao", "7- Preco\n"]

    # Printa a lista de categorias
    for i in range(7):
        print(cat[i])

    # Digitar o número da opção a ser alterada
    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    #tratamento de situacao mais preco

    # Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    # For para percorrer a lista de strings e substituir a informação antiga pela nova
    for i in range(len(lista_armario3)):
        # Se o ID da peça estiver na linha verificada, então
        if str(id_alter) in lista_armario3[i][0]:
            # O elemento da lista na linha i e na coluna cat_alter(característica a ser alterada) irá receber a alteração
            # através do método replace
            lista_armario3[i][cat_alter] = lista_armario3[i][cat_alter].replace(lista_armario3[i][cat_alter], alteracao)

    # Converte lista de lista para lista de strings
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

    # While para tratar as respostas do usuário
    while True:
        alterar_mesma = input("Você gostaria de alterar mais alguma coisa na mesma peça: ")
        if alterar_mesma.lower() == "sim" or alterar_mesma.lower() == "nao" or alterar_mesma.lower() == "não":
            break
        else:
            print("Entrada inválida. Porfavor digitar sim ou não.")

    # Se não, o programa direciona para alteração de outra peça.
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
        # Se o usuário digita 'sim' ele retorna a função opção_5()
        else:
            opcao_5()

    # Se sim ele executa a função alteração_arm() passando o id_alter e lista_armario3 como parametros.
    else:
        alteracao_arm(id_alter, lista_armario3)

#----------------------------------------------------

# Função para imprimir o arquivo armario.txt
def imprimir_arq_arm():
    
    # guarda a segunda linha do arquivo armario.txt em lista_armario
    arq = open("armario.txt", "r")

    lista_armario = arq.readlines()
    # print em lista armario com a quebra de linha
    print("".join(lista_armario) + "\n")

    arq.close()

    # retorna lista_armario para ser manipulada
    return lista_armario

#----------------------------------------------------

# Função para o tratamento de data
def tratamento_data():

    # data_atual recebe a data de hoje, de acordo com a biblioteca datetime
    data_atual = date.today()
    # transforma a data em string
    data_atual = str(data_atual)

    # transforma o dia, mês e ano em inteiro para comparar
    ano_atual = int(data_atual[0:4])
    mes_atual = int(data_atual[5:7])
    dia_atual = int(data_atual[8:10])

    # Validação do ano
    while True:
        ano = int(input("Digite o ano de aquisição: "))
        # o ano não pode ser maior que o atual
        if ano <= ano_atual:
            break
        else:
            print("Entrada inválida. Digite um ano menor ou igual ao ano atual.")

    # Validação do mês
    while True:
        mes = int(input("Digite o mês de aquisição: "))
        if ano == ano_atual and mes <= mes_atual:
            if mes >= 1 and mes <= mes_atual:
                break
            else:
                print("Entrada inválida. Digite um mês válido.")
        elif ano < ano_atual:
            if mes >= 1 and mes <= 12:
                break
            else:
                print("Entrada inválida. Digite um mês válido.")
        elif ano == ano_atual and mes > mes_atual:
            print("Entrada inválida. Digite um mês válido.")

    # Validação do dia
    while True:
        dia = int(input("Digite o dia de aquisição: "))
        if mes == mes_atual and dia <= dia_atual and ano == ano_atual:
            if dia >= 1 and dia <= dia_atual:
                break
            else:
                print("Entrada inválida. Digite um dia válido.")
        elif ano == ano_atual and mes < mes_atual:
            #MESES COM 30 DIAS  
            if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia >= 1 and dia <= 30:
                    break
                else:
                    print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
            #MESES COM 31 DIAS
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia >= 1 and dia <= 31:
                    break
                else:
                    print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
            #FEVEREIRO
            else:
                #SE É ANO BISSEXTO
                if ano % 4 == 0:
                    if dia >= 1 and dia <= 29:
                        break
                    else:
                        print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
                #SE NÃO É ANO BISSEXTO
                else:
                    if dia >= 1 and dia <= 28:
                        break
                    else:
                        print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
        elif ano < ano_atual:
            #MESES COM 30 DIAS  
            if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia >= 1 and dia <= 30:
                    break
                else:
                    print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
            #MESES COM 31 DIAS
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia >= 1 and dia <= 31:
                    break
                else:
                    print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
            #FEVEREIRO
            else:
                #SE É ANO BISSEXTO
                if ano % 4 == 0:
                    if dia >= 1 and dia <= 29:
                        break
                    else:
                        print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
                #SE NÃO É ANO BISSEXTO
                else:
                    if dia >= 1 and dia <= 28:
                        break
                    else:
                        print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
        elif ano == ano_atual and mes == mes_atual and dia > dia_atual:
            print("Entrada inválida. Digite um dia menor válido para o mês %i." %mes)
   
   # transforma a data em string
    data_aquisicao = str(dia) +"/"+ str(mes) +"/"+ str(ano)

    # retorna a data
    return data_aquisicao

#----------------------------------------------------

# Função para tratar os dados de entrada
def tratamento_cadastro(j, info):

    # Tratamento do tipo
    if j == 0:

        # guarda a primeira linha do arquivo validacao_opt_1.txt em lista_tipos
        arq = open("validacao_opt_1.txt", "r")
        lista_tipos = arq.readlines()[0].split()
        arq.close()

        # enquanto a informação tratada não estiver na lista, pedirá novamente a informação
        info = info.lower().strip()
        while True:
            if info in lista_tipos:
                return info
            else:
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")
                info = input("Digite o tipo da peça: ")
                info = info.lower().strip()

    # Tratamento do tamanho
    if j == 1:

        # enquanto a informação tratada não for p, m ou g, pedirá novamente a informação
        info = info.lower().strip()
        while True:
            if info == 'p' or info == 'm' or info == 'g':
                return info
            else:
                print("Entrada inválida. Informe se é p, m ou g!")
                info = input("Digite o tamanho da peça: ")
                info = info.lower().strip()

    # Tratamento de padrão
    if j == 2:

        # enquanto a informação tratada não for masculino, feminino ou unissex, pedirá novamente a informação
        info = info.lower().strip()
        while True:
            if info == 'masculino' or info == 'feminino' or info == 'unissex':
                return info
            else:
                print("Entrada inválida. Informe se é masculino, feminino ou unissex!")
                info = input("Digite o padrão da peça: ")
                info = info.lower().strip()

    # Tratamento de cor
    if j == 3:

        # guarda a segunda linha do arquivo validacao_opt_1.txt em lista_tipos
        arq = open("validacao_opt_1.txt", "r")
        lista_cores = arq.readlines()[1].split()
        arq.close()

        # enquanto a informação tratada não for p, m ou g, pedirá novamente a informação
        info = info.lower().strip()
        while True:
            if info in lista_cores:
                return info
            else:
                print("Entrada inválida. Informe uma cor presente na lista!\n")
                # print em lista cores para ver as cores disponíveis
                print(*lista_cores)
                info = input("\nDigite a cor da principal da peça: ")
                info = info.lower().strip()

    # Tratamento de situação
    if j == 5:

        # guarda a terceira linha do arquivo validacao_opt_1.txt em lista_tipos
        arq = open("validacao_opt_1.txt", "r")
        lista_sit = arq.readlines()[2].split()
        arq.close()

        # enquanto a informação tratada não for venda, doacao ou ficar, pedirá novamente a informação
        info = info.lower().strip()
        while True:
            if info in lista_sit:
                return info
            else:
                print("Entrada inválida. Informe se é venda, doação ou ficar!")
                info = input("Digite a situação da peça: ")
                info = info.lower().strip()

################# ################# #################

# Ao inicializar, o programa chama a nossa função principal do programa
menu_principal()
