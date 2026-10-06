"""
Actividad 10: Problemas decidibles, semidecidibles y no decidibles
Nombre: Camila Rodríguez Rosas - 194100
Nombre: Jonathan Hernández Lazcano - 200417
Materia: Lenguajes de Computación
Fecha: 1 de octubre de 2026

---------------------------------------------------------------------
Evalúa x^n + y^n = z^n para todas las combinaciones x, y, z ∈ {0, 1, ..., 100} y
n ∈ {1, 2, 3}, y vacía cada combinación evaluada en un archivo de texto con la 
etiqueta CUMPLE o NO CUMPLE según corresponda
"""
from itertools import product
from pathlib import Path

# --- Parámetros del problema --------------------------------------------------
NO_CUENTA = "200417, 194100"
NOMBRE = "Jonathan Hernández Lazcano, Camila Rodríguez Rosas"
RANGO_VARIABLES = range(0, 101)     # x, y, z ∈ {0, 1, ..., 100}
EXPONENTES = (1, 2, 3)              # n ∈ {1, 2, 3}
ARCHIVO_SALIDA = Path(__file__).with_name(f"A10_resultados_{NO_CUENTA}.txt")

BLOQUE_IDENTIFICACION = f"""\
==============================================================================
 BLOQUE DE IDENTIFICACIÓN
------------------------------------------------------------------------------
 Actividad      : A10. Problemas decidibles, semidecidibles y no decidibles
 Materia        : Lenguajes y Computación — 5.º semestre
 Alumno         : {NOMBRE}
 No. de cuenta  : {NO_CUENTA}
 Ecuación       : x^n + y^n = z^n
 Dominio        : x, y, z ∈ {{0, 1, ..., 100}},  n ∈ {{1, 2, 3}}
 Formato        : (x, y, z), n -> CUMPLE/NO CUMPLE
==============================================================================
"""


def cumple_ecuacion(x, y, z, n):
    """Devuelve True si x^n + y^n = z^n (aritmética entera exacta)."""
    return x ** n + y ** n == z ** n


def evaluar_combinaciones(ruta_salida=ARCHIVO_SALIDA):
    """
    Evalúa todas las combinaciones (x, y, z), n y escribe en `ruta_salida`
    una línea por combinación con la etiqueta CUMPLE o NO CUMPLE.

    Devuelve un diccionario {n: cantidad de combinaciones que cumplen}.
    """
    cumplen_por_n = {n: 0 for n in EXPONENTES}
    total = 0

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(BLOQUE_IDENTIFICACION + "\n")

        for n in EXPONENTES:
            # Se acumulan las líneas de cada exponente y se escriben de una
            # sola vez: son 101^3 = 1,030,301 combinaciones por cada n.
            lineas = []
            for x, y, z in product(RANGO_VARIABLES, repeat=3):
                if cumple_ecuacion(x, y, z, n):
                    etiqueta = "CUMPLE"
                    cumplen_por_n[n] += 1
                else:
                    etiqueta = "NO CUMPLE"
                lineas.append(f"({x}, {y}, {z}), {n} -> {etiqueta}\n")
            archivo.writelines(lineas)
            total += len(lineas)

        # Resumen al final de la lista
        archivo.write("\n" + "=" * 78 + "\n RESUMEN\n" + "-" * 78 + "\n")
        archivo.write(f" Combinaciones evaluadas : {total:,}\n")
        for n, cantidad in cumplen_por_n.items():
            archivo.write(f" n = {n} -> CUMPLE: {cantidad:,}  |  "
                          f"NO CUMPLE: {total // len(EXPONENTES) - cantidad:,}\n")
        archivo.write("=" * 78 + "\n")

    return cumplen_por_n


def main():
    cumplen_por_n = evaluar_combinaciones()
    total = len(RANGO_VARIABLES) ** 3 * len(EXPONENTES)
    print(f"Combinaciones evaluadas: {total:,}")
    for n, cantidad in cumplen_por_n.items():
        print(f"  n = {n}: {cantidad:,} combinaciones CUMPLEN")
    print(f"Resultados guardados en: {ARCHIVO_SALIDA.name}")


if __name__ == "__main__":
    main()
