# Pet-Voz 🐾

**Sistema de Gestión de PQRS para la atención de Perros y Gatos**
![Logo Pet-Voz](images/logo-pet-voz.svg)
> Proyecto Integrador — Algoritmia y Programación 2026-2
> Facultad de Ingeniería — Departamento de Ingeniería Industrial
> Universidad de Antioquia
 
---
 
## 1. Integrantes
 
| Nombre completo | Rol en el equipo |
|---|---|
| Andres Julian Giraldo Garcia | Líder de Proyecto |
| Anderson Leonardo Betancur Morales | Programador |
| Juan Jose Rios Ramirez | Programador |
| Dana Zapata Rodriguez | Comunicadora |
| Sofia Martinez Salgado | Diseñadora de Interfaz |
 
Somos un equipo de estudiantes del curso **Algoritmia y Programación**, encargado de diseñar y desarrollar un sistema de consola en Python para la gestión de Peticiones, Quejas, Reclamos y Sugerencias (PQRS) del Movimiento Estudiantil de Perritos y Gaticos (antes MEPEGA), ahora bajo el nombre **Pet-Voz**.
 
---
 
## 2. Vínculos académicos y descripción
 
Todos los integrantes pertenecen al programa de **Ingeniería Industrial** de la Universidad de Antioquia.
 
| Integrante | Habilidades / Fortalezas | Responsabilidad principal |
|---|---|---|
| **Andres Julian Giraldo Garcia** | Liderazgo, organización de equipos, investigación | Líder de proyecto: revisión bibliográfica y redacción del marco teórico |
| **Anderson Leonardo Betancur Morales** | Lógica de programación, diseño de arquitectura de software | Definición de la arquitectura del software, desarrollo del código base y la lógica del programa |
| **Juan Jose Rios Ramirez** | Programación, depuración y pruebas de software | Desarrollo de módulos, realización de pruebas, optimización y corrección de errores |
| **Dana Zapata Rodriguez** | Comunicación, trabajo en equipo, presentaciones | Apoyo en la elaboración de la presentación/diapositivas y comunicación del equipo |
| **Sofia Martinez Salgado** | Diseño de interfaces, redacción y estructura de documentos | Diseño de interfaz de consola, consolidación del informe, formato PDF y presentación final |
 
---
 
## 3. Nombre del proyecto y detalles
 
### Pet-Voz
 
El nombre **Pet-Voz** nace de la idea de "Pet" de mascotas y "voz" de darle la comunicacion a las peticiones, quejas, reclamos y sugerencias relacionadas con el bienestar de las mascotas (perros y gatos) atendidas en la Universidad. El sistema busca ser el canal ordenado y confiable a través del cual la comunidad estudiantil puede expresar sus solicitudes ante el equipo encargado de la atención animal. reemplazando el proceso manual (papel y lapiz) por un sistema digital organizado.

 ![Logo Pet-Voz](images/logo-pet-voz.svg)

 ## 4. Licencia del software
  <a href="https://github.com/andresj1038/TRABAJO_FINAL/blob/main/README.md">Pet-voz</a> © 2026 by <a href="https://github.com/andersonbetancur1-collab">Andres Julian Giraldo Garcia,Anderson Leonardo Betancur Morales,Juan Jose Rios Ramirez,Dana Zapata Rodriguez,Sofia Martinez Salgado</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">

## 5. Reporte de visión 
### Descripción general
Pet-Voz busca digitalizar y organizar el proceso de recepción y gestión de PQRS relacionadas con la atención de perros y gatos en la Universidad de Antioquia, reemplazando el registro manual en papel por un sistema de consola desarrollado en Python.
 
### Objetivo
Crear un programa de consola amigable que permita al administrador de Pet-Voz gestionar el ingreso, consulta, actualización y análisis estadístico de documentos PQRS, almacenando y exportando la información mediante archivos planos.
 
### Beneficios
- Elimina la pérdida o duplicidad de registros al reemplazar el papel por archivos digitales.
- Genera automáticamente un número de radicado consecutivo y único por tipo de solicitud.
- Permite calcular estadísticas clave (tiempos de respuesta, volumen de solicitudes, etc.) para la toma de decisiones.
- Facilita el seguimiento del estado de cada PQRS (Registrada → En proceso → Solucionada) y alerta sobre las que están próximas a vencer (30 días calendario).
- Mejora la trazabilidad y transparencia del proceso frente a la comunidad estudiantil.

