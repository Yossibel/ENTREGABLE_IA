import numpy as np

# Límites máximos
MAX_MATRICES = 20
MAX_FILAS = 10
MAX_COLUMNAS = 10

def solicitar_entero(mensaje, permitir_cero=False, maximo=None):
    while True:
        valor = input(mensaje)
        if valor.strip() == '':
            print("\u274C No puedes dejar este campo vacío. Intenta nuevamente.")
            continue
        if not valor.isdigit():
            print("\u274C Solo se permiten números enteros positivos.")
            continue
        valor = int(valor)
        if not permitir_cero and valor == 0:
            print("\u274C El número no puede ser cero. Intenta nuevamente.")
            continue
        if maximo is not None and valor > maximo:
            print(f"\u274C El número no puede ser mayor que {maximo}. Intenta nuevamente.")
            continue
        return valor

def solicitar_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion not in opciones:
            print(f"\u274C Opción inválida. Debe ser una de {', '.join(opciones)}. Intente nuevamente.")
            continue
        return opcion

def solicitar_fila(col_num):
    fila = []
    for i in range(col_num):
        while True:
            valor = input(f"Ingrese el valor numérico para la columna {i + 1}: ")
            if valor.strip() == '':
                print("\u274C No puede ser vacío. Intente nuevamente.")
                continue
            try:
                num = float(valor)
                fila.append(num)
                break
            except ValueError:
                print("\u274C Solo se permiten valores numéricos. Intente nuevamente.")
    return fila

def solicitar_rango_aleatorio():
    while True:
        minimo = input("Ingrese el valor mínimo del rango aleatorio: ").strip()
        maximo = input("Ingrese el valor máximo del rango aleatorio: ").strip()

        if minimo == '' or maximo == '':
            print("\u274C No puede dejar vacío los valores. Intente nuevamente.")
            continue
        try:
            minimo = int(minimo)
            maximo = int(maximo)
            if minimo >= maximo:
                print("\u274C El valor mínimo debe ser menor al valor máximo. Intente nuevamente.")
                continue
            return minimo, maximo
        except ValueError:
            print("\u274C Solo se permiten números enteros. Intente nuevamente.")

def generar_matriz_manual(filas, columnas):
    matriz = []
    for f in range(filas):
        print(f"\n\U0001F4DD -- Ingresando valores para la fila {f + 1} --")
        fila = solicitar_fila(columnas)
        matriz.append(fila)
    return np.array(matriz)

def generar_matriz_aleatoria(filas, columnas):
    minimo, maximo = solicitar_rango_aleatorio()
    return np.random.randint(minimo, maximo + 1, size=(filas, columnas))

def generar_matriz():
    filas = solicitar_entero(
        f"Ingrese el número de filas (1 a {MAX_FILAS}): ", 
        permitir_cero=False, 
        maximo=MAX_FILAS
    )
    columnas = solicitar_entero(
        f"Ingrese el número de columnas (1 a {MAX_COLUMNAS}): ", 
        permitir_cero=False, 
        maximo=MAX_COLUMNAS
    )
    
    tipo = solicitar_opcion(
        "¿Desea ingresar los datos (m)anualmente o generarlos (a)utomáticamente? [m/a]: ",
        ['m', 'a']
    )
    
    if tipo == 'm':
        return generar_matriz_manual(filas, columnas)
    else:
        return generar_matriz_aleatoria(filas, columnas)

def imprimir_matriz(matriz):
    print("\n\u2705 Matriz creada:")
    print("[")  # Abre la matriz
    for fila in matriz:
        fila_formateada = ' '.join(
            f"{int(x)}" if isinstance(x, (int, np.integer)) or (isinstance(x, float) and x.is_integer()) else f"{x:.2f}"
            for x in fila
        )
        print(f" [{fila_formateada}]")
    print("]")

def crear_matrices():
    print("\n=== Creación de Múltiples Matrices ===")
    cantidad = solicitar_entero(
        f"¿Cuántas matrices desea crear? (1 a {MAX_MATRICES}): ", 
        permitir_cero=False, 
        maximo=MAX_MATRICES
    )
    
    matrices = []
    for i in range(cantidad):
        print(f"\n\U0001F31F Creando matriz {i + 1} de {cantidad}:")
        matriz = generar_matriz()
        matrices.append(matriz)
        imprimir_matriz(matriz)
    
    print("\n\U0001F31E Todas las matrices han sido creadas correctamente.")
    return matrices

# Ejecución principal
if __name__ == "__main__":
    crear_matrices()
#FIN