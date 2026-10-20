"""
Conversor interactivo de unidades de longitud con interfaz gráfica (Tkinter y ttk).
Incluye botón para intercambiar unidades de origen y destino (Issue #1).
"""

import tkinter as tk
from tkinter import ttk, messagebox
from logica_conversor import (
    FACTORES_A_METROS,
    SIMBOLOS,
    convertir,
    intercambiar_unidades,
    formatear_resultado,
)

# --- PALETA DE COLORES MODERNA ---
COLOR_FONDO_VENTANA = "#0D1B2A"       # Azul oscuro profundo
COLOR_PANEL = "#16263D"               # Panel ligeramente más claro
COLOR_BORDE_PANEL = "#24364F"         # Borde del panel
COLOR_FONDO_INPUT = "#0D1B2A"         # Fondo de campos
COLOR_BORDE_INPUT = "#2E4057"         # Borde de campos
COLOR_TEXTO_ETIQUETA = "#B0C4DE"      # Azul grisáceo claro
COLOR_TEXTO_BLANCO = "#FFFFFF"        # Texto blanco
COLOR_ACENTO = "#5DE3C1"              # Turquesa brillante
COLOR_BOTON_HOVER = "#4AC6A7"         # Hover botón calcular
COLOR_BOTON_SEC = "#24364F"           # Botón secundario limpiar / intercambiar
COLOR_BOTON_SEC_HOVER = "#1E2D42"

UNIDADES_DISPONIBLES = [
    "Metros (m)",
    "Centímetros (cm)",
    "Milímetros (mm)",
    "Pulgadas (in)",
    "Pies (ft)",
    "Yardas (yd)",
]


def configurar_estilos() -> None:
    """Configura los estilos de ttk para los menús desplegables."""
    estilo = ttk.Style()
    estilo.theme_use("clam")

    estilo.configure(
        "TCombobox",
        fieldbackground=COLOR_FONDO_INPUT,
        background=COLOR_BOTON_SEC,
        foreground=COLOR_TEXTO_BLANCO,
        arrowcolor=COLOR_ACENTO,
        bordercolor=COLOR_BORDE_INPUT,
        lightcolor=COLOR_BORDE_INPUT,
        darkcolor=COLOR_BORDE_INPUT,
        padding=6,
    )
    estilo.map(
        "TCombobox",
        fieldbackground=[("readonly", COLOR_FONDO_INPUT)],
        foreground=[("readonly", COLOR_TEXTO_BLANCO)],
        selectbackground=[("readonly", COLOR_FONDO_INPUT)],
        selectforeground=[("readonly", COLOR_TEXTO_BLANCO)],
    )


def accion_convertir(
    entrada_valor: tk.Entry,
    combo_origen: ttk.Combobox,
    combo_destino: ttk.Combobox,
    etiqueta_resultado: tk.Label,
    etiqueta_resumen: tk.Label,
) -> None:
    """Valida la entrada del usuario y muestra el cálculo de la conversión."""
    texto_valor = entrada_valor.get().strip().replace(",", ".")
    unidad_origen = combo_origen.get().strip()
    unidad_destino = combo_destino.get().strip()

    if not texto_valor:
        messagebox.showwarning(
            "Campo vacío",
            "Por favor, introduce un valor numérico para convertir.",
        )
        return

    try:
        valor_original = float(texto_valor)
    except ValueError:
        messagebox.showerror(
            "Entrada no válida",
            "Debes ingresar un número válido (ejemplos: 10, 3.5, 0.25).",
        )
        return

    try:
        resultado = convertir(valor_original, unidad_origen, unidad_destino)
    except ValueError as err:
        messagebox.showwarning("Error en selección", str(err))
        return

    texto_num = formatear_resultado(resultado)
    simbolo_origen = SIMBOLOS.get(unidad_origen, "")
    simbolo_destino = SIMBOLOS.get(unidad_destino, "")

    etiqueta_resultado.config(text=f"{texto_num} {simbolo_destino}")
    etiqueta_resumen.config(
        text=f"{valor_original:g} {simbolo_origen} = {texto_num} {simbolo_destino}"
    )


