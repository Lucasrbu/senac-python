from usuario import Usuario

print("Execução normal do arquivo...")
usuario = Usuario("Lucas", 16)
usuario2 = Usuario("Erick", 16)
print(f"objeto usuário:  {usuario}")
print(f"objeto usuário:  {usuario2}")
print(usuario.nome)
print(usuario.idade)
usuario.idade = 17
print(f"Nova idade: {usuario.idade}")
usuario.apresentar()
usuario2.apresentar()
