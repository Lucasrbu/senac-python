nome = input("nome do aluno: ")
try:
    nota1 = float(input("primeira nota do aluno: "))
    nota2 = float(input("segunda nota do aluno: "))
    nota3 = float(input("terceira nota do aluno: "))
    notafinal = (nota1 + nota2 + nota3)/3

    if (nota1 <= 10 and nota1 >= 0) and (nota2 <= 10 and nota2 >= 0) and (nota3 <= 10 and nota3 >= 0):
        notafinal = (nota1 + nota2 + nota3)/3
        print(f"aluno {nome} / nota do primeiro trimestre: {nota1}, nota do segundo trimestre: {nota2} e nota do terceiro trimestre: {nota3}")
        print(f"A nota final é {notafinal:.2f}")
        if notafinal >= 7:
            print("aluno aprovado")
        elif notafinal >= 5 and notafinal <= 6.9:
            print("aluno em recuperação")
        else:
            print("aluno reprovado")
    elif nota1 < 0 or nota2 < 0 or nota3 < 0:
        print("nota abaixo do valor mínimo(0)")
    else:
        print("nota acima do válor máximo(10)")
except Exception:
    print("nota inválida")