def accion_intercambiar(
    entrada_valor: tk.Entry,
    combo_origen: ttk.Combobox,
    combo_destino: ttk.Combobox,
    etiqueta_resultado: tk.Label,
    etiqueta_resumen: tk.Label,
) -> None:
    """
    Intercambia la unidad de origen y destino.
    Conserva el texto escrito en valor, borra el resultado anterior a '—' y no convierte automáticamente.
    """
    origen_actual = combo_origen.get()
    destino_actual = combo_destino.get()

    nuevo_origen, nuevo_destino = intercambiar_unidades(origen_actual, destino_actual)

    combo_origen.set(nuevo_origen)
    combo_destino.set(nuevo_destino)

    # Restablecer el resultado a '—' sin alterar el campo de valor
    etiqueta_resultado.config(text="—")
    etiqueta_resumen.config(text="Unidades intercambiadas. Presiona Convertir para calcular.")


def accion_limpiar(
    entrada_valor: tk.Entry,
    combo_origen: ttk.Combobox,
    combo_destino: ttk.Combobox,
    etiqueta_resultado: tk.Label,
    etiqueta_resumen: tk.Label,
) -> None:
    """Restablece los campos de entrada y la etiqueta de resultado a su estado inicial."""
    entrada_valor.delete(0, tk.END)
    combo_origen.current(0)
    combo_destino.current(1)
    etiqueta_resultado.config(text="—")
    etiqueta_resumen.config(text="Introduce un número y presiona Convertir")
    entrada_valor.focus_set()


