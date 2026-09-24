import uuid
visitantes = []
def solicitar_texto(mensagem):

    while True:

        valor = input(mensagem).strip()

        # Verifica se o usuario digitou alguma coisa.
        if valor != "":
            return valor

        print("Este campo nao pode ficar vazio.")

def calcular_idade(data_nascimento):
    dia, mes, ano = data_nascimento.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    idade = 2022 - ano
    if mes > 10:
        idade -= 1
    return idade

def cpf_cadastrado(visitantes, cpf):
    for visitante in visitantes:
        if visitante["cpf"] == cpf:
            return True
    return False


def cadastrar_visitante(visitantes):

    print("\n" + "=" * 50)
    print("CADASTRO DE VISITANTE")
    print("=" * 50)

    nome = solicitar_texto("Nome: ")

    data_nascimento = solicitar_texto(
        "Data de nascimento (DD/MM/AAAA): "
    )

    cpf = solicitar_texto("CPF: ")

    print("\nTipos de ingresso:")
    print("1 - Normal")
    print("2 - VIP")
    print("3 - Premium")

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

    data_visita = solicitar_texto(
        "Data da visita (DD/MM/AAAA): "
    )

    numero_ingresso = str(uuid.uuid4())

    visitante = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "tipo_ingresso": tipo_ingresso,
        "data_visita": data_visita,
        "numero_ingresso": numero_ingresso
    }

    visitantes.append(visitante)

    print("\nVisitante cadastrado com sucesso!")

    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Tipo de ingresso: {tipo_ingresso}")
    print(f"Data da visita: {data_visita}")
    print(f"Numero do ingresso: {numero_ingresso}")

def listar_visitantes(visitantes):
    print("\n" + "=" * 50)
    print("CADASTRO DE VISITANTE")
    print("=" * 50)

    if not visitantes:
        print("Nenhum visitante cadastrado")
        return

    for visitante in visitantes:
        print(f"Nome: {visitante["nome"]}")
        print(f"Cpf: {visitante["cpf"]}")
        print(f"Tipo de ingresso: {visitante["tipo_ingresso"]}")
        print(f"Data da visita: {visitante["data_visita"]}")
        print(f"Número do ingresso: {visitante["numero_ingresso"]}")
        print("-" * 50)

def consultar_visitante(visitantes):
    print("\n" + "=" * 50)
    print("CENTRAL DE VISITANTES DO PARQUE")
    print("=" * 50)

    if not visitantes:
        print("Nenhum visitante cadastrado")
        return

    cpf = solicitar_texto("Digite o CPF do visitante: ")
    for visitante in visitantes:
        if visitante["cpf"] == cpf:
            print(f"Nome: {visitante["nome"]}")
            print(f"Cpf: {visitante["cpf"]}")
            print(f"Tipo de ingresso: {visitante["tipo_ingresso"]}")
            print(f"Data da visita: {visitante["data_visita"]}")
            print(f"Número do ingresso: {visitante["numero_ingresso"]}")
            print("-" * 50)
    print("Visitante não encontrado")

def remover_visitante(visitantes):
    print("\n" + "=" * 50)
    print("CENTRAL DE VISITANTES DO PARQUE")
    print("=" * 50)

    if not visitantes:
        print("Nenhum visitante cadastrado")
        return

    cpf = solicitar_texto("Digite o CPF do visitante: ")
    for visitante in visitantes:
        if visitante["cpf"] == cpf:
            confirmar = solicitar_texto("Tem certeza que deseja remover este visitante? (s/n): ")
            if confirmar == "s":
                visitantes.remove(visitante)
                print("Visitante removido com sucesso")
                return
            elif confirmar != "s" or confirmar != "n":
                print("Operação inválida. Tente novamente.")
                return
            elif confirmar == "n" or confirmar == "N":
                print("Operação cancelada")
                return
    print("Visitante não encontrado")

def main():

    while True:

        print("\n" + "=" * 50)
        print("CENTRAL DE VISITANTES DO PARQUE")
        print("=" * 50)

        print("0 - Encerrar programa")
        print("1 - Cadastrar visitante")
        print("2 - remover visitante")
        print("3 - listar visitantes")
        print("4 - ordenar visitantes")
        print("5 - filtrar visitantes")
        print("6 - consultar visitante")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":

            cadastrar_visitante(visitantes)

        elif opcao == "2":
            remover_visitante(visitantes)

        elif opcao == "3":
            listar_visitantes(visitantes)

        elif opcao == "6":
            consultar_visitante(visitantes)

        elif opcao == "0":

            print("\nPrograma encerrado.")
            break


        else:

            print("\nOpcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()