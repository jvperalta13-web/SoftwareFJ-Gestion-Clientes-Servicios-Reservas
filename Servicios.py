
from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, nombre, precio_base):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if (
            not isinstance(precio_base, (int, float))
            or isinstance(precio_base, bool)
            or precio_base <= 0
        ):
            raise ValueError("El precio debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def descripcion(self):
        """Describe el servicio ofrecido."""
        pass
