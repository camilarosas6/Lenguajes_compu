"""Tres enfoques para el problema de corte de varilla."""

from functools import lru_cache

_PRECIOS_CLASICOS = (1, 5, 8, 9, 10, 17, 17, 20, 24, 30)
# Para el benchmark extendemos a longitudes 11..20 con precio 2 * longitud.
PRECIOS = _PRECIOS_CLASICOS + tuple(2 * n for n in range(11, 21))


def _validar(precios, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("La longitud n debe ser un entero no negativo.")
    if n > len(precios):
        raise ValueError("Se requiere un precio por cada longitud de pieza hasta n.")


def cut_rod_recursivo(precios, n):
    """Solución recursiva directa; repite subproblemas (tiempo exponencial)."""
    _validar(precios, n)
    if n == 0:
        return 0
    return max(precios[i - 1] + cut_rod_recursivo(precios, n - i) for i in range(1, n + 1))


def cut_rod_memoizado(precios, n):
    """Top-down: guarda el resultado de cada longitud calculada."""
    _validar(precios, n)

    @lru_cache(maxsize=None)
    def resolver(longitud):
        if longitud == 0:
            return 0
        return max(precios[i - 1] + resolver(longitud - i) for i in range(1, longitud + 1))

    return resolver(n)


def cut_rod_tabulario(precios, n):
    """Bottom-up: calcula de 0 a n usando solo resultados ya calculados."""
    _validar(precios, n)
    mejor = [0] * (n + 1)
    for longitud in range(1, n + 1):
        mejor[longitud] = max(
            precios[i - 1] + mejor[longitud - i] for i in range(1, longitud + 1)
        )
    return mejor[n]
