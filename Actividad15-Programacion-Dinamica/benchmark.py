"""Benchmark de las tres técnicas de CUT_ROD."""

from statistics import median
from time import perf_counter

from cut_rod import PRECIOS, cut_rod_memoizado, cut_rod_recursivo, cut_rod_tabulario


def medir(funcion, precios, n, repeticiones=3):
    muestras = []
    for _ in range(repeticiones):
        inicio = perf_counter()
        resultado = funcion(precios, n)
        muestras.append(perf_counter() - inicio)
    return resultado, median(muestras) * 1_000


def ejecutar_benchmark():
    print(f"{'n':>4} {'ganancia':>9} {'recursivo (ms)':>16} {'memoizado (ms)':>16} {'tabulario (ms)':>16}")
    for n in (4, 8, 12, 16, 20):
        mediciones = [medir(f, PRECIOS, n) for f in
                      (cut_rod_recursivo, cut_rod_memoizado, cut_rod_tabulario)]
        ganancias = {resultado for resultado, _ in mediciones}
        assert len(ganancias) == 1, f"Resultados diferentes para n={n}: {ganancias}"
        tiempos = [tiempo for _, tiempo in mediciones]
        print(f"{n:4d} {ganancias.pop():9d} {tiempos[0]:16.4f} {tiempos[1]:16.4f} {tiempos[2]:16.4f}")


if __name__ == "__main__":
    ejecutar_benchmark()
