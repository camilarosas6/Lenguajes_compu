# Actividad 15. Programación dinámica: corte de una varilla

## Información

- **Nombre:** Camila Rodríguez Rosas
- **Número de cuenta:** 194100
- **Materia:** Lenguajes y Computación

## Objetivo

Encontrar la ganancia máxima al cortar una varilla de longitud `n`, dado el ingreso por cada
longitud posible de pieza. Se comparan recursión directa, memoización (top-down) y tabulación
(bottom-up).

Se usa el conjunto clásico `p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]`, donde `p[i-1]` es el
ingreso por una pieza de longitud `i`. Para poder medir hasta `n=20`, se extiende la tabla
asignando precio `2*i` a las longitudes 11..20. Si la libreta de clase usa otros precios,
sustituirlos en `cut_rod.py` y en la libreta.

## Recurrencia y análisis

`R(0) = 0` y `R(n) = max(p[i] + R(n-i))` para `1 ≤ i ≤ n`.

La recursión directa vuelve a resolver subproblemas y tiene tiempo exponencial. Memoización
guarda cada resultado; tabulación calcula `R(1), R(2), ..., R(n)` en orden. Las dos versiones
dinámicas requieren `O(n²)` tiempo y `O(n)` espacio; la tabulación evita la pila recursiva.

## Entregables y ejecución

- `Actividad15.ipynb`: libreta lista para abrir o subir a Google Colab.
- `cut_rod.py`: implementaciones reutilizables.
- `benchmark.py`: medición de los tres enfoques.

Desde este directorio ejecutar `python3 benchmark.py`. Se usa la mediana de tres mediciones,
se verifica que las ganancias coincidan y se muestran milisegundos para longitudes crecientes.
La recursión directa se limita a `n ≤ 20` porque su tiempo es exponencial. Los tiempos dependen
del equipo; deben compararse tendencias, no cifras absolutas.

## Ejemplo

Para `n = 4`, la ganancia máxima es `10`, cortando en dos piezas de longitud 2. Las tres
implementaciones deben coincidir para todos los tamaños medidos.