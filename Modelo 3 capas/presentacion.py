# presentacion.py

from negocio import ServicioAtencion

def mostrar_atenciones(atenciones):
    print("\n--- Atenciones Realizadas ---")
    for i, atencion in enumerate(atenciones, 1):
        print(f"{i}. Descripción: {atencion['descripcion']}, Diagnóstico: {atencion['diagnostico']}, "
              f"Servicio: {atencion['servicio']}, Precio: {atencion['precio']}, "
              f"Fecha y Hora: {atencion['fecha_hora_registro']}")

def ingresar_nueva_atencion(servicio_atencion):
    descripcion = input("Descripción de la TV (recepción): ")
    diagnostico = input("Diagnóstico: ")
    servicio = input("Servicio a realizar: ")
    precio = float(input("Precio del servicio: "))

    servicio_atencion.registrar_atencion(descripcion, diagnostico, servicio, precio)

    print("Atención registrada correctamente.")

def iniciar_programa():
    servicio_atencion = ServicioAtencion()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar Nueva Atención")
        print("2. Mostrar Atenciones Realizadas")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            # Ingresar nueva atención
            ingresar_nueva_atencion(servicio_atencion)
        elif opcion == '2':
            # Mostrar atenciones realizadas
            atenciones = servicio_atencion.obtener_atenciones()
            mostrar_atenciones(atenciones)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
