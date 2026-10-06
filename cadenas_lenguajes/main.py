from fastapi import FastAPI
from pydantic import BaseModel, Field

from operaciones_cadenas import (
    concatenar as concatenar_cadenas,
    unir,
    potencia as potencia_cadena
)

from operaciones_lenguajes import (
    union,
    interseccion,
    diferencia,
    concatenar as concatenar_lenguajes,
    potencia as potencia_lenguaje,
    complemento,
    primeros_elementos_kleene
)

app = FastAPI(
    title="API de Cadenas y Lenguajes - Camila R",
    description="Servicio web para realizar operaciones con cadenas y lenguajes formales.",
    version="1.0.0"
)

# ------ Modelos -------

class DosCadenas(BaseModel):
    cadena1: str
    cadena2: str

class VariasCadenas(BaseModel):
    cadenas: list[str]

class CadenaPotencia(BaseModel):
    cadena: str
    exponente: int = Field(ge=0)

class DosLenguajes(BaseModel):
    lenguaje1: list[str]
    lenguaje2: list[str]

class LenguajePotencia(BaseModel):
    lenguaje: list[str]
    exponente: int = Field(ge=0)

class ComplementoRequest(BaseModel):
    lenguaje: list[str]
    alfabeto: list[str]
    longitud_maxima: int = Field(ge=0)

class KleeneRequest(BaseModel):
    lenguaje: list[str]
    max_elementos: int = Field(gt=0)

# --- Inicio ---
@app.get("/")
def inicio():
    return {
        "mensaje": "API de operaciones de cadenas y lenguajes funciona"
    }

# Operaciones con cadenas
@app.post("/cadenas/concatenar")
def endpoint_concatenar_cadenas(datos: DosCadenas):
    resultado = concatenar_cadenas(
        datos.cadena1,
        datos.cadena2
    )

    return {
        "cadena1": datos.cadena1,
        "cadena2": datos.cadena2,
        "resultado": resultado
    }

@app.post("/cadenas/unir")
def endpoint_unir_cadenas(datos: VariasCadenas):
    resultado = unir(datos.cadenas)

    return {
        "cadenas": datos.cadenas,
        "resultado": resultado
    }

@app.post("/cadenas/potencia")
def endpoint_potencia_cadena(datos: CadenaPotencia):
    resultado = potencia_cadena(
        datos.cadena,
        datos.exponente
    )

    return {
        "cadena": datos.cadena,
        "exponente": datos.exponente,
        "resultado": resultado
    }

# Operaciones con lenguajes

@app.post("/lenguajes/union")
def endpoint_union(datos: DosLenguajes):
    resultado = union(
        set(datos.lenguaje1),
        set(datos.lenguaje2)
    )

    return {
        "lenguaje1": datos.lenguaje1,
        "lenguaje2": datos.lenguaje2,
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/interseccion")
def endpoint_interseccion(datos: DosLenguajes):
    resultado = interseccion(
        set(datos.lenguaje1),
        set(datos.lenguaje2)
    )

    return {
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/diferencia")
def endpoint_diferencia(datos: DosLenguajes):
    resultado = diferencia(
        set(datos.lenguaje1),
        set(datos.lenguaje2)
    )

    return {
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/concatenar")
def endpoint_concatenar_lenguajes(datos: DosLenguajes):
    resultado = concatenar_lenguajes(
        set(datos.lenguaje1),
        set(datos.lenguaje2)
    )

    return {
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/potencia")
def endpoint_potencia_lenguaje(datos: LenguajePotencia):
    resultado = potencia_lenguaje(
        set(datos.lenguaje),
        datos.exponente
    )

    return {
        "lenguaje": datos.lenguaje,
        "exponente": datos.exponente,
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/complemento")
def endpoint_complemento(datos: ComplementoRequest):
    resultado = complemento(
        set(datos.lenguaje),
        set(datos.alfabeto),
        datos.longitud_maxima
    )

    return {
        "lenguaje": datos.lenguaje,
        "alfabeto": datos.alfabeto,
        "longitud_maxima": datos.longitud_maxima,
        "resultado": sorted(resultado, key=lambda x: (len(x), x))
    }

@app.post("/lenguajes/kleene")
def endpoint_kleene(datos: KleeneRequest):
    resultado = primeros_elementos_kleene(
        set(datos.lenguaje),
        datos.max_elementos
    )

    return {
        "lenguaje": datos.lenguaje,
        "max_elementos": datos.max_elementos,
        "resultado": resultado
    }