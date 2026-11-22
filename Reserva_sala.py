
from Servicios import Servicio
from Logger import registrar_evento
from Excepciones import ServicioError


class ReservaSala(Servicio):
    """Representa el servicio de reserva de salas."""

    def __init__(self, capacidad, precio_base):

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise ServicioError(
                "La capacidad debe ser un número entero mayor que cero."
            )

        super().__init__("Reserva Sala", precio_base)

        self.capacidad = capacidad

        registrar_evento(
            f"Servicio de sala creado con capacidad para {capacidad} personas."
        )

    def calcular_costo(self, horas=1, impuesto=0, descuento=0):
        """Calcula el costo de la reserva de sala."""

        if not isinstance(horas, (int, float)) or isinstance(horas, bool) or horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        if not 0 <= impuesto <= 1:
            raise ValueError("El impuesto debe estar entre 0 y 1.")

        if not 0 <= descuento <= 1:
            raise ValueError("El descuento debe estar entre 0 y 1.")

        costo = self.precio_base * horas
        costo += costo * impuesto
        costo -= costo * descuento

        registrar_evento(
            f"Costo de reserva de sala calculado: ${costo:.2f}"
        )

        return round(costo, 2)

    def descripcion(self):
        """Devuelve la descripción de la sala."""

        return f"Sala para {self.capacidad} personas"
