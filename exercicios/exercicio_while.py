contagem = 1
resultado = 0
while contagem <= 5:
    try:
        contagem = contagem + 1
        numero = int(input("Número: "))
        resultado = resultado + numero
    except Exception:
        print("Caractere inválido(deve ser um número int)")
print(resultado) 