import uuid

lista_de_visitantes = []

visitante = {
    "nome": "nome",
    "data_de_nascimento": "data_de_nascimento",
    "cpf": "cpf",
    "tipo_de_ingresso": "tipo_do_ingresso",
    "data_da_visita": "data_da_visita",
    "numero_de_ingresso": "numero_de_ingresso"
}

while True:
    print("========================================")
    print("              PARQUE AVENTURA")
    print("========================================")

    print("1 - Cadastrar visitante")
    print("2 - Remover visitante")
    print("3 - Listar visitantes")
    print("4 - Ordenar visitantes")
    print("5 - Filtrar visitantes")
    print("6 - Consultar visitante")
    print("0 - Encerrar programa")
    acao = (input("Escolha sua ação: "))
    if acao == "1":
        visitante["nome"] = input("Digite seu nome")
        visitante["data_de_nascimento"] = input("Digite sua data de nascimento")
        visitante["cpf"] = input("Digite seu cpf")

        tipo_do_ingresso = input("Digite o tipo de ingresso, 1 é normal, 2 é VIP e 3 é premium")
        if tipo_do_ingresso == 1:
            visitante["tipo_de_ingresso"] = "Normal"
        elif tipo_do_ingresso == 2:
            visitante["tipo_de_ingresso"] = "VIP"
        elif tipo_do_ingresso == 3:
            lista_de_visitantes = "Premium"
        else:
            print("Tipo de ingresso inválido")
        visitante["data_da_visita"] = input("Digita a data da sua visita")
        visitante["numero_de_ingresso"] = str(uuid.uuid4())
        lista_de_visitantes.append(visitante)
    elif acao == "2":
        tamanho_lista = len(lista_de_visitantes)
        indice = 0 
        while indice < tamanho_lista:
            print(lista_de_visitantes[indice])
            indice = indice + 1
        texto = input("insira o índice do visitante que quer remover")
        lista_de_visitantes.pop(texto)
    elif acao == "3":
        for visita in lista_de_visitantes:
            print(lista_de_visitantes[visita])
    elif acao == "4":
        print()
    elif acao == 0:
        print("Programa encerrando")
        break

