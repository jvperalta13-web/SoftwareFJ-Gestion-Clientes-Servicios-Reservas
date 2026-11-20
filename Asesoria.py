from Servicios import Servicio


# Clase especializada para asesorías
class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        especialidad,
        precio_base
    ):

        super().__init__(
            "Asesoria",
            precio_base
        )

        self.especialidad = especialidad

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

    def descripcion(self):
        return f"Asesoría en {self.especialidad}"
