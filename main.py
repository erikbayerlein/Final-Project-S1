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
        if opcao_escolhida < 1 or opcao_escolhida > 8:
            print("Entrada inválida. Digite um número válido.\n")
        else:
            break

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
        if opcao_escolhida < 1 or opcao_escolhida > 3:
            print("Entrada inválida. Digite um número válido.\n")
        else:
            break

    # Se opção 1 escolhida, o usuário irá criar um novo nome de estilo
    if opcao_escolhida == 1:

        nome = input("Digite o nome do estilo: ")
        new_estilo = f"NOME = {nome}; CONTADOR = 0; PECAS = "

        # Abre o arquivo e adiciona o novo estilo criado
        arq = open("estilos.txt", "a")
        arq.write("\n" + new_estilo)
        arq.close()

        opcao_2()

    # Se opção 2 escolhida o usuário irá adicionar uma peça em algum dos estilos já criados ou disponíveis
    elif opcao_escolhida == 2:

        # O usuário informa em qual estilo ele quer adicionar a peça
        nome_estilo = input("Em qual estilo você gostaria de adicionar? ")

        lista_arm = imprimir_arq_arm()

        print(lista_arm)

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
        
        # For para adicionar a peça ao estilo informado
        for i in range(len(lista_dic)):
            if lista_dic[i]['NOME '] == " " + nome_estilo:
                peca = " " + peca + "|"       
                lista_estilos[i] = lista_estilos[i][:-1] + peca + "\n"

        # Sobrescreve o arquivo com a peça já adicionada
        arq = open("estilos.txt", "w")
        arq.writelines(lista_estilos)
        arq.close()


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
        print(lista_armario2)
        arq = open("armario.txt", "w")
        arq.writelines(lista_armario2)
        arq.close()


        opcao_2()

    elif opcao_escolhida == 3:
        menu_principal()

#----------------------------------------------------

