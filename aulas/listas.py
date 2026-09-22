frutas = ["Maçã", "Banana", "Mamão", "Uva"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Lucas", 16, True, "Estudante"]

for dado in dados:
    print(f"dados: {dados}")

alunos = []

alunos.append("Lucas")
alunos.append("Victor")
alunos.append("Pedro")

print(f"Alunos(0): {alunos[0]}")
print(f"Alunos(0): {alunos[1]}")
print(f"Alunos(0): {alunos[2]}")

alunos[1] = "Erik"

print(alunos)

alunos.insert(1, "João")

print(alunos)

alunos.remove("Pedro")

print(alunos)

# alunos.pop(1)

# print(alunos)

tamanho_lista = len(alunos)

print(f"tamanho lista: {tamanho_lista}")
