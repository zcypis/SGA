# --- Validadores de dados --------
def validar_nome(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError(
            f'({nome}) Valor informado inaceitavel pela função, informe: str.'
        )
    if not nome.strip():
        raise ValueError(
            'Nada foi informado, Impossivel prosseguir.'
        )
    if len(nome) < 2:
        raise ValueError(
            'Informe no minimo 2 letras.'
        )
    if len(nome.split()) > 2:
        raise ValueError(
            'Informe no maximo 2 nomes, ex: "Nome Sobrenome".'
        )
    if not all(parte.isalpha() for parte in nome.split()):
        raise ValueError(
            'O nome nao pode conter numeros ou simbolos.'
        )
    return nome


def validar_nota(nota: str) -> float:
    if not isinstance(nota, str):
        raise TypeError(
            f'({nota}) Valor informado inaceitavel pela função, informe: str.'
        )
    try:
        nota_convertida = float(nota)
    except ValueError:
        raise ValueError(
            'O valor digitado nao e um numero real valido'
        )
    if '.' in nota and len(nota.split('.')[1]) > 1:
        raise ValueError(
            f'O valor a digita pode conter somente 1 casa decimal, ex: "{round(float(nota), 1)}".'
        )
    if not 0.0 <= nota_convertida <= 10.0:
        raise ValueError(
            'O valor tem que ser no maximo: "10.0", e no minimo: "0.0".'
        )
    return nota_convertida


def validar_lista_nota(lista: list[float]) -> None:
    if not isinstance(lista, list):
        raise TypeError(
            f'Valor invalido, esperado: "list", informado: "{type(lista).__name__}".'
        )
    if not lista:
        raise ValueError(
            'Nenhum valor informado, Impossivel prosseguir'
        )
    for nota in lista:
        if not isinstance(nota, float):
            raise TypeError(
                f'Valor "{nota}" da lista é invalido, esperado: "float", informado: "{type(nota).__name__}".'
            )

