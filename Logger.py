import logging


# Configuración del archivo de logs
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Registrar eventos normales
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores
def registrar_error(mensaje):
    logging.error(mensaje)