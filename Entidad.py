# Importamos ABC para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta principal del sistema
class Entidad(ABC):
    """Representa una entidad base identificada de forma única."""

    # Constructor
    def __init__(self, entity_id):
        self._id = entity_id

    @property
    def id(self):
        """Devuelve el identificador de la entidad."""
        return self._id

    # Método obligatorio para clases hijas
    @abstractmethod
    def mostrar_info(self) -> None:
        """Muestra la información de la entidad."""