# negocio.py

from datos import RepositorioAtencion
from datetime import datetime

class ServicioAtencion:
    def __init__(self):
        self.repositorio_atencion = RepositorioAtencion()

    def validar_campos_obligatorios(self, descripcion, diagnostico, servicio, precio):
        if not descripcion or not diagnostico or not servicio or precio is None:
            raise ValueError("Todos los campos son obligatorios")

    def validar_precio_no_negativo(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

    def obtener_atenciones(self):
        return self.repositorio_atencion.obtener_todas_atenciones()

    def registrar_atencion(self, descripcion, diagnostico, servicio, precio):
        # Regla de negocio 1: Validar campos obligatorios
        self.validar_campos_obligatorios(descripcion, diagnostico, servicio, precio)

        # Regla de negocio 2: Validar que el precio no sea negativo
        self.validar_precio_no_negativo(precio)

        # Guardar en el repositorio de datos con fecha y hora
        fecha_hora_registro = datetime.now()
        self.repositorio_atencion.guardar_atencion(descripcion, diagnostico, servicio, precio, fecha_hora_registro)
