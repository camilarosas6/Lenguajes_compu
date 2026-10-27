"""Multiplicación de enteros grandes con Karatsuba y método escolar."""

from dataclasses import dataclass


@dataclass
class Metrics:
    """Contadores de operaciones de una ejecución de Karatsuba."""

    digit_multiplications: int = 0
    recursive_calls: int = 0
    max_depth: int = 0


def _normalizar(numero: str) -> tuple[int, str]:
    texto = str(numero).strip()
    signo = -1 if texto.startswith("-") else 1
    if texto[:1] in {"-", "+"}:
        texto = texto[1:]
    if not texto or not texto.isdigit():
        raise ValueError("El valor debe ser un entero decimal.")
    texto = texto.lstrip("0") or "0"
    if texto == "0":
        signo = 1
    return signo, texto


def _sumar(a: str, b: str) -> str:
    """Suma dos enteros no negativos representados como cadenas."""
    i, j, acarreo = len(a) - 1, len(b) - 1, 0
    resultado = []
    while i >= 0 or j >= 0 or acarreo:
        total = acarreo
        if i >= 0:
            total += ord(a[i]) - 48
            i -= 1
        if j >= 0:
            total += ord(b[j]) - 48
            j -= 1
        resultado.append(chr(total % 10 + 48))
        acarreo = total // 10
    return "".join(reversed(resultado)) or "0"


def _restar(a: str, b: str) -> str:
    """Resta b de a; requiere a >= b >= 0."""
    i, j, prestamo = len(a) - 1, len(b) - 1, 0
    resultado = []
    while i >= 0:
        digito = ord(a[i]) - 48 - prestamo
        if j >= 0:
            digito -= ord(b[j]) - 48
            j -= 1
        prestamo = 1 if digito < 0 else 0
        resultado.append(chr((digito + 10 if prestamo else digito) + 48))
        i -= 1
    return "".join(reversed(resultado)).lstrip("0") or "0"


def _desplazar(numero: str, posiciones: int) -> str:
    if numero == "0":
        return "0"
    return numero + "0" * posiciones


def _karatsuba(a: str, b: str, metrics: Metrics, umbral: int, depth: int = 0) -> str:
    metrics.recursive_calls += 1
    metrics.max_depth = max(metrics.max_depth, depth)
    a, b = a.lstrip("0") or "0", b.lstrip("0") or "0"
    if a == "0" or b == "0":
        return "0"
    if max(len(a), len(b)) <= umbral:
        # Usar el método escolar hace comparable el conteo en todos los umbrales.
        producto, operaciones = multiplicacion_escolar(a, b)
        metrics.digit_multiplications += operaciones
        return producto

    n = max(len(a), len(b))
    mitad = n // 2
    a_alto, a_bajo = (a[:-mitad] or "0"), a[-mitad:]
    b_alto, b_bajo = (b[:-mitad] or "0"), b[-mitad:]

    # División: separar cada número en parte alta y baja.
    # Conquista: calcular solo tres productos recursivos.
    z2 = _karatsuba(a_alto, b_alto, metrics, umbral, depth + 1)
    z0 = _karatsuba(a_bajo, b_bajo, metrics, umbral, depth + 1)
    suma_altas = _sumar(a_alto, a_bajo)
    suma_bajas = _sumar(b_alto, b_bajo)
    z1 = _karatsuba(suma_altas, suma_bajas, metrics, umbral, depth + 1)
    z1 = _restar(_restar(z1, z2), z0)

    # Integración: z2*10^(2m) + z1*10^m + z0.
    return _sumar(_sumar(_desplazar(z2, 2 * mitad), _desplazar(z1, mitad)), z0)


def karatsuba(a: str, b: str, umbral: int = 1) -> tuple[str, Metrics]:
    """Multiplica dos enteros decimales y devuelve (producto, métricas).

    El umbral decide cuándo resolver directamente el producto de los bloques.
    Con umbral 1 se cuentan los productos de dígitos individuales.
    """
    if umbral < 1:
        raise ValueError("El umbral debe ser un entero positivo.")
    signo_a, digitos_a = _normalizar(a)
    signo_b, digitos_b = _normalizar(b)
    metrics = Metrics()
    producto = _karatsuba(digitos_a, digitos_b, metrics, umbral)
    if signo_a != signo_b and producto != "0":
        producto = "-" + producto
    return producto, metrics


def multiplicacion_escolar(a: str, b: str) -> tuple[str, int]:
    """Multiplica con el algoritmo escolar; devuelve resultado y productos de dígitos."""
    signo_a, digitos_a = _normalizar(a)
    signo_b, digitos_b = _normalizar(b)
    if digitos_a == "0" or digitos_b == "0":
        return "0", 0
    acumulado = [0] * (len(digitos_a) + len(digitos_b))
    operaciones = 0
    for i in range(len(digitos_a) - 1, -1, -1):
        for j in range(len(digitos_b) - 1, -1, -1):
            acumulado[i + j + 1] += (ord(digitos_a[i]) - 48) * (ord(digitos_b[j]) - 48)
            operaciones += 1
    for i in range(len(acumulado) - 1, 0, -1):
        acumulado[i - 1] += acumulado[i] // 10
        acumulado[i] %= 10
    resultado = "".join(map(str, acumulado)).lstrip("0") or "0"
    if signo_a != signo_b and resultado != "0":
        resultado = "-" + resultado
    return resultado, operaciones
