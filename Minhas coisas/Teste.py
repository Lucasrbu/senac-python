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
