# Bitácora de Configuración: Laboratorio de Programación
## Ejercicio 1 - Gestión de Entornos y Librerías
### Autor: Brandon Estrada

---

## 1. Introducción
Este documento detalla la resolución de problemas y la configuración exitosa del entorno de desarrollo para el proyecto de Introducción a la Programación.

## 2. Resolución del Conflicto de Ubicación
### 2.1. El error en System32
Se identificó que el entorno virtual inicial fue creado accidentalmente en la ruta crítica del sistema `C:\Windows\System32`. 

### 2.2. Solución y Limpieza
Se procedió a eliminar la carpeta errónea y se reubicó el proyecto en una ruta de usuario segura.

## 3. Configuración del Entorno Virtual (venv)
### 3.1. Creación y Activación
Se generó un nuevo entorno local y se habilitó la ejecución de scripts. Como se observa en la evidencia, el prefijo **(env)** confirma que la terminal está operando correctamente:

![Activación del entorno](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110744.png)

## 4. Gestión de Librerías
### 4.1. Instalación y Funcionamiento de NumPy
Con el entorno activo, se instaló la librería **NumPy**. Se comprobó su funcionamiento en el archivo `mate.py`, donde el IDE reconoce los métodos de la librería.

![Funcionamiento NumPy](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110837.png)

## 5. Configuración del IDE (VS Code)
### 5.1. Selección del Intérprete
Para asegurar que VS Code utilice las librerías del entorno virtual, se seleccionó el intérprete recomendado.

![Selección del Intérprete](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110729.png)

## 6. Estructura Final del Proyecto
La organización del repositorio sigue el estándar de orden requerido:
* **Ejercicio-1/**: Carpeta raíz del ejercicio.
* **Activos/**: Contiene todas las evidencias gráficas.
* **Documento.md**: Documentación técnica.
