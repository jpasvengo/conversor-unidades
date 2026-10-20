def convertir_longitud():
    print("=== CONVERSOR DE UNIDADES DE LONGITUD ===\n")

    # 1. Solicitar el valor numérico
    try:
        valor = float(input("Introduce el valor a convertir: "))
    except ValueError:
        print(" Error: Debes ingresar un número válido.")
        return

    # 2. Solicitar la unidad de origen
    print("\n¿En qué unidad está el valor introducido?")
    print("1. Metros (m)")
    print("2. Centímetros (cm)")
    print("3. Milímetros (mm)")
    print("4. Pulgadas (in)")
    print("5. Pies (ft)")
    
    origen = input("Selecciona una opción (1-5): ").strip()

    # Convertir primero la unidad de origen a metros como base estándar
    if origen == '1':
        metros = valor
    elif origen == '2':
        metros = valor / 100
    elif origen == '3':
        metros = valor / 1000
    elif origen == '4':
        metros = valor * 0.0254
    elif origen == '5':
        metros = valor * 0.3048
    else:
        print(" Opción de unidad de origen no válida.")
        return

    # 3. Preguntar la unidad de destino (Centímetros o Milímetros)
    print("\n¿A qué unidad deseas convertirlo?")
    print("1. Centímetros (cm)")
    print("2. Milímetros (mm)")
    
    destino = input("Selecciona una opción (1 o 2): ").strip()

    # 4. Realizar la conversión final y mostrar el resultado
    if destino == '1':
        resultado = metros * 100
        unidad_destino = "cm"
    elif destino == '2':
        resultado = metros * 1000
        unidad_destino = "mm"
    else:
        print(" Opción de unidad de destino no válida.")
        return

    print(f"\n Resumen: {valor} en la unidad seleccionada equivale a {resultado:.4f} {unidad_destino}.")

if __name__ == "__main__":
    convertir_longitud()