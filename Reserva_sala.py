from Servicios import Servicio


# Clase especializada para salas
class ReservaSala(Servicio):

    def __init__(self, capacidad, precio_base):

        super().__init__(
            "Reserva Sala",
            precio_base
        )

        self.capacidad = capacidad

    # Sobrescritura del método abstracto
    def calcular_costo(
        self,
        horas=1,
        impuesto=0,
        descuento=0
    ):

        costo = self.precio_base * horas

        costo += costo * impuesto

        costo -= costo * descuento

        return costo

    # Sobrescritura del método abstracto
    def descripcion(self):
        return f"Sala para {self.capacidad} personas"