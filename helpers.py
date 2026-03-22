from validadores import *

# --- Ler Dados --------
def ler_nome(prompt: str) -> str:
    if not isinstance(prompt, str):
        raise TypeError(
            f'O valor a ser informado tem que ser somente strings, informado: {type(prompt).__name__}'
        )
    if not prompt.strip():
        raise ValueError(
            'Nada foi informado, Impossivel prosseguir'
        )
    while True:
        print()
        entrada = input(prompt).strip()

        try:
            nome = validar_nome(entrada)

        except ValueError as error:
            print()
            print(error)
            continue

        return nome


def ler_nota(prompt: str, qtd_nota: int) -> list[float]:
    if not isinstance(prompt, str):
        raise TypeError(
            f'Valor invalido, esperado: "str", informado: "{type(prompt).__name__}".'
        )
    if not prompt.strip():
        raise ValueError(
            f'Nenhum valor foi informado, Impossivel prosseguir.'
        )
    if not isinstance(qtd_nota, int) or isinstance(qtd_nota, bool):
        raise TypeError(
            f'Valor invalido, esperado: "int", informado: "{type(qtd_nota).__name__}".'
        )
    notas = []

    for c in range(qtd_nota):
        while True:
            entrada = input(prompt).strip()

            try:
                nota = validar_nota(entrada)

            except ValueError as error:
                print()
                print(error)
                continue

            notas.append(nota)
            break

    return notas


def ler_quantidade_nota(prompt: str) -> int:
    if not isinstance(prompt, str):
        raise TypeError(
            f'Valor invalido, esperado: "str", informado: "{type(prompt).__name__}".'
        )
    if not prompt.strip():
        raise ValueError(
            f'Nenhum valor foi informado, Impossivel prosseguir.'
        )
    while True:
        try:
            print()
            entrada = int(input(prompt))
            print()
            
        except ValueError:
            print('\nInforme um numero int para prosseguir.')
            continue

        if entrada <= 0:
            print('\nInforme um numero positivo.')
            continue

        return entrada
    