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
### Actividades y cronograma 

