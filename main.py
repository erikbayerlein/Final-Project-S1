################# Importações de bibliotecas #################
from datetime import date
################# ########################## #################


################ FUNÇÕES PRINCIPAIS #################

# Função para chamar o menu principal
def menu_principal():

    # Inicializa uma variável que vai mostrar as opções do menu principal
    titulos = ["1- Inserir nova peça", "2- Inserir novo estilo", "3- Remover peça",
               "4- Remover estilo", "5- Alterar peça", "6- Procurar peça", "7- Finalizar programa"]

    print("\n**************** ARMÁRIO VIRTUAL ****************\n")

    for i in range(7):
        print(titulos[i])

    #Aqui sera tratada a entrada do usuário quanto a opção escolhida
    while True:
        opcao_escolhida = int(input("\nDigite um número correspondente a opção do menu: "))
        if opcao_escolhida < 1 or opcao_escolhida > 7:
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

    opcoes = ["1- Criar estilo", "2- Inserir peça a um estilo", "3- Voltar ao menu principal"]

    for i in opcoes:
        print(i)

    while True:
        opcao_escolhida = int(input("\nDigite um número correspondente a opção do menu: \n"))
        if opcao_escolhida < 1 or opcao_escolhida > 3:
            print("Entrada inválida. Digite um número válido.\n")
        else:
            break

    if opcao_escolhida == 1:

        nome = input("Digite o nome do estilo: ")
        new_estilo = f"NOME = {nome}; CONTADOR = 0; PECAS = "

        arq = open("estilos.txt", "a")
        arq.write("\n" + new_estilo)
        arq.close()

        opcao_2()
        
    elif opcao_escolhida == 2:
        
        nome_estilo = input("Em qual estilo você gostaria de adicionar? ")

        lista_arm = imprimir_arq_arm()

        id_peca = input("Digite o ID da peça a ser adicionada: ")

        lista_arm_2 = []
        for i in range(len(lista_arm)):
            lista_arm_2.append(lista_arm[i].split())

        for i in range(len(lista_arm_2)):
            if id_peca in lista_arm_2[i][0]:
                peca = lista_arm[i]

        peca = peca[0:-2]

        arq = open("estilos.txt", "r")
        lista_estilos = arq.readlines()
        arq.close()


        lista_dic = []
        for i in lista_estilos:
            dictionary = dict(subString.split("=") for subString in i.split(";"))
            lista_dic.append(dictionary)
        
        
        for i in range(len(lista_dic)):
            if lista_dic[i]['NOME '] == " " + nome_estilo:
                peca = "|" + peca              
                lista_estilos[i] = lista_estilos[i][:-2] + peca + "\n"


        arq = open("estilos.txt", "w")
        arq.writelines(lista_estilos)
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

    para = input("Digite para quem foi vendida ou doada: ")

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
    print("Esta função não está pronta ainda, você será movido ao menu principal")
    menu_principal()

#----------------------------------------------------

# Função para alteração de dados
def opcao_5():
    # Mostrar as peças presentes no armário
    lista_armario = imprimir_arq_arm()

    # Lista para as categorias
    cat = ["1- Tipo", "2- Tamanho", "3- Padrao",
           "4- Cor", "5- Data", "6- Situacao", "7- Preco\n"]

    # ID para localizar a peça a ser alterada
    id_alter = int(input("Digite o ID da peça a ser alterada: "))

    # Imprimir a lista de categorias
    for i in range(7):
        print(cat[i])

    # Digitar o número da opção a ser alterada
    cat_alter = int(input("Digite o número da opção a ser alterada: \n"))

    #Situção e preco

    # Digitar a nova informação que irá substituir a anterior
    alteracao = input("Digite a nova informação: ")

    # Criação de uma lista para conter todo o armário em forma de lista de strings
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
    print(lista_armario2)
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
    print("Esta função não está pronta ainda, você será movido ao menu principal")
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

    while True:
        ano = int(input("Digite o ano de aquisição: "))
        if ano <= ano_atual:
            break
        else:
            print("Entrada inválida. Digite um ano menor ou igual ao ano atual.")

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
