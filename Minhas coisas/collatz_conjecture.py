try:
    numero = float(input("Digite um número: "))
    quantidade_de_passos = 0

    while numero >= 1:
        if numero == 1:
            print(numero)
            break
        if numero % 2 == 0:
            print(numero)
            numero = numero/2
            if numero == 1:
                print(numero)
                break
        else:
            print(numero)
            numero = numero * 3 + 1
        quantidade_de_passos = quantidade_de_passos + 1
    if numero < 1:
        print("Número inválido(deve ser 1 ou maior)")
    print(f"Quantidade de passos: {quantidade_de_passos}")
except Exception:
    print("Deve ser um número")
