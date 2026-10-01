from constantes import NOME_ARQUIVO, ENCOD_ARQUIVO
import json

def salvar_visitantes(visitantes):
    with open(NOME_ARQUIVO, "w", encoding=ENCOD_ARQUIVO) as arquivo:
        json.dump(visitantes, arquivo, indent=4)

def carregar_visitantes():
    try:
        with open(NOME_ARQUIVO, "r", encoding=ENCOD_ARQUIVO) as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
