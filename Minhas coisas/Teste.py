import uuid

opcao = 10
if opcao == "1":
    ingresso = "Normal"
elif opcao == "2":
    ingresso = "VIP"
elif opcao == "3":
    ingresso = "Premium"
else:
    ingresso = "Inválido"


lista_visitantes = []
visitante = {
    "nome": "nome",
    "cpf": "cpf",
    "ingresso": "ingresso"
}

lista_visitantes.append(visitante)

for visitantes in lista_visitantes:
    print(visitante)

def cadastrar_visitantes(visitantes):
    numero_ingresso = str(uuid.uuid4())

def cadastrar_visitante(visitantes):

    print("\n" + "=" * 50)

while True:
    cpf = solicitar_texto("CPF: ")

    if len(cpf) != 11:
        print("CPF inválido: Digite 11 números")
    elif cpf_cadastrado(visitantes, cpf):
        print("CPF já cadastrado")
    else:
        break

def validar_date
while True:
    data_visita = solicitar_texto(
        "Data da visita (DD/MM/AAAA): "
    )
    try:
        dia, mes, ano = data_visita.split("/")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if dia < 1 or dia > 31:
            print("Data inválida")
        elif mes < 1 or mes > 12:
            print("Mês inválido")
        elif ano < 1500 or ano > 2026:
            print("Ano inválido: ")
        else:
            break
    except ValueError:

