#  contador = 1

# while contador <= 10:
#     if contador == 3:
#         contador += 1
#         continue

#     if contador == 7:
#         break

#     print(f"contador: {contador}")
#     contador += 1

# for numero in range(5):
#     print(f"numweo: {numero}")

# for numero in range(1, 5):
#     print(f"numweo: {numero}")

# for numero in range(1, 5, 2):
#     print(f"numweo: {numero}")

# for numero in range(10, 0, -1):
#     print(f"numweo: {numero}")

# sequencia = range(0, 11, 2)
# for numero in sequencia:
#     print(f"numero: {numero}")

for letra in "Lucas":
    print(f"Letra: {letra}")

frutas = ["Maçã", "Banana", "Mamão"]
for fruta in frutas:
    print(f"fruta: {fruta}")

for indice, fruta in enumerate(frutas):
    print(f"índice: {indice}, fruta: {fruta}")

for indice, fruta in enumerate(frutas, start=1):
    print(f"índice: {indice}, fruta: {fruta}")
