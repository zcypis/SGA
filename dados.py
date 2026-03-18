# --- Salvar Dados ------
import json

def salvar_dados(cadastro: dict) -> None:
    with open('dados_alunos.json', 'w') as f:
        json.dump(cadastro, f, indent=4)

def carregar_dados() -> dict:
    try:
        with open('dados_alunos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
