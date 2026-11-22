# PET-VOZ - Funciones para revisar los datos
# Se usan funciones, if, for, listas y cadenas.

from datetime import date, timedelta

TIPOS = ["Petición", "Queja", "Reclamo", "Sugerencia"]
DOCUMENTOS = ["CC", "TI", "CE", "PP", "NIT"]
TELEFONOS = ["Celular", "Fijo", "Corporativo", "Otro"]
CANALES = ["Presencial", "Correo electrónico", "Página web",
           "Teléfono", "Redes sociales", "Otro"]
MASCOTAS = ["Perro", "Gato"]
ESTADOS = ["Registrada", "En proceso", "Solucionada"]
CAMPUS = [
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


def validar_nombre(nombre):
    nombre = nombre.strip()
    if len(nombre) < 3 or len(nombre) > 100:
        return False
    for letra in nombre:
        if not (letra.isalpha() or letra in " '-"):
            return False
    return True


def validar_documento(numero):
    return numero.isdigit() and 3 <= len(numero) <= 15


def validar_telefono(numero):
    return numero.isdigit() and len(numero) == 10


def validar_correo(correo):
    if len(correo) == 0 or len(correo) > 254:
        return False
    if correo.count("@") != 1 or " " in correo or ".." in correo:
        return False
    partes = correo.split("@")
    usuario = partes[0]
    dominio = partes[1]
    if usuario == "" or dominio == "":
        return False
    if usuario[0] == "." or usuario[-1] == ".":
        return False
    for letra in usuario:
        if not (letra.isalnum() or letra in "._%+-"):
            return False
    secciones = dominio.split(".")
    if len(secciones) < 2:
        return False
    for parte in secciones:
        if parte == "" or parte[0] == "-" or parte[-1] == "-":
            return False
        for letra in parte:
            if not (letra.isalnum() or letra == "-"):
                return False
    if len(secciones[-1]) < 2:
        return False
    return True


def validar_direccion(direccion):
    direccion = direccion.strip()
    if direccion == "":
        return True
    if len(direccion) < 5 or len(direccion) > 200:
        return False
    for letra in direccion:
        if not (letra.isalnum() or letra in " #-,./"):
            return False
    return True


def validar_asunto(asunto):
    asunto = asunto.strip()
    if len(asunto) < 5 or len(asunto) > 150:
        return False
    for letra in asunto:
        if not (letra.isalnum() or letra in " .,;:¿?¡!()-"):
            return False
    return True


def validar_descripcion(descripcion):
    return 20 <= len(descripcion.strip()) <= 2000


def fecha_valida(fecha):
    # Revisamos el formato antes de convertir a numeros.
    if len(fecha) != 10:
        return False
    if fecha[4] != "-" or fecha[7] != "-":
        return False
    anio = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:]
    if not (anio.isdigit() and mes.isdigit() and dia.isdigit()):
        return False
    anio = int(anio)
    mes = int(mes)
    dia = int(dia)
    if anio < 1 or anio > 9999 or mes < 1 or mes > 12:
        return False
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        dias_mes[1] = 29
    if dia < 1 or dia > dias_mes[mes - 1]:
        return False
    hoy = date.today()
    if (anio, mes, dia) > (hoy.year, hoy.month, hoy.day):
        return False
    return True


def convertir_fecha(fecha):
    if not fecha_valida(fecha):
        return None
    return date(int(fecha[:4]), int(fecha[5:7]), int(fecha[8:]))


def fecha_maxima(fecha):
    inicio = convertir_fecha(fecha)
    if inicio == None:
        return None
    if inicio.toordinal() > date.max.toordinal() - 30:
        return None
    limite = inicio + timedelta(days=30)
    return str(limite)


def cambio_permitido(actual, nuevo):
    if actual == "Registrada" and nuevo == "En proceso":
        return True
    if actual == "En proceso" and nuevo == "Solucionada":
        return True
    return False
