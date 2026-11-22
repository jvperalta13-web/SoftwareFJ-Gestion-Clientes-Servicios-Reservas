
"""
Excepciones personalizadas para el sistema Software FJ.
"""


class SistemaError(Exception):
    """Excepción base para los errores del sistema Software FJ."""
    pass


class ClienteError(SistemaError):
    """Error relacionado con los datos de un cliente."""
    pass


class ServicioError(SistemaError):
    """Error relacionado con un servicio."""
    pass


class ReservaError(SistemaError):
    """Error relacionado con una reserva."""
    pass


class ValidacionError(SistemaError):
    """Error cuando no se cumplen las reglas de validación."""
    pass


class EstadoReservaError(ReservaError):
    """Error cuando se establece un estado no permitido."""
    pass


class DuracionError(ReservaError):
    """Error cuando la duración de una reserva no es válida."""
    pass


class CostoError(ServicioError):
    """Error cuando ocurre un problema al calcular un costo."""
    pass
