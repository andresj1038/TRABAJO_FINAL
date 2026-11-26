# PET-VOZ - Lectura y escritura de los cuatro TXT

import os
from validaciones import TIPOS, cambio_permitido, fecha_valida

CARPETA_SRC = os.path.dirname(os.path.abspath(__file__))
CARPETA_PROYECTO = os.path.dirname(CARPETA_SRC)
CARPETA_DATOS = os.path.join(CARPETA_PROYECTO, "data")

NOMBRES = {
    "Petición": "Peticion.txt",
    "Queja": "Queja.txt",
    "Reclamo": "Reclamo.txt",
    "Sugerencia": "Sugerencia.txt"
}

CAMPOS = [
    "id", "nombre_completo", "tipo_documento", "numero_documento",
    "tipo_telefono", "telefono_contacto", "correo_electronico",
    "direccion", "tipo_solicitud", "fecha_radicacion",
    "canal_recepcion", "asunto_titulo", "descripcion_detallada",
    "tipo_mascota", "campus_relacionado", "fecha_maxima_respuesta",
    "estado_peticion", "fecha_solucion"
]


def ruta(tipo):
    if tipo not in TIPOS:
        return None
    return os.path.join(CARPETA_DATOS, NOMBRES[tipo])


def preparar_archivos():
    if not os.path.exists(CARPETA_DATOS):
        os.mkdir(CARPETA_DATOS)
    for tipo in TIPOS:
        nombre = ruta(tipo)
        if not os.path.exists(nombre):
            archivo = open(nombre, "w", encoding="utf-8")
            archivo.close()


def convertir_a_texto(registro):
    valores = []
    for campo in CAMPOS:
        valor = str(registro.get(campo, ""))
        valor = valor.replace("\n", " ")
        valor = valor.replace("\r", " ")
        valor = valor.replace("\t", " ")
        valores.append(valor)
    return "\t".join(valores)


def convertir_a_registro(linea):
    valores = linea.rstrip("\n").rstrip("\r").split("\t")
    if len(valores) != len(CAMPOS):
        return None
    if not valores[0].isdigit():
        return None
    registro = {}
    for i in range(len(CAMPOS)):
        registro[CAMPOS[i]] = valores[i]
    return registro


def leer(tipo):
    preparar_archivos()
    nombre = ruta(tipo)
    registros = []
    if nombre == None:
        return registros
    archivo = open(nombre, "r", encoding="utf-8")
    for linea in archivo:
        if linea.strip() != "":
            registro = convertir_a_registro(linea)
            if registro != None:
                registros.append(registro)
    archivo.close()
    return registros


def siguiente_id(tipo):
    mayor = 0
    for registro in leer(tipo):
        numero = int(registro["id"])
        if numero > mayor:
            mayor = numero
    return mayor + 1


def guardar(registro):
    tipo = registro.get("tipo_solicitud", "")
    if tipo not in TIPOS:
        return None
    if registro.get("estado_peticion", "") != "Registrada":
        return None
    numero = siguiente_id(tipo)
    registro["id"] = str(numero)
    registro["fecha_solucion"] = ""
    archivo = open(ruta(tipo), "a", encoding="utf-8")
    archivo.write(convertir_a_texto(registro) + "\n")
    archivo.close()
    return numero


def buscar(tipo, numero):
    for registro in leer(tipo):
        if registro["id"] == str(numero):
            return registro
    return None


def actualizar(tipo, numero, nuevo, fecha_solucion=""):
    registros = leer(tipo)
    encontrado = False
    for registro in registros:
        if registro["id"] == str(numero):
            if not cambio_permitido(registro["estado_peticion"], nuevo):
                return False
            if nuevo == "Solucionada":
                if not fecha_valida(fecha_solucion):
                    return False
                if fecha_solucion < registro["fecha_radicacion"]:
                    return False
                registro["fecha_solucion"] = fecha_solucion
            registro["estado_peticion"] = nuevo
            encontrado = True
            break
    if encontrado:
        archivo = open(ruta(tipo), "w", encoding="utf-8")
        for registro in registros:
            archivo.write(convertir_a_texto(registro) + "\n")
        archivo.close()
    return encontrado


def todos():
    registros = []
    for tipo in TIPOS:
        registros.extend(leer(tipo))
    return registros
