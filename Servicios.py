# Importamos ABC y abstractmethod para crear una clase abstracta
from abc import ABC, abstractmethod


# =====================================================
# CLASE ABSTRACTA SERVICIO
# =====================================================
# Esta clase representa cualquier servicio que ofrece
# la empresa Software FJ.
#
# No se puede crear un objeto directamente de esta
# clase porque es abstracta.
#
# Será heredada por:
# - ReservaSala
# - AlquilerEquipo
# - AsesoriaEspecializada
# =====================================================

class Servicio(ABC):

    # Constructor de la clase
    def __init__(self, nombre, precio_base):

        # Validación:
        # El precio no puede ser menor o igual a cero
        if precio_base <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero"
            )

        # Atributos comunes para todos los servicios
        self.nombre = nombre
        self.precio_base = precio_base

    # =================================================
    # METODO ABSTRACTO
    # =================================================
    # Obliga a las clases hijas a implementar
    # su propio cálculo de costo.
    # =================================================
    @abstractmethod
    def calcular_costo(self):
        pass

    # =================================================
    # METODO ABSTRACTO
    # =================================================
    # Obliga a las clases hijas a describir
    # el servicio que representan.
    # =================================================
    @abstractmethod
    def descripcion(self):
        pass
