# presentacion.py

from tkinter import Tk, Label, Button, Text, Scrollbar
from negocio import ServicioAtencion

class InterfazAtenciones:
    def __init__(self, root, servicio_atencion):
        self.root = root
        self.root.title("Sistema de Atención de TV")

        self.servicio_atencion = servicio_atencion

        self.label = Label(root, text="Bienvenido al Sistema de Atención de TV")
        self.label.pack()

        self.btn_nueva_atencion = Button(root, text="Ingresar Nueva Atención", command=self.ingresar_nueva_atencion)
        self.btn_nueva_atencion.pack()

        self.btn_mostrar_atenciones = Button(root, text="Mostrar Atenciones Realizadas", command=self.mostrar_atenciones)
        self.btn_mostrar_atenciones.pack()

    def mostrar_atenciones(self, atenciones):
        print("\n--- Atenciones Realizadas ---")
        for i, atencion in enumerate(atenciones, 1):
            print(f"{i}. Descripción: {atencion['descripcion']}, Diagnóstico: {atencion['diagnostico']}, "
                  f"Servicio: {atencion['servicio']}, Precio: {atencion['precio']}, "
                  f"Fecha y Hora: {atencion['fecha_hora_registro']}")

    def ingresar_nueva_atencion(self):
        descripcion = input("Descripción de la TV (recepción): ")
        diagnostico = input("Diagnóstico: ")
        servicio = input("Servicio a realizar: ")
        precio = float(input("Precio del servicio: "))

        self.servicio_atencion.registrar_atencion(descripcion, diagnostico, servicio, precio)

        print("Atención registrada correctamente.")

    def mostrar_ventana(self, titulo, contenido):
        ventana_secundaria = Tk()
        ventana_secundaria.title(titulo)

        texto = Text(ventana_secundaria, wrap="word", width=50, height=10)
        texto.insert("1.0", contenido)

        scrollbar = Scrollbar(ventana_secundaria, command=texto.yview)
        scrollbar.pack(side="right", fill="y")

        texto.config(yscrollcommand=scrollbar.set, state="disabled")
        texto.pack()

        ventana_secundaria.mainloop()
