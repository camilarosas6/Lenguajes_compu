# Implementación de operaciones con cadenas y lenguajes

**Nombre completo:** Camila Rodríguez Rosas
**Materia:** Lenguajes de Computación
**Número de cuenta:** 194100-0
**Título:** Implementación de operaciones con cadenas y lenguajes

## Descripción

Se usa **FastAPI** para aplicar operaciones sobre cadenas y lenguajes formales. Un lenguaje se representa como una lista de cadenas y la cadena vacía (λ) se escribe como `""` en las solicitudes y respuestas.

Se incluyen operaciones de concatenación, unión y potencia para cadenas, así como operaciones de conjuntos, concatenación, potencia, complemento y clausura de Kleene para lenguajes.

## Se utilizó: 

- Python
- FastAPI
- Uvicorn
- Jupyter Notebook

## Estructura del proyecto

```text
.
├── main.py
├── operaciones_cadenas.py
├── operaciones_lenguajes.py
├── ejercicios.ipynb
├── requirements.txt
└── README.md
```

| Archivo | Descripción |
|---|---|
| `main.py` | Define la aplicación FastAPI, los modelos de entrada y los endpoints. |
| `operaciones_cadenas.py` | Implementa las operaciones aplicables a cadenas. |
| `operaciones_lenguajes.py` | Implementa las operaciones aplicables a lenguajes formales. |
| `ejercicios.ipynb` | Contiene ejercicios y pruebas complementarias. |
| `requirements.txt` | Lista las dependencias necesarias para ejecutar el proyecto. |

## Instrucciones para ejecutar

```bash
# Crear y activar un entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Levantar la API
uvicorn main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000` y su documentación interactiva en `http://127.0.0.1:8000/docs`.

Para abrir el notebook de ejercicios:

```bash
jupyter notebook ejercicios.ipynb
```

## Endpoints

### Cadenas

| Endpoint | Cuerpo de la solicitud | Descripción |
|---|---|---|
| `POST /cadenas/concatenar` | `{ "cadena1": "Hola", "cadena2": "Mundo" }` | Concatena dos cadenas. |
| `POST /cadenas/unir` | `{ "cadenas": ["Hola", " ", "mundo"] }` | Une una lista de cadenas en el orden recibido. |
| `POST /cadenas/potencia` | `{ "cadena": "ab", "exponente": 3 }` | Repite una cadena un número de veces: `wⁿ`. |

Ejemplo de resultado para la potencia de una cadena:

```text
"ab"³ = "ababab"
```

### Lenguajes

| Endpoint | Cuerpo de la solicitud | Descripción |
|---|---|---|
| `POST /lenguajes/union` | `{ "lenguaje1": ["a", "b"], "lenguaje2": ["b", "c"] }` | Calcula `L ∪ M`. |
| `POST /lenguajes/interseccion` | `{ "lenguaje1": ["a", "b"], "lenguaje2": ["b", "c"] }` | Calcula `L ∩ M`. |
| `POST /lenguajes/diferencia` | `{ "lenguaje1": ["a", "b"], "lenguaje2": ["b", "c"] }` | Calcula `L − M`. |
| `POST /lenguajes/concatenar` | `{ "lenguaje1": ["a", "b"], "lenguaje2": ["c", "d"] }` | Calcula la concatenación `L · M`. |
| `POST /lenguajes/potencia` | `{ "lenguaje": ["a", "b"], "exponente": 2 }` | Calcula la potencia de un lenguaje, `Lⁿ`. |
| `POST /lenguajes/complemento` | `{ "lenguaje": ["a"], "alfabeto": ["a", "b"], "longitud_maxima": 2 }` | Calcula el complemento respecto a `Σ*` hasta la longitud indicada. |
| `POST /lenguajes/kleene` | `{ "lenguaje": ["a", "b"], "max_elementos": 8 }` | Devuelve los primeros elementos de `L*` en orden por longitud y lexicográfico. |

## Ejercicios

Dado el alfabeto `Σ = {a, b}` y los lenguajes:

- `L = {λ, a, b}`
- `M = {b, aa}`

### 1 Operaciones de conjuntos

| Operación | Resultado |
|---|---|
| `L ∪ M` | `{λ, a, b, aa}` |
| `L ∩ M` | `{b}` |
| `L − M` | `{λ, a}` |
| `M − L` | `{aa}` |

### 2 Operaciones sobre lenguajes

| Operación | Resultado |
|---|---|
| `L · M` | `{b, aa, ab, bb, aaa, baa}` |
| `M · L` | `{b, aa, ba, bb, aaa, aab}` |
| `M²` | `{bb, aab, baa, aaaa}` |

### 3 Clausura de Kleene y combinación

| Operación | Resultado |
|---|---|
| `L*` (primeros 8 elementos) | `{λ, a, b, aa, ab, ba, bb, aaa}` |
| `M*` (primeros 8 elementos) | `{λ, b, aa, bb, aab, baa, bbb, aaaa}` |
| `(L · M) ∪ (M* ∩ L²)` | `{λ, b, aa, ab, bb, aaa, baa}` |

## Para probar

Se puede probar desde la documentación interactiva de FastAPI:

```text
http://127.0.0.1:8000/docs
```

Se incluyen ejercicios y pruebas adicionales en `ejercicios.ipynb` como documentación