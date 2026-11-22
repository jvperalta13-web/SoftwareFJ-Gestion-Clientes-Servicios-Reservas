
"""
Excepciones personalizadas para el sistema Software FJ.
"""


class SistemaError(Exception):
    """Excepción base para los errores del sistema Software FJ."""

    pass


class ClienteError(SistemaError):
    """Se produce cuando existen datos inválidos de un cliente."""

    pass


class ServicioError(SistemaError):
    """Se produce cuando ocurre un error en un servicio."""

    pass


class ReservaError(SistemaError):
    """Se produce cuando una reserva presenta información inválida."""

    pass


class ValidacionError(SistemaError):
    """Se produce cuando no se cumplen las reglas de validación."""

    pass


class EstadoReservaError(ReservaError):
    """Se produce cuando se intenta establecer un estado no permitido."""

    pass


class DuracionError(ReservaError):
    """Se produce cuando la duración de una reserva no es válida."""

    pass


class CostoError(ServicioError):
    """Se produce cuando existe un error al calcular un costo."""

    pass
