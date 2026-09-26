import uuid
import json
import os
from datetime import datetime

lista_de_visitantes = []
ARQUIVO_DADOS = "dados.json"

visitante = {
    "nome": "nome",
    "data_nascimento": "data_nascimento",
    "cpf": "cpf",
    "tipo_ingresso": "tipo_ingresso",
    "data_visita": "data_visita",
    "numero_ingresso": "numero_ingresso"
}

def salvar_visitantes(lista_de_visitantes):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(lista_de_visitantes, f, indent=4)
    print("\nDados salvos com sucesso")

def carregar_visitantes():
    """"Carrega a lista de visitantes do arquivo JSON"""
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def remover_visitantes_json(lista_de_visitantes):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(lista_de_visitantes, f, indent=4)
    print("\nDados excluídos com sucesso")

def solicitar_texto(mensagem):

    while True:

        valor = input(mensagem).strip()
        if valor != "":
            return valor

        print("Este campo não pode ficar vazio.")

def cpf_cadastrado(lista_de_visitantes, cpf):
    for visitante in lista_de_visitantes:
        if visitante["cpf"] == cpf:
            return True
    return False

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
        nome = solicitar_texto("Nome: ")
        while True:
            data_nascimento = solicitar_texto("Data de nascimento (DD/MM/AAAA): ")
            try:
                datetime.strptime(data_nascimento, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida. " "Use o formato DD/MM/AAAA.")
        while True:
                cpf = solicitar_texto("CPF: ")
                if cpf_cadastrado(lista_de_visitantes, cpf):
                    print("Este CPF já está cadastrado.")
                else:
                    break
        while True:
                tipo_opcao = input("Escolha o tipo de ingresso: ").strip()
                if tipo_opcao == "1":
                    tipo_ingresso = "Normal"
                    break
                elif tipo_opcao == "2":
                    tipo_ingresso = "VIP"
                    break
                elif tipo_opcao == "3":
                    tipo_ingresso = "Premium"
                    break
                else:
                    print("Opcao invalida. Escolha 1, 2 ou 3.")
        print("\nTipos de ingresso:")
        print("1 - Normal")
        print("2 - VIP")
        print("3 - Premium")
        while True:
            data_visita = solicitar_texto("Data da visita (DD/MM/AAAA): ")
            try:
                datetime.strptime(data_visita, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida. " "Use o formato DD/MM/AAAA.")
            numero_ingresso = str(uuid.uuid4())
        lista_de_visitantes.append(visitante)
        print("\nVisitante cadastrado com sucesso!")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Tipo de ingresso: {tipo_ingresso}")
        print(f"Data da visita: {data_visita}")
        print(f"Numero do ingresso: {numero_ingresso}")
        salvar_visitantes(lista_de_visitantes)
    elif acao == "2":
        print()
    elif acao == "0":
        print("Operação encerrada")
        break

    visitante = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "tipo_ingresso": tipo_ingresso,
            "data_visita": data_visita,
            "numero_ingresso": numero_ingresso
        }
