# PET-VOZ - Comprobantes y estadisticas

import os
from datetime import date
from validaciones import TIPOS, MASCOTAS, ESTADOS, convertir_fecha

CARPETA_SRC = os.path.dirname(os.path.abspath(_file_))
CARPETA_PROYECTO = os.path.dirname(CARPETA_SRC)
CARPETA_COMPROBANTES = os.path.join(CARPETA_PROYECTO, "data", "comprobantes")
ANCHO = 120


def linea_marco():
    return "+" + "-" * (ANCHO - 2) + "+"


def linea_texto(texto):
    return "| " + texto.ljust(ANCHO - 4) + " |"


def agregar_campo(lineas, titulo, valor):
    texto = titulo + ": " + str(valor)
    # Si el campo es largo, lo repartimos en varias lineas.
    while len(texto) > ANCHO - 4:
        lineas.append(linea_texto(texto[:ANCHO - 4]))
        texto = texto[ANCHO - 4:]
    lineas.append(linea_texto(texto))


def hacer_comprobante(registro):
    lineas = [linea_marco()]
    lineas.append(linea_texto("PET-VOZ - COMPROBANTE DE RADICADO".center(ANCHO - 4)))
    lineas.append(linea_texto("GESTOR DE PQRS - UNIVERSIDAD DE ANTIOQUIA".center(ANCHO - 4)))
    lineas.append(linea_marco())
    agregar_campo(lineas, "Radicado", registro["tipo_solicitud"] + " #" + registro["id"])
    agregar_campo(lineas, "Fecha de radicacion", registro["fecha_radicacion"])
    agregar_campo(lineas, "Estado", registro["estado_peticion"])
    agregar_campo(lineas, "Fecha maxima de respuesta", registro["fecha_maxima_respuesta"])
    agregar_campo(lineas, "Nombre", registro["nombre_completo"])
    agregar_campo(lineas, "Documento", registro["tipo_documento"] + " " + registro["numero_documento"])
    agregar_campo(lineas, "Telefono", registro["tipo_telefono"] + " " + registro["telefono_contacto"])
    agregar_campo(lineas, "Correo", registro["correo_electronico"])
    direccion = registro["direccion"]
    if direccion == "":
        direccion = "N/A"
    agregar_campo(lineas, "Direccion", direccion)
    agregar_campo(lineas, "Solicitud", registro["tipo_solicitud"])
    agregar_campo(lineas, "Canal", registro["canal_recepcion"])
    agregar_campo(lineas, "Mascota", registro["tipo_mascota"])
    agregar_campo(lineas, "Campus", registro["campus_relacionado"])
    agregar_campo(lineas, "Asunto", registro["asunto_titulo"])
    # La descripcion detallada no se incluye, segun las instrucciones.
    lineas.append(linea_marco())
    return "\n".join(lineas) + "\n"


def imprimir_radicado(registro):
    if not os.path.exists(CARPETA_COMPROBANTES):
        os.mkdir(CARPETA_COMPROBANTES)
    tipo = registro["tipo_solicitud"].replace("ó", "o")
    nombre = tipo + "_" + registro["id"] + ".txt"
    destino = os.path.join(CARPETA_COMPROBANTES, nombre)
    archivo = open(destino, "w", encoding="utf-8")
    archivo.write(hacer_comprobante(registro))
    archivo.close()
    return destino


def estadisticas(registros):
    print("\n========== ESTADISTICAS PET-VOZ ==========")
    print("Total de solicitudes:", len(registros))

    # 1. Promedio de dias de respuesta (obligatoria)
    suma_dias = 0
    solucionadas = 0
    for registro in registros:
        if registro["estado_peticion"] == "Solucionada":
            inicio = convertir_fecha(registro["fecha_radicacion"])
            fin = convertir_fecha(registro["fecha_solucion"])
            if inicio != None and fin != None and fin >= inicio:
                suma_dias = suma_dias + (fin - inicio).days
                solucionadas = solucionadas + 1
    if solucionadas > 0:
        promedio = round(suma_dias / solucionadas)
        print("1. Promedio de dias de respuesta:", promedio)
    else:
        print("1. Promedio de dias de respuesta: sin datos")

    # 2. Cantidad por tipo
    print("2. Cantidad por tipo de PQRS:")
    for tipo in TIPOS:
        cantidad = 0
        for registro in registros:
            if registro["tipo_solicitud"] == tipo:
                cantidad = cantidad + 1
        print("  ", tipo, ":", cantidad)

    # 3. Cantidad por mascota
    print("3. Cantidad por mascota:")
    for mascota in MASCOTAS:
        cantidad = 0
        for registro in registros:
            if registro["tipo_mascota"] == mascota:
                cantidad = cantidad + 1
        print("  ", mascota, ":", cantidad)

    # 4. Cantidad por estado
    print("4. Cantidad por estado:")
    for estado in ESTADOS:
        cantidad = 0
        for registro in registros:
            if registro["estado_peticion"] == estado:
                cantidad = cantidad + 1
        print("  ", estado, ":", cantidad)

    # 5 y 6. Vencidas y proximas a vencer
    vencidas = 0
    proximas = 0
    hoy = date.today()
    for registro in registros:
        if registro["estado_peticion"] != "Solucionada":
            limite = convertir_fecha(registro["fecha_maxima_respuesta"])
            if limite != None:
                dias = (limite - hoy).days
                if dias < 0:
                    vencidas = vencidas + 1
                elif dias <= 5:
                    proximas = proximas + 1
    print("5. PQRS activas vencidas:", vencidas)
    print("6. PQRS activas que vencen en 0 a 5 dias:", proximas)