## 6. Especificaciones de requisitos
### Requisitos funcionales:
- El sistema debe permitir **registrar** una nueva PQRS validando todos los datos del solicitante (nombre, tipo y número de documento, teléfono, correo, dirección) y de la solicitud (tipo, fecha, canal de recepción, asunto, descripción).
- El sistema debe asignar un **ID de registro auto-incremental e independiente** para cada uno de los cuatro tipos de documento (Petición, Queja, Reclamo, Sugerencia).
- El sistema debe **almacenar** los registros en cuatro archivos planos independientes (`Peticion.txt`, `Queja.txt`, `Reclamo.txt`, `Sugerencia.txt`).
- El sistema debe permitir **consultar** los registros activos y su estado general.
- El sistema debe permitir **actualizar el estado** de una PQRS siguiendo el flujo: Registrada → En proceso → Solucionada.
- El sistema debe **generar e imprimir un radicado** en formato TXT (ancho fijo de 120 caracteres, delimitado con marco ASCII) como comprobante de cada registro.
- El sistema debe **calcular la fecha máxima de respuesta** (fecha de registro + 30 días).
- El sistema debe **generar estadísticas**, incluyendo obligatoriamente el promedio de días de respuesta, más cinco estadísticas adicionales definidas por el equipo.

### Requisitos no funcionales 
- **Usabilidad:** el menú de consola debe ser claro, amigable e intuitivo para el administrador.
- **Rendimiento:** las operaciones de lectura/escritura sobre los archivos planos deben ejecutarse sin demoras perceptibles para el usuario.
- **Fiabilidad:** el sistema debe validar rigurosamente cada dato ingresado para evitar información inconsistente o corrupta en los archivos.
- **Mantenibilidad:** el código debe estar modularizado en archivos independientes (`validaciones.py`, `archivos.py`, `reportes.py`) para facilitar su mantenimiento.
- **Compatibilidad:** el sistema debe ejecutarse en cualquier entorno con Python instalado, sin dependencias externas complejas.

---
## 7. Plan de proyecto: 


Para desarrollar **Pet-Voz**, dividiremos el trabajo en diferentes etapas. La idea es avanzar primero con la estructura básica del programa y después ir agregando las funcionalidades hasta tener una versión completa que podamos probar y corregir antes de la entrega.

### Actividades y cronograma

| Etapa | Actividad | Responsable(s) |
|---|---|---|
| 1 | Revisar los requisitos y definir cómo funcionará el programa. | Todo el equipo |
| 2 | Diseñar el menú de consola y organizar la estructura del código. | Anderson, Juan José y Sofía |
| 3 | Crear las validaciones para los datos ingresados por el usuario. | Anderson y Juan José |
| 4 | Programar el registro y almacenamiento de las PQRS en los archivos TXT. | Anderson y Juan José |
| 5 | Implementar la generación automática de los radicados. | Anderson y Juan José |
| 6 | Programar la consulta de las PQRS y la actualización de sus estados. | Anderson y Juan José |
| 7 | Implementar el cálculo de fechas de respuesta y las estadísticas. | Anderson y Juan José |
| 8 | Probar el programa, encontrar errores y realizar las correcciones necesarias. | Todo el equipo |
| 9 | Organizar el informe, README y demás documentación del proyecto. | Andrés y Sofía |
| 10 | Preparar las diapositivas, la exposición y la demostración del programa. | Dana y Sofía, con apoyo del equipo |
| 11 | Hacer una revisión final y preparar la entrega. | Todo el equipo |

### Organización del programa

Para mantener el código ordenado y facilitar el trabajo en equipo, inicialmente se utilizará la siguiente estructura:

- `main.py`: menú principal y ejecución del programa.
- `validaciones.py`: validación de los datos ingresados.
- `archivos.py`: lectura, escritura y actualización de los archivos.
- `reportes.py`: cálculo y presentación de estadísticas.

Los registros se almacenarán en cuatro archivos independientes:

- `Peticion.txt`
- `Queja.txt`
- `Reclamo.txt`
- `Sugerencia.txt`

### Pruebas

A medida que avancemos, iremos probando cada parte del programa. Antes de la entrega final verificaremos principalmente que:

- Los cuatro tipos de PQRS se puedan registrar correctamente.
- Los datos ingresados sean validados.
- Cada tipo de PQRS tenga su propio consecutivo.
- Los registros se guarden en el archivo correspondiente.
- Se puedan consultar y actualizar las solicitudes.
- Las fechas máximas de respuesta se calculen correctamente.
- Los radicados se generen con el formato solicitado.
- Las estadísticas funcionen correctamente.
- La información no se pierda al cerrar y volver a ejecutar el programa.

### Trabajo en equipo

El proyecto se manejará mediante **GitHub**, donde iremos guardando los avances del código y la documentación.

Aunque cada integrante tiene una responsabilidad principal, todos participaremos en la revisión y las pruebas del proyecto. De esta manera podremos detectar errores, aportar mejoras y asegurarnos de que **Pet-Voz** cumpla con los requisitos establecidos antes de realizar la entrega final.