# Função para Remoção de dados
def opcao_3():
    # Chama a função para imprimir o arquivo
    lista_armario = imprimir_arq_arm()

    # Pede o ID da peça a ser removida
    remov_id = int(input("Digite o ID da peça a ser removida: "))


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

    #Adiciona a informação a linha da peça
    historico = "\n" + historico[:-1] + " " + para

    print(historico)
    
    # Sobrescreve o arquivo com as alterações realizadas e volta ao menu principal
    arq = open("armario.txt", "w")
    arq.writelines(lista_armario)
    arq.close()

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

    # Split na lista de estilos
    for i in range(len(estilos)):
        estilos[i] = estilos[i].split(";")

    # Print na lista dos estilos
    for i in range(len(estilos)):
        print(estilos[i][0])

    # Pede a entrada do usuário para saber qual estilo ele quer remover
    remov_estilo = input("\nDigite o nome do estilo a ser removido: ")

    ######### NECESSÁRIO TRATAMENTO DE DADOS #########
    # For para procurar o estilo a ser removido e excluir a linha dele
    for i in range(len(estilos) -1):
        if remov_estilo in estilos[i][0]:
            del(estilos[i])

    # Transforma ele de volta em lista de strings
    for i in range(len(estilos)):
        estilos = ";".join(estilos[i])
    
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

    # Lista para as categorias
    cat = ["1- Tipo", "2- Tamanho", "3- Padrao",
           "4- Cor", "5- Data", "6- Situacao", "7- Preco", "8- Estilos\n"]

    # ID para localizar a peça a ser alterada
    id_alter = int(input("Digite o ID da peça a ser alterada: "))

    # Imprimir a lista de categorias
    for i in range(8):
        print(cat[i])

    # Digitar o número da opção a ser alterada
    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    #Situção e preco

    # Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    # Se a alteração é no estilo da peça é realizado um for para pegar a linha
    if cat_alter == 8:

        lista_armario2 = []
        for i in range(len(lista_armario)):
            lista_armario2.append(lista_armario[i].split())

        # For para armazenar o estilo da peça desejada
        for i in range(len(lista_armario2)):
            if str(id_alter) in lista_armario2[i][0]:
                estilo_alter = lista_armario2[i][8]
            

        arq = open("estilos.txt", "r")
        lista_estilos = arq.readlines()
        arq.close()

        # For para transformar o dicionário em lista
        lista_dic = []
        for i in lista_estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)

        # For para pegar as peças do estilo que sofrerá uma alteração e formatá-la de modo que possamos manipular
        for i in range (len(lista_dic)):
            if " " + estilo_alter == lista_dic[i]["NOME "]:
                dic = lista_dic[i]
                dic_pecas = dic[" PECAS "]
                dic_pecas = dic_pecas.split("|")
                for j in range(len(dic_pecas)):
                    dic_pecas[j] = dic_pecas[j].split()

        dic_pecas.pop(-1)

        # Depois de alterada vai excluir a peça do estilo anterior
        for i in range(len(dic_pecas)):
            if dic_pecas[i][0] == str(id_alter):
                del(dic_pecas[i])
                break
        # Adiciona a peça ao novo estilo informado
        dic_pecas2 = ""
        for i in range(len(dic_pecas)):
            dic_pecas = " ".join(dic_pecas[i])
            dic_pecas = dic_pecas + "|"
            dic_pecas2 = dic_pecas2 + dic_pecas
        dic_pecas = dic_pecas2

        dic[" PECAS "] = dic_pecas

        # For para adicionar a peça alterada para o estilo que agora ela faz parte
        for i in range (len(lista_dic)):
            if " " + estilo_alter == lista_dic[i]["NOME "]:
                lista_dic[i] = dic

        # For para converter a lista em dicionarios após as alterações
        new_list = []
        for i in range(len(lista_dic)):
            elemento_new_list = "NOME = "
            elemento_new_list = elemento_new_list + lista_dic[i]["NOME "] + ";"
            elemento_new_list = elemento_new_list + " CONTADOR = " + lista_dic[i][" CONTADOR "] + ";"
            elemento_new_list = elemento_new_list + " " + lista_dic[i][" PECAS "]
            new_list.append(elemento_new_list)

        
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
        if i == len(lista_armario2) - 1:
            lista_armario2[i] = " ".join(lista_armario2[i])
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
    titulos = ["1- Tipo", "2- Tamanho", "3- Padrão", "4- Situação"]

    for i in range(4):
        print(titulos[i])

    # Validação da entrada do usuário
    while True:
        opcao = int(input("Digite a opção a ser filtrada: "))
        if opcao < 1 or opcao > 4:
            print("Entrada inválida. Digite um número válido.\n")
        else:
            break

    # Se opção 1(TIPO) escolhida
    if opcao == 1:

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

    # Se opção 2(TAMANHO) escolhida
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

    # Se opção 3(PADRÃO) escolhida
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

    # Se opção 3(SITUAÇÃO) escolhida
    elif opcao == 4:

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
            lista_armario2 = []
            for i in range(len(lista_arm)):
                lista_armario2.append(lista_arm[i].split())


            lista_sit_filt = []
            for i in range(len(lista_armario2)):
                if sit in lista_armario2[i][6]:
                    lista_sit_filt.append(lista_armario2[i])

            print(lista_sit_filt)


            lista_precos = []
            for i in range(len(lista_sit_filt)):
                lista_precos.append(float(lista_sit_filt[i][7]))

            #PARAMOS AQUI E PRECISAMOS CONSERTAR ORDEM DE VENDA E DATA
            lista_precos = sorted(lista_precos)
            l = []
            '''for i in range(len(lista_precos)):
                menor_preco = lista_precos[i]
                for j in range(len(lista_precos)):
                    if lista_precos[j] <= menor_preco:
                        menor_preco = lista_precos[j]
                        l.append(menor_preco)'''

            lista_ordem = []
            for i in range(len(lista_sit_filt)):
                if lista_precos[i] == float(lista_sit_filt[i][7]):
                    print(lista_sit_filt[i][7])
                    lista_ordem.append(lista_sit_filt[i])
                

            print(lista_ordem)
            print(lista_ordem)

            for i in range(len(lista_sit_filt)):
                lista_ordem[i] = " ".join(lista_ordem[i])

            print("\n")

            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_ordem)):
                print(lista_ordem[i])


            '''for i in range(len(lista_sit_filt)):
                for j in range(1, len(lista_sit_filt)):
                    if i == len(lista_sit_filt):
                        break
                    elif float(lista_sit_filt[i][7]) >= float(lista_sit_filt[j][7]):
                        comp_indice = '''


            #APAGAR
            '''i = 0
            while True:
                for j in range(len(1, lista_sit_filt)):
                    if j == len(lista_sit_filt):
                        break
                    elif float(lista_sit_filt[0][7]) >= float(lista_sit_filt[j][7]):
                        lista_sit_filt.insert(j, lista_sit_filt[0])
                        lista_sit_filt.pop(0)
                        j += 1
                    else:
                        break'''



            '''for i in range(len(lista_sit_filt)):
                lista_sit_filt[i] = " ".join(lista_sit_filt[i])

            print("\n")

            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_sit_filt)):
                print(lista_sit_filt[i])'''



        elif sit.lower() == "doacao":
            lista_armario2 = []
            for i in range(len(lista_arm)):
                lista_armario2.append(lista_arm[i].split())

            lista_sit_filt = []
            for i in range(len(lista_armario2)):
                if sit in lista_armario2[i][6]:
                    lista_sit_filt.append(lista_armario2[i])


            for i in range(len(lista_sit_filt)):
                lista_sit_filt[i] = " ".join(lista_sit_filt[i])

            print("\n")

            print("ID Tipo Tamanho Padrao Cor Data Situacao Preco Estilos")
            for i in range(len(lista_sit_filt)):
                print(lista_sit_filt[i])

    


    menu_principal()

