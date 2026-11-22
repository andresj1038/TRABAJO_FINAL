# PET-VOZ - Menu principal
# Proyecto de Algoritmia y Programacion

from validaciones import (
    TIPOS, DOCUMENTOS, TELEFONOS, CANALES, MASCOTAS, CAMPUS,
    validar_nombre, validar_documento, validar_telefono,
    validar_correo, validar_direccion, validar_asunto,
    validar_descripcion, fecha_valida, fecha_maxima
)
from archivos import preparar_archivos, guardar, buscar, actualizar, todos
from reportes import imprimir_radicado, estadisticas


def pedir_dato(mensaje, funcion):
    while True:
        dato = input(mensaje).strip()
        if funcion(dato):
            return dato
        print("Dato incorrecto. Intente nuevamente.")


def elegir(titulo, opciones):
    while True:
        print("\n" + titulo)
        for i in range(len(opciones)):
            print(str(i + 1) + ". " + opciones[i])
        numero = input("Elija un numero: ").strip()
        if numero.isdigit():
            numero = int(numero)
            if numero >= 1 and numero <= len(opciones):
                return opciones[numero - 1]
        print("Opcion no valida.")


def pedir_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        if fecha_valida(fecha):
            return fecha
        print("Fecha no valida. Use AAAA-MM-DD y no una fecha futura.")


def pedir_numero():
    while True:
        numero = input("Numero de radicado: ").strip()
        if numero.isdigit() and int(numero) > 0:
            return numero
        print("Escriba un numero positivo.")


def registrar():
    print("\n--- REGISTRAR PQRS ---")
    tipo = elegir("Tipo de solicitud:", TIPOS)
    nombre = pedir_dato("Nombre completo: ", validar_nombre)
    tipo_documento = elegir("Tipo de documento:", DOCUMENTOS)
    numero_documento = pedir_dato("Numero de documento: ", validar_documento)
    tipo_telefono = elegir("Tipo de telefono:", TELEFONOS)
    telefono = pedir_dato("Telefono (10 digitos): ", validar_telefono)
    correo = pedir_dato("Correo electronico: ", validar_correo)
    direccion = pedir_dato("Direccion (Enter si no tiene): ", validar_direccion)
    fecha = pedir_fecha("Fecha de radicacion (AAAA-MM-DD): ")
    limite = fecha_maxima(fecha)
    if limite == None:
        print("No es posible calcular la fecha maxima.")
        return
    canal = elegir("Canal de recepcion:", CANALES)
    asunto = pedir_dato("Asunto o titulo: ", validar_asunto)
    descripcion = pedir_dato("Descripcion (20 a 2000 caracteres): ", validar_descripcion)
    mascota = elegir("Tipo de mascota:", MASCOTAS)
    campus = elegir("Campus relacionado:", CAMPUS)

    registro = {
        "nombre_completo": nombre,
        "tipo_documento": tipo_documento,
        "numero_documento": numero_documento,
        "tipo_telefono": tipo_telefono,
        "telefono_contacto": telefono,
        "correo_electronico": correo,
        "direccion": direccion,
        "tipo_solicitud": tipo,
        "fecha_radicacion": fecha,
        "canal_recepcion": canal,
        "asunto_titulo": asunto,
        "descripcion_detallada": descripcion,
        "tipo_mascota": mascota,
        "campus_relacionado": campus,
        "fecha_maxima_respuesta": limite,
        "estado_peticion": "Registrada",
        "fecha_solucion": ""
    }
    numero = guardar(registro)
    if numero == None:
        print("No se pudo guardar la solicitud.")
        return
    print("\nSolicitud registrada:", tipo, "#", numero)
    print("Comprobante TXT:", imprimir_radicado(registro))


def consultar():
    print("\n--- CONSULTAR PQRS ---")
    tipo = elegir("Tipo de solicitud:", TIPOS)
    numero = pedir_numero()
    registro = buscar(tipo, numero)
    if registro == None:
        print("No se encontro esa solicitud.")
        return
    print("\nRadicado:", registro["id"])
    print("Solicitante:", registro["nombre_completo"])
    print("Asunto:", registro["asunto_titulo"])
    print("Estado:", registro["estado_peticion"])
    print("Fecha maxima:", registro["fecha_maxima_respuesta"])
    print("Comprobante TXT:", imprimir_radicado(registro))


def cambiar_estado():
    print("\n--- CAMBIAR ESTADO ---")
    tipo = elegir("Tipo de solicitud:", TIPOS)
    numero = pedir_numero()
    registro = buscar(tipo, numero)
    if registro == None:
        print("No se encontro esa solicitud.")
        return
    actual = registro["estado_peticion"]
    print("Estado actual:", actual)
    if actual == "Solucionada":
        print("Esta solicitud ya esta solucionada.")
        return
    if actual == "Registrada":
        nuevo = "En proceso"
    else:
        nuevo = "Solucionada"
    print("Siguiente estado permitido:", nuevo)
    confirmar = input("Confirmar cambio (S/N): ").strip().upper()
    if confirmar != "S":
        print("Cambio cancelado.")
        return
    fecha_solucion = ""
    if nuevo == "Solucionada":
        while True:
            fecha_solucion = pedir_fecha("Fecha de solucion (AAAA-MM-DD): ")
            if fecha_solucion >= registro["fecha_radicacion"]:
                break
            print("No puede ser anterior a la radicacion.")
    if actualizar(tipo, numero, nuevo, fecha_solucion):
        print("Estado actualizado.")
        registro = buscar(tipo, numero)
        print("Comprobante TXT:", imprimir_radicado(registro))
    else:
        print("No fue posible actualizar.")


def menu():
    preparar_archivos()
    opcion = ""
    while opcion != "5":
        print("\n==========================================")
        print("          PET-VOZ - GESTOR DE PQRS")
        print("==========================================")
        print("1. Registrar PQRS")
        print("2. Consultar PQRS")
        print("3. Registrar cambio en PQRS")
        print("4. Estadisticas")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrar()
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            cambiar_estado()
        elif opcion == "4":
            estadisticas(todos())
        elif opcion == "5":
            print("Gracias por utilizar Pet-Voz.")
        else:
            print("Opcion incorrecta.")


menu()
