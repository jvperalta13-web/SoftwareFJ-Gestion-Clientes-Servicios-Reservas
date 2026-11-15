"""Define la entidad Cliente y sus datos básicos."""
# pylint: disable=invalid-name

from Entidad import Entidad
from Excepciones import ClienteError


# Clase Cliente
class Cliente(Entidad):
    """Representa un cliente con datos personales y su información básica."""

    def __init__(self, cliente_id, nombre, correo, telefono):

        # Constructor del padre
        super().__init__(cliente_id)

        # Validación nombre
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")

        # Validación correo
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Getter de nombre
    @property
    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    # Setter de nombre
    @nombre.setter
    def nombre(self, valor):

        if not valor:
            raise ClienteError("Nombre inválido")

        self.__nombre = valor

    # Getter de correo
    @property
    def correo(self):
        """Devuelve el correo electrónico del cliente."""
        return self.__correo

    # Getter de teléfono
    @property
    def telefono(self):
        """Devuelve el teléfono del cliente."""
        return self.__telefono

    # Método heredado obligatorio
    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"