#----------------------------------------------------

# Função para selecionar estilo
def opcao_7():
    print ("Função ainda não disponível")


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
    arq = open("armario.txt", "r")

    lista_armario = arq.readlines()
    print("".join(lista_armario) + "\n")

    arq.close()

    return lista_armario

#----------------------------------------------------

# Função para o tratamento de data
def tratamento_data():

    data_atual = date.today()
    data_atual = str(data_atual)

    ano_atual = int(data_atual[0:4])
    mes_atual = int(data_atual[5:7])
    dia_atual = int(data_atual[8:10])

    # Validação do ano
    while True:
        ano = int(input("Digite o ano de aquisição: "))
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
   
    data_aquisicao = str(dia) +"/"+ str(mes) +"/"+ str(ano)

    return data_aquisicao

#----------------------------------------------------

# Função para tratar os dados de entrada
def tratamento_cadastro(j, info):
    # Tipo
    # OK
    if j == 0:

        arq = open("validacao_opt_1.txt", "r")
        lista_tipos = arq.readlines()[0].split()
        arq.close()

        info = info.lower().strip()
        while True:
            if info in lista_tipos:
                return info
            else:
                print("Entrada inválida. Informe se é superior, inferior ou calçado!")
                info = input("Digite o tipo da peça: ")
                info = info.lower().strip()

    # Tamanho
    # OK
    if j == 1:
        info = info.lower().strip()
        while True:
            if info == 'p' or info == 'm' or info == 'g':
                return info
            else:
                print("Entrada inválida. Informe se é p, m ou g!")
                info = input("Digite o tamanho da peça: ")
                info = info.lower().strip()

    # Padrão
    # OK
    if j == 2:
        info = info.lower().strip()
        while True:
            if info == 'masculino' or info == 'feminino' or info == 'unissex':
                return info
            else:
                print("Entrada inválida. Informe se é masculino, feminino ou unissex!")
                info = input("Digite o padrão da peça: ")
                info = info.lower().strip()

    # Cor
    # OK
    if j == 3:

        arq = open("validacao_opt_1.txt", "r")
        lista_cores = arq.readlines()[1].split()
        arq.close()

        info = info.lower().strip()
        while True:
            if info in lista_cores:
                return info
            else:
                print("Entrada inválida. Informe uma cor presente na lista!\n")
                print(*lista_cores)
                info = input("\nDigite a cor da principal da peça: ")
                info = info.lower().strip()

    # Situação
    # OK
    if j == 5:

        arq = open("validacao_opt_1.txt", "r")
        lista_sit = arq.readlines()[2].split()
        arq.close()

        print(lista_sit)

        info = info.lower().strip()
        while True:
            if info in lista_sit:
                return info
            else:
                print("Entrada inválida. Informe se é venda, doação ou ficar!")
                info = input("Digite a situação da peça: ")
                info = info.lower().strip()

################# ################# #################

# Ao inicializar o programa chama a nossa função principal do programa
menu_principal()
