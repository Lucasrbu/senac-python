print("Primeira entrada de dados no python")

nome = input("Qual é o seu nome?")

try:
    idade = int(input("Qual é a sua idade?"))
    print(f"Olá, {nome}. Você tem {idade} anos")

    if idade <= 12:
        print("É criança")
    elif idade <= 18:
        print("É adolescente")
    else:
        print("É adulto")
except Exception:
    print("O valor da idade não é válido")

print(f"tipo do nome {type(nome)}")
print(f"tipo do idade {type(idade)}")

2041775275