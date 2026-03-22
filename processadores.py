from validadores import *

# --- Processadores de dados ----------
def registrar_aluno(cadastro: dict, aluno: str, notas: list[float]) -> None:
    nome_normalizado = aluno.strip().lower()

    if nome_normalizado in cadastro:
        raise ValueError(
            f'Aluno "{aluno}" ja esta cadastrado.'
        )
    validar_lista_nota(notas)

    cadastro[nome_normalizado] = notas


def calcular_desempenho(notas: list[float]) -> dict:
    validar_lista_nota(notas)

    media = sum(notas) / len(notas)

    if media >= 6:
        situacao = 'aprovado'

    elif media >= 4:
        situacao = 'recuperacao'

    else:
        situacao = 'reprovado'

    return {'media': round(media, 2), 'maior': max(notas), 'menor': min(notas), 'situacao': situacao}


def buscar_aluno(cadastro: dict, aluno_nome: str) -> dict:
    nome_normalizado = aluno_nome.strip().lower()

    if nome_normalizado not in cadastro:
        raise ValueError(
            f'Aluno "{aluno_nome}" nao encontrado.'
        )
    return {'nome': nome_normalizado, 'notas': cadastro[nome_normalizado]}


def listar_alunos(cadastro: dict) -> list[dict]:
    if not cadastro:
        raise ValueError(
            'Nenhum aluno cadastrado.'
        )
    resultado = []

    for nome, notas in cadastro.items():
        desempenho = calcular_desempenho(notas)
        resultado.append({'nome': nome, **desempenho})

    return resultado
