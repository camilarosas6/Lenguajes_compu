from itertools import product


def union(lenguaje1: set[str], lenguaje2: set[str]) -> set[str]:
    """
    Union de dos lenguajes.
    """
    return lenguaje1 | lenguaje2


def interseccion(lenguaje1: set[str], lenguaje2: set[str]) -> set[str]:
    """
    Interseccion de dos lenguajes.
    """
    return lenguaje1 & lenguaje2


def diferencia(lenguaje1: set[str], lenguaje2: set[str]) -> set[str]:
    """
    Diferencia entre dos lenguajes.
    """
    return lenguaje1 - lenguaje2


def concatenar(lenguaje1: set[str], lenguaje2: set[str]) -> set[str]:
    """
    Concatenacion de dos lenguajes.
    """
    resultado = set()

    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            resultado.add(palabra1 + palabra2)

    return resultado


def potencia(lenguaje: set[str], exponente: int) -> set[str]:
    """
    Calcula potencia de un lenguaje.
    """
    if exponente < 0:
        raise ValueError("El exponente debe ser mayor o igual a 0")

    if exponente == 0:
        return {""}

    resultado = {""}

    for _ in range(exponente):
        resultado = concatenar(resultado, lenguaje)

    return resultado


def complemento(
    lenguaje: set[str],
    alfabeto: set[str],
    longitud_maxima: int
) -> set[str]:
    """
    Calcula el complemento del lenguaje dentro de Sigma*
    hasta longitud maxima.
    """

    universo = {""}

    for longitud in range(1, longitud_maxima + 1):
        for combinacion in product(alfabeto, repeat=longitud):
            universo.add("".join(combinacion))

    return universo - lenguaje


def clausura_kleene(
    lenguaje: set[str],
    max_elementos: int
) -> set[str]:
    """
    Genera primeros elementos de la clausura de Kleene.

    Se ordenan primero por longitud y despues
    lexicograficamente.
    """

    # Quitar lambda para evitar ciclos infinitos
    palabras = {palabra for palabra in lenguaje if palabra != ""}

    resultado = {""}

    # Genera suficientes combinaciones
    actual = {""}

    for _ in range(max_elementos):
        siguiente = set()

        for palabra1 in actual:
            for palabra2 in palabras:
                siguiente.add(palabra1 + palabra2)

        resultado.update(siguiente)
        actual = siguiente

    # Ordena por longitud y despues alfabeticamente
    ordenado = sorted(
        resultado,
        key=lambda palabra: (len(palabra), palabra)
    )

    return set(ordenado[:max_elementos])


def primeros_elementos_kleene(
    lenguaje: set[str],
    max_elementos: int
) -> list[str]:
    """
    Devuelve una lista
    ordenada para mostrar los elementos de forma consistente.
    """

    palabras = {palabra for palabra in lenguaje if palabra != ""}

    resultado = {""}
    actual = {""}

    for _ in range(max_elementos):
        siguiente = set()

        for palabra1 in actual:
            for palabra2 in palabras:
                siguiente.add(palabra1 + palabra2)

        resultado.update(siguiente)
        actual = siguiente

    ordenado = sorted(
        resultado,
        key=lambda palabra: (len(palabra), palabra)
    )

    return ordenado[:max_elementos]