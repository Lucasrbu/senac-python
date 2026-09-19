from dataclasses import dataclass

@dataclass
class Usuario:
    email: str
    senha: str

admin = Usuario(email= "admin@gmail.com", senha= "1234")

while True:
    email = input("Email: ")
    senha = input("Senha: ")
    if email == admin.email and senha == admin.senha:
        print(f"Email: {admin.email}, Senha: {admin.senha}")
        print("Login realizado com sucesso")
    else:
        print("Dados incorretos")