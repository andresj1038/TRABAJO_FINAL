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

El desarrollo de **Pet-Voz** se realizará de manera progresiva, dividiendo el proyecto en etapas que permitan organizar el trabajo del equipo, verificar el cumplimiento de los requisitos y realizar pruebas antes de la entrega final.

El proyecto se desarrollará como una aplicación de consola en **Python**, utilizando archivos planos para el almacenamiento de la información y separando las principales funcionalidades en módulos independientes.

### 7.1 Actividades del proyecto

| N.º | Actividad | Descripción | Responsable(s) | Entregable |
|---|---|---|---|---|
| 1 | Análisis de requisitos | Revisar los requerimientos del proyecto, identificar las funcionalidades principales y definir las restricciones del sistema. | Todo el equipo | Lista definitiva de requisitos |
| 2 | Diseño general del sistema | Definir la estructura del programa, el menú principal, los módulos y la forma en que se almacenará la información. | Anderson y Juan José | Diseño general y estructura del programa |
| 3 | Diseño de la interfaz de consola | Diseñar la presentación del menú, mensajes, opciones, confirmaciones y formato visual de los radicados. | Sofía | Propuesta de interfaz de consola |
| 4 | Desarrollo de validaciones | Implementar las funciones necesarias para validar nombres, documentos, teléfonos, correos, fechas y demás datos ingresados. | Anderson y Juan José | `validaciones.py` |
| 5 | Gestión de archivos | Implementar la creación, lectura, escritura y actualización de los archivos `Peticion.txt`, `Queja.txt`, `Reclamo.txt` y `Sugerencia.txt`. | Anderson y Juan José | `archivos.py` |
| 6 | Registro de PQRS | Implementar el formulario de registro de nuevas Peticiones, Quejas, Reclamos y Sugerencias. | Anderson y Juan José | Módulo funcional de registro |
| 7 | Generación de radicados | Implementar la generación automática de un ID consecutivo independiente para cada tipo de PQRS y crear el comprobante TXT con marco ASCII de 120 caracteres. | Anderson y Juan José | Sistema de radicación |
| 8 | Consulta de PQRS | Implementar las funciones necesarias para consultar los registros almacenados y visualizar su información y estado. | Anderson y Juan José | Módulo de consultas |
| 9 | Actualización de estados | Permitir modificar el estado de una PQRS siguiendo el flujo `Registrada → En proceso → Solucionada`. | Anderson y Juan José | Módulo de actualización |
| 10 | Control de fechas | Calcular automáticamente la fecha máxima de respuesta de cada PQRS y detectar registros próximos a cumplir los 30 días calendario. | Anderson y Juan José | Sistema de control de fechas |
| 11 | Desarrollo de estadísticas | Implementar el promedio de días de respuesta y las cinco estadísticas adicionales seleccionadas por el equipo. | Anderson y Juan José | `reportes.py` |
| 12 | Pruebas y depuración | Realizar pruebas sobre todas las funciones, identificar errores, verificar validaciones y comprobar el funcionamiento de los archivos. | Todo el equipo | Versión corregida del programa |
| 13 | Documentación | Consolidar la descripción del proyecto, requisitos, funcionamiento, instrucciones de uso y demás información requerida. | Andrés y Sofía | Documentación final |
| 14 | Preparación de presentación | Elaborar las diapositivas y organizar la explicación del proyecto y la demostración del programa. | Dana y Sofía, con apoyo del equipo | Presentación final |
| 15 | Revisión y entrega final | Verificar que el repositorio, código, documentación y presentación cumplan con todos los requisitos antes de realizar la entrega. | Todo el equipo | Versión final de Pet-Voz |

---

### 7.2 Cronograma de trabajo

El cronograma se organiza por etapas de desarrollo. Algunas actividades podrán realizarse simultáneamente para distribuir mejor el trabajo entre los integrantes.

| Etapa | Actividades principales | Resultado esperado |
|---|---|---|
| **Etapa 1 — Planeación** | Análisis de requisitos, distribución de responsabilidades y definición de la estructura del sistema. | Alcance y organización del proyecto definidos |
| **Etapa 2 — Diseño** | Diseño de arquitectura, menú de consola, estructura de archivos y formato de los radicados. | Diseño general de Pet-Voz |
| **Etapa 3 — Desarrollo base** | Programación de validaciones, manejo de archivos y registro de PQRS. | Sistema capaz de registrar y almacenar información |
| **Etapa 4 — Desarrollo funcional** | Consulta de registros, actualización de estados, generación de radicados y control de fechas. | Funcionalidades principales terminadas |
| **Etapa 5 — Reportes** | Desarrollo del cálculo de estadísticas y generación de información para análisis. | Módulo de estadísticas funcional |
| **Etapa 6 — Pruebas** | Pruebas de funcionamiento, validaciones, archivos, casos incorrectos y corrección de errores. | Programa estable y corregido |
| **Etapa 7 — Documentación** | Consolidación del informe, README, instrucciones de ejecución y preparación de presentación. | Documentación completa |
| **Etapa 8 — Entrega** | Revisión conjunta del repositorio, ejecución final del programa y preparación de la exposición. | Versión final de Pet-Voz |

