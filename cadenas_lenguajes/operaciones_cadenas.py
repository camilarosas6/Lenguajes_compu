def concatenar(cadena1: str, cadena2: str) -> str:
    """
    Concatena dos cadenas.
    """
    return cadena1 + cadena2


def unir(cadenas: list[str]) -> str:
    """
    Une una lista de cadenas en una sola cadena.
    """
    return "".join(cadenas)


def potencia(cadena: str, exponente: int) -> str:
    """
    Calcula la potencia de una cadena.
    """
    if exponente < 0:
        raise ValueError("El exponente debe ser mayor o igual a 0")

    return cadena * exponente