def crear_interfaz() -> None:
    """Construye y lanza la ventana principal del conversor."""
    ventana = tk.Tk()
    ventana.title("Conversor de Unidades")
    ventana.geometry("640x500")
    ventana.minsize(580, 460)
    ventana.configure(bg=COLOR_FONDO_VENTANA)

    configurar_estilos()

    # Panel contenedor principal
    panel = tk.Frame(
        ventana,
        bg=COLOR_PANEL,
        padx=28,
        pady=22,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE_PANEL,
    )
    panel.pack(expand=True, fill="both", padx=25, pady=25)

    # Título
    titulo = tk.Label(
        panel,
        text="Conversor de Unidades de Longitud",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_BLANCO,
        font=("Segoe UI", 16, "bold"),
    )
    titulo.pack(pady=(0, 16))

    # Campo de Valor
    lbl_valor = tk.Label(
        panel,
        text="Valor numérico:",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_ETIQUETA,
        font=("Segoe UI", 10, "bold"),
    )
    lbl_valor.pack(anchor="w", pady=(0, 5))

    marco_input = tk.Frame(panel, bg=COLOR_BORDE_INPUT, padx=1, pady=1)
    marco_input.pack(fill="x", pady=(0, 16))

    entrada_valor = tk.Entry(
        marco_input,
        bg=COLOR_FONDO_INPUT,
        fg=COLOR_TEXTO_BLANCO,
        insertbackground=COLOR_ACENTO,
        font=("Segoe UI", 13),
        relief=tk.FLAT,
        justify="center",
    )
    entrada_valor.pack(fill="both", expand=True, ipady=6, padx=3)

    # Fila de selección de unidades con botón de intercambio central
    fila_unidades = tk.Frame(panel, bg=COLOR_PANEL)
    fila_unidades.pack(fill="x", pady=(0, 18))
    fila_unidades.columnconfigure(0, weight=1)
    fila_unidades.columnconfigure(1, weight=0)
    fila_unidades.columnconfigure(2, weight=1)

    # 1. Origen
    col_origen = tk.Frame(fila_unidades, bg=COLOR_PANEL)
    col_origen.grid(row=0, column=0, sticky="ew", padx=(0, 6))

    lbl_origen = tk.Label(
        col_origen,
        text="Unidad de origen:",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_ETIQUETA,
        font=("Segoe UI", 10, "bold"),
    )
    lbl_origen.pack(anchor="w", pady=(0, 5))

    combo_origen = ttk.Combobox(
        col_origen,
        values=UNIDADES_DISPONIBLES,
        state="readonly",
        font=("Segoe UI", 10),
    )
    combo_origen.current(0)
    combo_origen.pack(fill="x", ipady=3)

    # 2. Botón Intercambiar Unidades (⇄)
    col_swap = tk.Frame(fila_unidades, bg=COLOR_PANEL)
    col_swap.grid(row=0, column=1, padx=6, sticky="s")

    btn_swap = tk.Button(
        col_swap,
        text="⇄ Intercambiar",
        command=lambda: accion_intercambiar(
            entrada_valor, combo_origen, combo_destino, lbl_resultado, lbl_resumen
        ),
        font=("Segoe UI", 9, "bold"),
        bg=COLOR_BOTON_SEC,
        fg=COLOR_TEXTO_BLANCO,
        activebackground=COLOR_BOTON_SEC_HOVER,
        activeforeground=COLOR_TEXTO_BLANCO,
        relief=tk.FLAT,
        cursor="hand2",
        padx=10,
        pady=5,
    )
    btn_swap.pack(pady=(20, 0))

    # 3. Destino
    col_destino = tk.Frame(fila_unidades, bg=COLOR_PANEL)
    col_destino.grid(row=0, column=2, sticky="ew", padx=(6, 0))

    lbl_destino = tk.Label(
        col_destino,
        text="Unidad de destino:",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_ETIQUETA,
        font=("Segoe UI", 10, "bold"),
    )
    lbl_destino.pack(anchor="w", pady=(0, 5))

    combo_destino = ttk.Combobox(
        col_destino,
        values=UNIDADES_DISPONIBLES,
        state="readonly",
        font=("Segoe UI", 10),
    )
    combo_destino.current(1)
    combo_destino.pack(fill="x", ipady=3)

    # Botones principales: Convertir y Limpiar
    fila_botones = tk.Frame(panel, bg=COLOR_PANEL)
    fila_botones.pack(pady=(0, 16))

    btn_convertir = tk.Button(
        fila_botones,
        text="Convertir",
        command=lambda: accion_convertir(
            entrada_valor, combo_origen, combo_destino, lbl_resultado, lbl_resumen
        ),
        font=("Segoe UI", 11, "bold"),
        bg=COLOR_ACENTO,
        fg=COLOR_FONDO_VENTANA,
        activebackground=COLOR_BOTON_HOVER,
        activeforeground=COLOR_FONDO_VENTANA,
        relief=tk.FLAT,
        cursor="hand2",
        padx=24,
        pady=7,
    )
    btn_convertir.pack(side="left", padx=8)

    btn_limpiar = tk.Button(
        fila_botones,
        text="Limpiar",
        command=lambda: accion_limpiar(
            entrada_valor, combo_origen, combo_destino, lbl_resultado, lbl_resumen
        ),
        font=("Segoe UI", 11, "bold"),
        bg=COLOR_BOTON_SEC,
        fg=COLOR_TEXTO_BLANCO,
        activebackground=COLOR_BOTON_SEC_HOVER,
        activeforeground=COLOR_TEXTO_BLANCO,
        relief=tk.FLAT,
        cursor="hand2",
        padx=20,
        pady=7,
    )
    btn_limpiar.pack(side="left", padx=8)

    # Resultados
    lbl_resultado = tk.Label(
        panel,
        text="—",
        bg=COLOR_PANEL,
        fg=COLOR_ACENTO,
        font=("Segoe UI", 22, "bold"),
    )
    lbl_resultado.pack(pady=(4, 4))

    lbl_resumen = tk.Label(
        panel,
        text="Introduce un número y presiona Convertir",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_ETIQUETA,
        font=("Segoe UI", 10, "italic"),
        wraplength=500,
    )
    lbl_resumen.pack()

    # Atajo: presionar Enter ejecuta la conversión
    ventana.bind(
        "<Return>",
        lambda event: accion_convertir(
            entrada_valor, combo_origen, combo_destino, lbl_resultado, lbl_resumen
        ),
    )

    entrada_valor.focus_set()
    ventana.mainloop()


if __name__ == "__main__":
    crear_interfaz()
