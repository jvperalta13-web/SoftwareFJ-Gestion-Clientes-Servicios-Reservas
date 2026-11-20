from Excepciones import ReservaError


# Clase Reserva
class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):
        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):
        self.estado = "Cancelada"

    # Procesar reserva
    def procesar(self):

        if self.duracion <= 0:

            raise ReservaError(
                "La duración no puede ser negativa"
            )

        self.confirmar()

    # Mostrar información
    def mostrar(self):

        print(
            f"Estado: {self.estado}"
        )