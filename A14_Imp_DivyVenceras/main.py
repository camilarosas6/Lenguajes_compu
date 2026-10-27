# Camila Rodríguez Rosas
# 194100-0
# Lenguajes de Computación
"""Interfaz de consola y mediciones para la actividad A14."""

import argparse
import random
import statistics
import time
import tracemalloc

from karatsuba import karatsuba, multiplicacion_escolar


def numero_aleatorio(digitos: int, rng: random.Random) -> str:
    return str(rng.randrange(1, 10)) + "".join(str(rng.randrange(10)) for _ in range(digitos - 1))


def demostrar(a: str, b: str) -> None:
    k, metricas = karatsuba(a, b)
    escolar, ops_escolar = multiplicacion_escolar(a, b)
    nativo = str(int(a) * int(b))
    print(f"A = {a}\nB = {b}\n")
    print(f"Karatsuba : {k}")
    print(f"Escolar   : {escolar}")
    print(f"Nativo    : {nativo}")
    print(f"Coinciden : {k == escolar == nativo}")
    print(f"Productos de dígitos: Karatsuba={metricas.digit_multiplications}, escolar={ops_escolar}")
    print(f"Llamadas recursivas de Karatsuba: {metricas.recursive_calls}")


def medir(repeticiones: int, semilla: int) -> None:
    rng = random.Random(semilla)
    print("dígitos | variante             | T(N) mediana (ms) | S(N) pico (KB) | productos | llamadas | prof.")
    print("--------|----------------------|------------------|----------------|-----------|----------|------")
    for n in (20, 50, 100):
        a, b = numero_aleatorio(n, rng), numero_aleatorio(n, rng)
        variantes = [
            ("Karatsuba (umbral 1)", lambda: karatsuba(a, b)),
            ("Karatsuba (umbral 2)", lambda: karatsuba(a, b, umbral=2)),
            ("Karatsuba (umbral 4)", lambda: karatsuba(a, b, umbral=4)),
            ("Karatsuba (umbral 16)", lambda: karatsuba(a, b, umbral=16)),
            ("Escolar", lambda: multiplicacion_escolar(a, b)),
            ("Enteros nativos", lambda: (str(int(a) * int(b)), None)),
        ]
        for nombre, funcion in variantes:
            muestras = []
            resultado = None
            for _ in range(repeticiones):
                inicio = time.perf_counter_ns()
                resultado, _ = funcion()
                muestras.append((time.perf_counter_ns() - inicio) / 1_000_000)
                assert resultado == str(int(a) * int(b)), f"Resultado incorrecto: {nombre}, n={n}"
            tracemalloc.start()
            _, _ = funcion()
            _, pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            _, contadores = funcion()
            if contadores is None:
                operaciones, llamadas, profundidad = "interno", "—", "—"
            elif hasattr(contadores, "digit_multiplications"):
                operaciones = contadores.digit_multiplications
                llamadas = contadores.recursive_calls
                profundidad = contadores.max_depth
            else:
                operaciones, llamadas, profundidad = contadores, "—", "—"
            print(
                f"{n:7} | {nombre:20} | {statistics.median(muestras):16.6f} | "
                f"{pico / 1024:14.3f} | {str(operaciones):>9} | {str(llamadas):>8} | {profundidad}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="Multiplicación de enteros gigantes con Karatsuba")
    subparsers = parser.add_subparsers(dest="comando", required=True)
    demo = subparsers.add_parser("multiplicar", help="Multiplica dos enteros y compara tres métodos")
    demo.add_argument("a", help="Primer entero decimal (puede tener signo)")
    demo.add_argument("b", help="Segundo entero decimal (puede tener signo)")
    benchmark = subparsers.add_parser("medir", help="Mide 20, 50 y 100 dígitos")
    benchmark.add_argument("--repeticiones", type=int, default=7)
    benchmark.add_argument("--semilla", type=int, default=14)
    args = parser.parse_args()

    if args.comando == "multiplicar":
        demostrar(args.a, args.b)
    else:
        if args.repeticiones < 1:
            parser.error("--repeticiones debe ser mayor que cero")
        medir(args.repeticiones, args.semilla)


if __name__ == "__main__":
    main()
