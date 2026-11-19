"""
Sistema de Gestión de Reservas - Software FJ

Archivo principal del programa.
Aquí se realizan las pruebas solicitadas en el trabajo,
creando clientes, servicios y reservas.
También se manejan los errores y se registran eventos.
"""

# Importamos las clases del proyecto
from Cliente import Cliente
from Reserva_sala import ReservaSala
from Alquiler_equipo import AlquilerEquipo
from Asesoria import AsesoriaEspecializada
from Reserva import Reserva
from Excepciones import ClienteError, ServicioError, ReservaError

# Importamos las funciones para registrar eventos y errores
from Logger import registrar_evento
from Logger import registrar_error


# =====================================
# INICIO DEL SISTEMA
# =====================================

print("===================================")
print(" SISTEMA DE RESERVAS SOFTWARE FJ ")
print("===================================")

# Lista para almacenar clientes
clientes = []

# Lista para almacenar reservas
reservas = []


# =====================================
# OPERACIÓN 1
# REGISTRO DE CLIENTE VÁLIDO
# =====================================

try:

    # Se crea un cliente con datos válidos
    cliente1 = Cliente(
        1,
        "Sebastian",
        "sebastian@gmail.com",
        "300111111"
    )

    # Se guarda en la lista
    clientes.append(cliente1)

    # Se registra el evento en el log
    registrar_evento(
        "Cliente 1 registrado correctamente"
    )

    print("Operación 1 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    # Si ocurre un error se registra
    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 2
# REGISTRO DE SEGUNDO CLIENTE
# =====================================

try:

    cliente2 = Cliente(
        2,
        "Viviana",
        "viviana@gmail.com",
        "300222222"
    )

    clientes.append(cliente2)

    registrar_evento(
        "Cliente 2 registrado correctamente"
    )

    print("Operación 2 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 3
# CLIENTE CON ERROR
# =====================================

try:

    # Nombre vacío para generar excepción
    cliente3 = Cliente(
        3,
        "",
        "correo@gmail.com",
        "300333333"
    )

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Operación 3 fallida:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 4
# CREAR SERVICIO DE RESERVA DE SALA
# =====================================

try:

    sala = ReservaSala(
        20,
        50000
    )

    registrar_evento(
        "Servicio sala creado"
    )

    print("Operación 4 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 5
# CREAR SERVICIO DE ALQUILER EQUIPO
# =====================================

try:

    equipo = AlquilerEquipo(
        "Portátil",
        30000
    )

    registrar_evento(
        "Servicio equipo creado"
    )

    print("Operación 5 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 6
# CREAR SERVICIO DE ASESORÍA
# =====================================

try:

    asesoria = AsesoriaEspecializada(
        "Python",
        80000
    )

    registrar_evento(
        "Servicio asesoría creado"
    )

    print("Operación 6 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 7
# CREAR RESERVA EXITOSA
# =====================================

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    # Se procesa la reserva
    reserva1.procesar()

    reservas.append(reserva1)

    registrar_evento(
        "Reserva 1 creada correctamente"
    )

    print("Operación 7 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 8
# SEGUNDA RESERVA EXITOSA
# =====================================

try:

    reserva2 = Reserva(
        cliente2,
        equipo,
        2
    )

    reserva2.procesar()

    reservas.append(reserva2)

    registrar_evento(
        "Reserva 2 creada correctamente"
    )

    print("Operación 8 exitosa")

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Error:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 9
# RESERVA CON ERROR
# =====================================

try:

    # Duración negativa para generar excepción
    reserva3 = Reserva(
        cliente1,
        asesoria,
        -5
    )

    reserva3.procesar()

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Operación 9 fallida:", e)

    registrar_error(str(e))


# =====================================
# OPERACIÓN 10
# SERVICIO CON PRECIO INVÁLIDO
# =====================================

try:

    servicio_malo = ReservaSala(
        10,
        -50000
    )

except (ValueError, TypeError, ClienteError, ServicioError, ReservaError) as e:

    print("Operación 10 fallida:", e)

    registrar_error(str(e))


# =====================================
# DEMOSTRACIÓN DE POLIMORFISMO
# =====================================

print("\nPRUEBA DE POLIMORFISMO")

servicios = [
    sala,
    equipo,
    asesoria
]

# Cada objeto ejecuta su propia versión
# del método descripcion()
for servicio in servicios:

    print(
        servicio.descripcion()
    )


# =====================================
# DEMOSTRACIÓN DE SOBRECARGA
# =====================================

print("\nPRUEBA DE COSTOS")

print(
    sala.calcular_costo()
)

print(
    sala.calcular_costo(
        horas=2,
        impuesto=0.19
    )
)

print(
    sala.calcular_costo(
        horas=2,
        impuesto=0.19,
        descuento=0.10
    )
)


# =====================================
# MOSTRAR RESERVAS REALIZADAS
# =====================================

print("\nRESERVAS REGISTRADAS")

for reserva in reservas:

    print(
        reserva.cliente.nombre,
        "-",
        reserva.estado
    )


# =====================================
# FIN DEL PROGRAMA
# =====================================

print("\nFIN DEL PROGRAMA")