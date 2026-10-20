# Especificación del Conversor de Unidades (SPEC)

## 1. Propósito
Aplicación de conversión de unidades de longitud con interfaz gráfica (Tkinter) y soporte para operaciones interactivas.

## 2. Unidades Soportadas
- Metros (m)
- Centímetros (cm)
- Milímetros (mm)
- Pulgadas (in)
- Pies (ft)
- Yardas (yd)

## 3. Funcionalidad de Conversión
- Entrada de valor numérico (admite enteros y decimales con punto o coma).
- Selección de unidad de origen y destino.
- Cálculo preciso usando el metro (m) como unidad base estándar.
- Presentación de resultado destacado y resumen explicativo.

## 4. Botón Intercambiar Unidades (Mejora Issue #1)
- **Acción:** Al presionar el botón "Intercambiar unidades" (o icono `⇄`), intercambia la unidad de Origen y la de Destino.
- **Comportamiento:**
  - Conserva exactamente el texto escrito en el campo de Valor.
  - Borra el resultado anterior, restableciéndolo a `—`.
  - No ejecuta la conversión de forma automática.
  - El botón "Convertir" sigue funcionando normalmente.
  - Pulsarlo dos veces restaura las unidades originales.
