"""Definiciones de servicios abstractos para la aplicación."""

# pylint: disable=invalid-name

import abc


# Clase abstracta Servicio
class Servicio(abc.ABC):
    """Representa un servicio abstracto con nombre y precio base."""

    def __init__(self, nombre, precio_base):

        # Validar precio
        if precio_base <= 0:
            raise ValueError("Precio inválido")

        self.nombre = nombre
        self.precio_base = precio_base

    # Método abstracto
    @abc.abstractmethod
    def calcular_costo(self):
        """Calcula el costo total del servicio."""

    # Método abstracto
    @abc.abstractmethod
    def descripcion(self):
        """Devuelve la descripción del servicio."""