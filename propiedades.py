import numpy as np

def format_vector(v):
    return "[" + " ".join(f"{int(x)}" if isinstance(x, (int, np.integer)) or (isinstance(x, float) and x.is_integer()) else f"{x:.2f}" for x in v) + "]"

def validar_vector(tamano, nombre_vector):
    vector = []
    for i in range(tamano):
        while True:
            try:
                elemento = float(input(f"Ingrese el elemento {i + 1} de {nombre_vector}: "))
                vector.append(elemento)
                break
            except ValueError:
                print("\u274C Error: El valor debe ser un número.")
    return np.array(vector)

def pedir_tamano():
    while True:
        tamano = input("Ingrese el tamaño de los vectores: ").strip()
        if tamano.isdigit() and int(tamano) > 0:
            return int(tamano)
        else:
            print("\u274C Error: Debe ingresar un número entero positivo.")

def conmutativa():
    print("\n\u25B6 Propiedad Conmutativa (a + b = b + a y a * b = b * a)")
    tamano = pedir_tamano()

    print("\n\u2B50 Ingresando datos del vector A")
    a = validar_vector(tamano, "A")

    print("\n\u2B50 Ingresando datos del vector B")
    b = validar_vector(tamano, "B")

    suma_ab = a + b
    suma_ba = b + a
    prod_ab = a * b
    prod_ba = b * a

    print(f"A + B = {format_vector(suma_ab)}")
    print(f"B + A = {format_vector(suma_ba)}")
    print("\u2705 ¿Se cumple la Suma conmutativa?", "Sí" if np.array_equal(suma_ab, suma_ba) else "No")

    print(f"A * B = {format_vector(prod_ab)}")
    print(f"B * A = {format_vector(prod_ba)}")
    print("\u2705 ¿Se cumple la Multiplicación conmutativa?", "Sí" if np.array_equal(prod_ab, prod_ba) else "No")

def asociativa():
    print("\n\u25B6 Propiedad Asociativa ((a + b) + c = a + (b + c) y (a * b) * c = a * (b * c))")
    tamano = pedir_tamano()

    print("\n\u2B50 Ingresando datos del vector A")
    a = validar_vector(tamano, "A")
    print("\n\u2B50 Ingresando datos del vector B")
    b = validar_vector(tamano, "B")
    print("\n\u2B50 Ingresando datos del vector C")
    c = validar_vector(tamano, "C")

    suma_izq = (a + b) + c
    suma_der = a + (b + c)
    mult_izq = (a * b) * c
    mult_der = a * (b * c)

    print(f"(A + B) + C = {format_vector(suma_izq)}")
    print(f"A + (B + C) = {format_vector(suma_der)}")
    print("\u2705 ¿Se cumple la Suma asociativa?", "Sí" if np.array_equal(suma_izq, suma_der) else "No")

    print(f"(A * B) * C = {format_vector(mult_izq)}")
    print(f"A * (B * C) = {format_vector(mult_der)}")
    print("\u2705 ¿Se cumple la Multiplicación asociativa?", "Sí" if np.array_equal(mult_izq, mult_der) else "No")

def distributiva():
    print("\n\u25B6 Propiedad Distributiva (A*(B + C) = A*B + A*C)")
    tamano = pedir_tamano()

    print("\n\u2B50 Ingresando datos del vector A")
    a = validar_vector(tamano, "A")
    print("\n\u2B50 Ingresando datos del vector B")
    b = validar_vector(tamano, "B")
    print("\n\u2B50 Ingresando datos del vector C")
    c = validar_vector(tamano, "C")

    izquierda = a * (b + c)
    derecha = (a * b) + (a * c)

    print(f"A * (B + C) = {format_vector(izquierda)}")
    print(f"(A * B) + (A * C) = {format_vector(derecha)}")
    print("\u2705 ¿Se cumple la propiedad distributiva?", "Sí" if np.array_equal(izquierda, derecha) else "No")

def inverso():
    print("\n\u25B6 Propiedad del Inverso Aditivo (a + (-a) = 0) e Inverso multiplicativo (si a != 0)")
    tamano = pedir_tamano()

    print("\n\u2B50 Ingresando datos del vector A")
    a = validar_vector(tamano, "A")

    inverso_suma = -a
    suma = a + inverso_suma
    print(f"A + (-A) = {format_vector(suma)}")
    print("\u2705 ¿Es Inverso aditivo correcto?", "Sí" if np.allclose(suma, np.zeros_like(a)) else "No")

    if np.all(a != 0):
        inverso_mult = 1 / a
        producto = a * inverso_mult
        print(f"A * (1/A) = {format_vector(producto)}")
        print("\u2705 ¿Es Inverso multiplicativo correcto?", "Sí" if np.allclose(producto, np.ones_like(a)) else "No")
    else:
        print("\u274C No se puede calcular inverso multiplicativo: el vector tiene ceros.")

def identidad():
    print("\n\u25B6 Propiedad de la Identidad Aditiva (a + 0 = a) y Multiplicativa (a * 1 = a)")
    tamano = pedir_tamano()

    print("\n\u2B50 Ingresando datos del vector A")
    a = validar_vector(tamano, "A")

    identidad_suma = np.zeros_like(a)
    identidad_mult = np.ones_like(a)

    suma = a + identidad_suma
    producto = a * identidad_mult

    print(f"A + 0 = {format_vector(suma)}")
    print("\u2705 ¿Es Identidad aditiva correcta?", "Sí" if np.array_equal(a, suma) else "No")

    print(f"A * 1 = {format_vector(producto)}")
    print("\u2705 ¿Es Identidad multiplicativa correcta?", "Sí" if np.array_equal(a, producto) else "No")

def menu():
    while True:
        print("\n===== Menú de Propiedades Aritméticas Vectoriales =====")
        print("1. Propiedad Conmutativa")
        print("2. Propiedad Asociativa")
        print("3. Propiedad Distributiva")
        print("4. Propiedad del Inverso")
        print("5. Propiedad de la Identidad")
        print("6. Salir")

        opcion = input("\U0001F4DD Ingrese el número de la opción: ").strip()
        if opcion == "1":
            conmutativa()
        elif opcion == "2":
            asociativa()
        elif opcion == "3":
            distributiva()
        elif opcion == "4":
            inverso()
        elif opcion == "5":
            identidad()
        elif opcion == "6":
            print("\u274C Saliendo del programa...")
            break
        else:
            print("\u274C Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

#FIN