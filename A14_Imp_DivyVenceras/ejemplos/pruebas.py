"""Comprobaciones de funcionamiento sin dependencias externas.

Ejecutar desde A14: python3 ejemplos/pruebas.py
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from karatsuba import karatsuba, multiplicacion_escolar  # noqa: E402


def comprobar(a: str, b: str) -> None:
    referencia = str(int(a) * int(b))
    escolar, _ = multiplicacion_escolar(a, b)
    assert escolar == referencia, ("escolar", a, b, escolar, referencia)
    for umbral in (1, 2, 4, 16):
        resultado, _ = karatsuba(a, b, umbral=umbral)
        assert resultado == referencia, ("Karatsuba", umbral, a, b, resultado, referencia)


def main() -> None:
    # Tamaños requeridos y casos con signo, ceros, acarreo y longitudes distintas.
    for n in (20, 50, 100):
        comprobar("9" * n, "8" * n)
    bordes = [
        ("0", "0"), ("0", "98765432109876543210"), ("7", "8"),
        ("1234", "5678"), ("9" * 100, "9" * 100),
        ("1" + "0" * 99, "1" + "0" * 49),
        ("-" + "3" * 50, "4" * 20), ("-123456789", "-987654321"),
        ("000000123", "0045"), ("9" * 100, "1"),
    ]
    for a, b in bordes:
        comprobar(a, b)

    rng = random.Random(14)
    for _ in range(300):
        digitos_a, digitos_b = rng.randint(1, 150), rng.randint(1, 150)
        a = str(rng.randrange(10 ** (digitos_a - 1), 10**digitos_a))
        b = str(rng.randrange(10 ** (digitos_b - 1), 10**digitos_b))
        if rng.random() < 0.3:
            a = "-" + a
        if rng.random() < 0.3:
            b = "-" + b
        comprobar(a, b)

    for a, b in (("", "3"), ("12a", "3"), ("1.5", "2")):
        for funcion in (karatsuba, multiplicacion_escolar):
            try:
                funcion(a, b)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Se esperaba ValueError para {a!r} × {b!r}")
    try:
        karatsuba("12", "3", umbral=0)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError para umbral=0")

    print("Correcto: tamaños 20/50/100, 10 casos borde, 300 pares aleatorios y entradas inválidas.")


if __name__ == "__main__":
    main()
