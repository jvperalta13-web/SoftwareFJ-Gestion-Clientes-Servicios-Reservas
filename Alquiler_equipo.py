from Servicios import Servicio


# Clase especializada para alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(
        self,
        equipo,
        precio_base
    ):

        super().__init__(
            "Alquiler Equipo",
            precio_base
        )

        self.equipo = equipo

    def calcular_costo(
        self,
        dias=1,
        impuesto=0,
        descuento=0
    ):

        costo = self.precio_base * dias

        costo += costo * impuesto

        costo -= costo * descuento

        return costo

    def descripcion(self):
        return f"Equipo: {self.equipo}"