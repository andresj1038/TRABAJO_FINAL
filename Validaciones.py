# ==========================================
# PET-VOZ
# VALIDACIONES DEL SISTEMA
# ==========================================

from datetime import datetime, timedelta


# DATOS DEL SOLICITANTE

def validar_nombre(nombre):
    nombre = nombre.strip()

    if len(nombre) < 3 or len(nombre) > 100:
        return False

    for letra in nombre:
        if not (letra.isalpha() or letra in " '-"):
            return False

    return True


def validar_tipo_documento(tipo):
    tipos = ["CC", "TI", "CE", "PP", "NIT"]
    return tipo in tipos


def validar_numero_documento(numero):
    return numero.isdigit() and 3 <= len(numero) <= 15


def validar_tipo_telefono(tipo):
    tipos = ["Celular", "Fijo", "Corporativo", "Otro"]
    return tipo in tipos


def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10


def validar_correo(correo):
    correo = correo.strip()

    if len(correo) == 0 or len(correo) > 254:
        return False

    if correo.count("@") != 1 or " " in correo:
        return False

    partes = correo.split("@")
    usuario = partes[0]
    dominio = partes[1]

    if usuario == "" or dominio == "":
        return False

    if usuario[0] == "." or usuario[-1] == ".":
        return False

    if ".." in correo:
        return False

    if "." not in dominio:
        return False

    secciones = dominio.split(".")

    for seccion in secciones:
        if seccion == "":
            return False

    return True


def validar_direccion(direccion):
    direccion = direccion.strip()

    if direccion == "":
        return True

    return 5 <= len(direccion) <= 200


# DATOS DE LA PQRS

def validar_tipo_solicitud(tipo):
    tipos = ["Petición", "Queja", "Reclamo", "Sugerencia"]
    return tipo in tipos


def validar_canal(canal):
    canales = [
        "Presencial",
        "Correo electrónico",
        "Página web",
        "Teléfono",
        "Redes sociales",
        "Otro"
    ]

    return canal in canales


def validar_asunto(asunto):
    asunto = asunto.strip()

    if len(asunto) < 5 or len(asunto) > 150:
        return False

    permitidos = " .,;:¿?¡!()-"

    for caracter in asunto:
        if not (caracter.isalnum() or caracter in permitidos):
            return False

    return True


def validar_descripcion(descripcion):
    descripcion = descripcion.strip()
    return 20 <= len(descripcion) <= 2000


def validar_mascota(mascota):
    mascotas = ["Perro", "Gato"]
    return mascota in mascotas


def validar_campus(campus):
    campus_permitidos = [
        "Campus Medellín - Ciudad Universitaria",
        "Campus Medellín - Ciudadela Robledo",
        "Campus en el Área de la salud",
        "Campus Medellín - Sede de Posgrado",
        "Campus Medellín - Edificio San Ignacio",
        "Campus Medellín - Antigua Escuela de Derecho",
        "Campus Medellín - Edificio Antioquia",
        "Campus Medellín - Casas Patrimoniales",
        "Campus Medellín - Edificio de Extensión"
    ]

    return campus in campus_permitidos


# FECHAS

def validar_fecha(fecha):
    if len(fecha) != 10:
        return False

    if fecha[4] != "-" or fecha[7] != "-":
        return False

    anio = fecha[0:4]
    mes = fecha[5:7]
    dia = fecha[8:10]

    if not (anio.isdigit() and mes.isdigit() and dia.isdigit()):
        return False

    anio = int(anio)
    mes = int(mes)
    dia = int(dia)

    if anio < 1 or anio > 9998:
        return False

    if mes < 1 or mes > 12:
        return False

    dias_mes = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if anio % 4 == 0 and (
        anio % 100 != 0 or anio % 400 == 0
    ):
        dias_mes[1] = 29

    if dia < 1 or dia > dias_mes[mes - 1]:
        return False

    fecha_actual = datetime.now().date()

    if (anio, mes, dia) > (
        fecha_actual.year,
        fecha_actual.month,
        fecha_actual.day
    ):
        return False

    return True


def calcular_fecha_maxima(fecha):
    if not validar_fecha(fecha):
        return None

    partes = fecha.split("-")

    anio = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])

    fecha_registro = datetime(anio, mes, dia)
    fecha_maxima = fecha_registro + timedelta(days=30)

    return fecha_maxima.strftime("%Y-%m-%d")


# ESTADOS DE LAS PQRS

def validar_estado(estado):
    estados = [
        "Registrada",
        "En proceso",
        "Solucionada"
    ]

    return estado in estados


def validar_cambio_estado(actual, nuevo):
    if actual == "Registrada" and nuevo == "En proceso":
        return True

    if actual == "En proceso" and nuevo == "Solucionada":
        return True

    return False
