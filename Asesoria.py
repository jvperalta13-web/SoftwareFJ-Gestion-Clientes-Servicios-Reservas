
from Servicios import Servicio
from Logger import registrar_evento


class AsesoriaEspecializada(Servicio):
    """Representa una asesoría especializada."""

    def __init__(self, nombre, precio_base, especialidad="General"):

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

    def calcular_costo(self):
        """Devuelve el precio base de la asesoría."""

        registrar_evento(
            f"Costo calculado para asesoría: {self.nombre}"
        )

        return self.precio_base

    def descripcion(self):
        """Devuelve la descripción de la asesoría."""

        return (
            f"Asesoría especializada: {self.nombre} - "
            f"Especialidad: {self.__especialidad} - "
            f"Precio: ${self.precio_base}"
        )