---

### 7.3 Distribución de responsabilidades

Para garantizar una participación organizada, cada integrante tendrá una responsabilidad principal, sin impedir que pueda apoyar otras actividades del proyecto.

- **Andres Julian Giraldo Garcia — Líder de Proyecto:** coordinará el avance general, verificará el cumplimiento del cronograma, apoyará la investigación y realizará la revisión bibliográfica y el marco teórico.
- **Anderson Leonardo Betancur Morales — Programador:** estará encargado principalmente de la arquitectura del software, lógica general, manejo de datos y desarrollo de las funcionalidades principales.
- **Juan Jose Rios Ramirez — Programador:** apoyará el desarrollo de módulos, integración de funcionalidades, realización de pruebas, depuración y corrección de errores.
- **Dana Zapata Rodriguez — Comunicadora:** apoyará la preparación de la presentación, organización de la exposición y comunicación de los resultados del proyecto.
- **Sofia Martinez Salgado — Diseñadora de Interfaz:** diseñará la interfaz de consola y apoyará la consolidación, organización y presentación de la documentación final.

Aunque existen responsabilidades principales, las decisiones importantes y la revisión final serán realizadas por todo el equipo.

---

### 7.4 Organización del código

Para facilitar el desarrollo y mantenimiento, el programa se dividirá inicialmente en los siguientes archivos:

| Archivo | Función principal |
|---|---|
| `main.py` | Ejecutar el programa y controlar el menú principal |
| `validaciones.py` | Validar los datos ingresados por el usuario |
| `archivos.py` | Gestionar lectura, escritura y actualización de archivos TXT |
| `reportes.py` | Calcular y presentar las estadísticas del sistema |

Los archivos de información generados por el programa serán:

- `Peticion.txt`
- `Queja.txt`
- `Reclamo.txt`
- `Sugerencia.txt`

Adicionalmente, el sistema generará los archivos TXT correspondientes a los comprobantes de radicación.

---

### 7.5 Estrategia de pruebas

Antes de la entrega final se realizarán pruebas para verificar el correcto funcionamiento del sistema.

Se comprobarán principalmente los siguientes aspectos:

1. Registro correcto de cada uno de los cuatro tipos de PQRS.
2. Rechazo de datos inválidos o incompletos.
3. Generación correcta y consecutiva de los números de radicado.
4. Almacenamiento de cada PQRS en el archivo correspondiente.
5. Consulta correcta de los registros almacenados.
6. Actualización válida de los estados.
7. Cálculo correcto de la fecha máxima de respuesta.
8. Identificación de solicitudes próximas a vencer.
9. Generación correcta de los radicados en formato TXT.
10. Cálculo correcto de las estadísticas.
11. Conservación de la información después de cerrar y volver a ejecutar el programa.
12. Manejo adecuado de archivos vacíos o inexistentes.

Cuando se identifique un error durante las pruebas, este será corregido y la funcionalidad será probada nuevamente antes de integrarla a la versión final.

---

### 7.6 Control de versiones

El código fuente y la documentación del proyecto serán administrados mediante **GitHub**.

Cada integrante deberá trabajar sobre las tareas que le correspondan y registrar los cambios realizados mediante commits descriptivos. Antes de considerar una funcionalidad como terminada, se verificará que no genere errores en las demás partes del programa.

El repositorio servirá como punto central para almacenar el código, mantener el historial de cambios y consolidar la versión final de **Pet-Voz**.

---

### 7.7 Criterios de finalización

El proyecto se considerará terminado cuando:

- Las cuatro categorías de PQRS puedan registrarse correctamente.
- Los datos sean almacenados y recuperados desde los archivos planos correspondientes.
- Los radicados sean únicos, consecutivos e independientes para cada tipo de PQRS.
- El sistema permita consultar y actualizar los registros.
- Se calcule correctamente la fecha máxima de respuesta.
- El sistema genere las estadísticas solicitadas.
- Las entradas del usuario sean correctamente validadas.
- El programa pueda cerrarse y ejecutarse nuevamente sin perder la información almacenada.
- El código se encuentre organizado y modularizado.
- Se hayan realizado y superado las pruebas establecidas.
- El repositorio y la documentación estén completos.
- El equipo cuente con una versión estable para realizar la presentación y demostración final.

