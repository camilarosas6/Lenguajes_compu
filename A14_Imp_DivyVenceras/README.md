# A14 — Implementación de Divide y Vencerás: Karatsuba

Implementación recursiva de Karatsuba para multiplicar enteros decimales de gran tamaño. La representación de los operandos es texto, de modo que el algoritmo no depende de convertir el número completo al tipo entero nativo.

## Requisitos

- Python 3.10 o posterior.
- No requiere paquetes externos.

## Ejecutar 

Desde una terminal, entra a la carpeta `A14` y ejecuta:

```bash
python3 main.py multiplicar 12345678901234567890 98765432109876543210
python3 main.py medir
python3 ejemplos/pruebas.py
```

El primer comando enseña el resultado de Karatsuba, el método escolar y la multiplicación nativa, además de comparar los productos de dígitos y llamadas recursivas. El segundo genera operandos aleatorios reproducibles de 20, 50 y 100 dígitos, verifica que todas las variantes den el mismo resultado y reporta T(N), el pico de memoria S(N), productos de dígitos, llamadas y profundidad para umbrales 1, 2, 4 y 16. El tiempo es la mediana de las repeticiones configuradas; por defecto son siete. Se puede cambiar la cantidad con `--repeticiones 20` y la semilla con `--semilla 25`. El tercer comando ejecuta pruebas de casos borde y 300 pares aleatorios sin instalar paquetes externos.

También se puede importar `karatsuba(a, b)` desde `karatsuba.py`; devuelve una tupla con el producto decimal y los contadores de la ejecución.

## División, conquista e integración

Para operandos positivos `x` e `y`, se separan sus dígitos alrededor de `m`:

`x = a·10^m + b` y `y = c·10^m + d`.

- **División:** se obtienen los bloques altos `a`, `c` y bajos `b`, `d`.
- **Conquista:** se calculan recursivamente tres productos: `z₂ = ac`, `z₀ = bd` y `z₁ = (a+b)(c+d)`. Así se requieren tres productos recursivos en vez de cuatro.
- **Integración:** se usa `xy = z₂·10^(2m) + (z₁-z₂-z₀)·10^m + z₀`.

El caso base multiplica directamente cuando ambos bloques tienen como máximo `umbral` dígitos. El umbral predeterminado es 1; la medición también prueba 2 y 4 para mostrar la variante híbrida que reduce llamadas recursivas.

## Análisis de complejidad

Sea `n` la cantidad de dígitos. Con división en mitades, el tiempo satisface `T(n) = 3T(n/2) + O(n)`, por lo que `T(n) = Θ(n^(log₂ 3)) ≈ Θ(n^1.585)`. El método escolar realiza `n²` productos de dígitos: `Θ(n²)`. La cantidad de productos de dígitos de Karatsuba cambia con el tamaño y el umbral del caso base; el programa la cuenta para cada ejecución. Las mediciones incluyen además el tiempo observado, que puede verse afectado por el intérprete y el hardware.

La profundidad de recursión es `O(log n)`. La pila usa `O(log n)` espacio; contando las cadenas temporales que se crean en las llamadas, el espacio auxiliar máximo es `O(n)`. La medición práctica de S(N) usa `tracemalloc` y muestra el pico de memoria Python en KB; la entrada ya creada queda fuera de la medición. T(N) y S(N) se miden en ejecuciones separadas para que el rastreo de memoria no distorsione el tiempo.

La multiplicación nativa se incluye como referencia práctica. En Python usa enteros de precisión arbitraria y una implementación interna optimizada, por eso no es una medición del método escolar ni una comparación aislada de Karatsuba.

## Comparación con la versión de la carpeta de la actividad

La carpeta `Actividad14-Implementación-De-Estrategia-Divide-Y-Vencerás` incluye una API FastAPI con endpoints, tipos Pydantic, gráficas, mediciones de memoria y un conjunto amplio de pruebas. Su implementación representa los números como listas de dígitos little-endian; esta entrega los representa como cadenas decimales y tiene una interfaz de terminal sin dependencias externas. Ambas implementan Karatsuba recursivo y el método escolar a mano, con el entero nativo limitado a referencia/validación.

De esa versión se incorporaron aquí la medición explícita de S(N), los contadores de profundidad, la variante híbrida mediante umbrales configurables y las pruebas deterministas de bordes y pares aleatorios. Se mantiene la interfaz CLI para que la actividad se pueda ejecutar con Python estándar, sin instalar FastAPI, Uvicorn o Matplotlib. Las gráficas y la API de la otra carpeta siguen disponibles allí; esta carpeta genera sus datos de medición en consola.

## Estructura

- `karatsuba.py`: suma, resta, desplazamiento decimal, Karatsuba y multiplicación escolar.
- `main.py`: demostración y mediciones con validación de resultados.
- `ejemplos/pruebas.py`: pruebas funcionales deterministas sin dependencias.
