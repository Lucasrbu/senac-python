usuario = {
    "nome": "Lucas",
    "email": "Lucas@gmail.com",
    "idade": 16,
    "ativo": True }
print(usuario)
print(f"nome: {usuario["nome"]}")
usuario["idade"] = 17
usuario["cidade"] = "Santa Cruz do Sul"
print(f"nova idade: {usuario["idade"]}")
print(f"Cidade: {usuario["cidade"]}")
del usuario["cidade"]
usuario.pop("idade")
print(usuario)

for chave in usuario.keys():
    print(chave)

for valor in usuario.values():
    print(valor)

for chave, valor in usuario.items():
    print(f"chave: {chave} | valor: {valor}")
    