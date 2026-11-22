
"""
Sistema de Gestión de Reservas - Software FJ

Este archivo define la clase Reserva, encargada de
relacionar un cliente con un servicio y controlar
el estado y el costo de cada reserva.
"""

from Entidad import Entidad
from Cliente import Cliente
from Servicios import Servicio
from Excepciones import ReservaError
from Logger import registrar_evento, registrar_error


class Reserva(Entidad):
    """Representa una reserva realizada por un cliente."""

    contador = 0

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ReservaError("El cliente no es válido.")

        if not isinstance(servicio, Servicio):
            raise ReservaError("El servicio no es válido.")

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ReservaError(
                "La duración debe ser un número mayor que cero."
            )

        Reserva.contador += 1
        super().__init__(Reserva.contador)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        registrar_evento(
            f"Reserva {self.id} creada correctamente."
        )

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def procesar(self):
        """Confirma una reserva pendiente."""

        try:
            if self.__estado != "Pendiente":
                raise ReservaError(
                    "Solo se pueden procesar reservas pendientes."
                )

            self.__estado = "Confirmada"

        except ReservaError as error:
            registrar_error(str(error))
            raise

        else:
            registrar_evento(
                f"Reserva {self.id} confirmada correctamente."
            )
            return True

        finally:
            registrar_evento(
                f"Finalizó el intento de procesar la reserva {self.id}."
            )

    def cancelar(self):
        """Cancela una reserva que no esté finalizada."""

        if self.__estado == "Finalizada":
            raise ReservaError(
                "No se puede cancelar una reserva finalizada."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.id} cancelada."
        )

    def finalizar(self):
        """Finaliza una reserva confirmada."""

        if self.__estado != "Confirmada":
            raise ReservaError(
                "Solo se pueden finalizar reservas confirmadas."
            )

        self.__estado = "Finalizada"

        registrar_evento(
            f"Reserva {self.id} finalizada correctamente."
        )

    def calcular_costo(self):
        """Calcula el costo según el tipo de servicio."""

        try:
            if self.__servicio.nombre == "Reserva Sala":
                total = self.__servicio.calcular_costo(
                    horas=self.__duracion
                )

            elif self.__servicio.nombre == "Alquiler Equipo":
                total = self.__servicio.calcular_costo(
                    dias=self.__duracion
                )

            else:
                total = (
                    self.__servicio.calcular_costo()
                    * self.__duracion
                )

            registrar_evento(
                f"Costo de reserva {self.id}: ${total:.2f}"
            )

            return round(total, 2)

        except Exception as error:
            registrar_error(
                f"Error al calcular la reserva {self.id}: {error}"
            )
            raise ReservaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def mostrar_info(self):
        """Devuelve la información completa de la reserva."""

        return (
            f"Reserva: {self.id}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )
