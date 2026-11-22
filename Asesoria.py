
from Servicios import Servicio
from Logger import registrar_evento


class AsesoriaEspecializada(Servicio):
    """Representa una asesoría especializada."""

    def __init__(self, nombre_o_especialidad, precio_base, especialidad=None):

        # Permite utilizar las dos formas de crear una asesoría
        if especialidad is None:
            nombre = "Asesoria"
            especialidad = nombre_o_especialidad
        else:
            nombre = nombre_o_especialidad

        super().__init__(nombre, precio_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        self.__especialidad = especialidad.strip()

        registrar_evento(
            f"Asesoría creada: {self.nombre}"
        )

    @property
    def especialidad(self):
        """Devuelve la especialidad de la asesoría."""
        return self.__especialidad

    def calcular_costo(self, horas=1, impuesto=0, descuento=0):
        """Calcula el costo según horas, impuestos y descuentos."""

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        costo = self.precio_base * horas
        costo += costo * impuesto
        costo -= costo * descuento

        registrar_evento(
            f"Costo calculado para asesoría: {self.nombre}"
        )

        return costo

    def descripcion(self):
        """Devuelve la descripción de la asesoría."""

        return (
            f"Asesoría especializada: {self.nombre} - "
            f"Especialidad: {self.__especialidad} - "
            f"Precio: ${self.precio_base}"
        )
