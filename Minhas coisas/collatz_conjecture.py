numero = int(input("Digite um número: "))
quantidade_de_passos = 0

while numero >= 2:
    if numero % 2 == 0:
        print(numero)
        numero = numero/2
    else:
        print(numero)
        numero = numero * 3 + 1
    quantidade_de_passos = quantidade_de_passos + 1
print(f"Quantidade de passos: {quantidade_de_passos}")