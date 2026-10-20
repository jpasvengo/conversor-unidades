"""
Lógica del Conversor de Unidades y funciones auxiliares para interfaz gráfica.
Permite convertir unidades de longitud e intercambiar selecciones de origen y destino.
"""

from typing import Tuple, Dict

# Factores de conversión referenciados al metro (m)
FACTORES_A_METROS: Dict[str, float] = {
    "Metros (m)": 1.0,
    "Centímetros (cm)": 0.01,
    "Milímetros (mm)": 0.001,
    "Pulgadas (in)": 0.0254,
    "Pies (ft)": 0.3048,
    "Yardas (yd)": 0.9144,
    # Abreviaturas estándar
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
}

SIMBOLOS: Dict[str, str] = {
    "Metros (m)": "m",
    "Centímetros (cm)": "cm",
    "Milímetros (mm)": "mm",
    "Pulgadas (in)": "in",
    "Pies (ft)": "ft",
    "Yardas (yd)": "yd",
    "m": "m",
    "cm": "cm",
    "mm": "mm",
    "in": "in",
    "ft": "ft",
    "yd": "yd",
}


def convertir(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    """Convierte un valor numérico de la unidad de origen a la unidad de destino."""
    if unidad_origen not in FACTORES_A_METROS:
        raise ValueError(f"Unidad de origen no reconocida: '{unidad_origen}'")
    if unidad_destino not in FACTORES_A_METROS:
        raise ValueError(f"Unidad de destino no reconocida: '{unidad_destino}'")

    metros = valor * FACTORES_A_METROS[unidad_origen]
    resultado = metros / FACTORES_A_METROS[unidad_destino]
    return resultado


def intercambiar_unidades(origen: str, destino: str) -> Tuple[str, str]:
    """
    Intercambia las unidades de origen y destino.
    Devuelve la tupla (nuevo_origen, nuevo_destino).
    """
    return destino, origen


def formatear_resultado(resultado: float) -> str:
    """Formatea el número obtenido de manera limpia sin ceros innecesarios."""
    if resultado.is_integer():
        return str(int(resultado))
    return f"{resultado:.6g}"
