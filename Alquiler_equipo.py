
from Servicios import Servicio
from Logger import registrar_evento
from Excepciones import ServicioError


class AlquilerEquipo(Servicio):
    """Representa el servicio de alquiler de equipos."""

    def __init__(self, equipo, precio_base):

        if not isinstance(equipo, str) or not equipo.strip():
            raise ServicioError(
                "El nombre del equipo no puede estar vacío."
            )

        super().__init__("Alquiler Equipo", precio_base)

        self.equipo = equipo.strip()

        registrar_evento(
            f"Equipo registrado para alquiler: {self.equipo}"
        )

    def calcular_costo(self, dias=1, impuesto=0, descuento=0):
        """Calcula el costo del alquiler según los días."""

        if not isinstance(dias, (int, float)) or isinstance(dias, bool) or dias <= 0:
            raise ValueError(
                "Los días de alquiler deben ser mayores que cero."
            )

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 1
        ):
            raise ValueError(
                "El impuesto debe estar entre 0 y 1."
            )

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 1
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 1."
            )

        costo = self.precio_base * dias

        costo += costo * impuesto

        costo -= costo * descuento

        registrar_evento(
            f"Costo de alquiler calculado para {self.equipo}: ${costo:.2f}"
        )

        return round(costo, 2)

    def descripcion(self):
        """Devuelve la descripción del equipo alquilado."""

        return f"Equipo: {self.equipo}"
