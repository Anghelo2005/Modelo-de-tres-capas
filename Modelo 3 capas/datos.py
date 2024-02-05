# datos.py

class RepositorioAtencion:
    def __init__(self):
        self.lista_atenciones = []

    def guardar_atencion(self, descripcion, diagnostico, servicio, precio, fecha_hora_registro):
        nueva_atencion = {
            'descripcion': descripcion,
            'diagnostico': diagnostico,
            'servicio': servicio,
            'precio': precio,
            'fecha_hora_registro': fecha_hora_registro
        }
        self.lista_atenciones.append(nueva_atencion)
        print("Atención registrada correctamente.")

    def obtener_todas_atenciones(self):
        # Obtener todas las atenciones realizadas
        return self.lista_atenciones
