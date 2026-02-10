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
Se procedió a eliminar la carpeta errónea y se reubicó el proyecto en una ruta de usuario segura: `C:\Users\brand\LABORATORIO INTRODUCCION A LA PROGRAMACION`.

---

## 3. Configuración del Entorno Virtual (venv)
### 3.1. Creación y Activación
Se generó un nuevo entorno local y se habilitó la ejecución de scripts en PowerShell. El prefijo **(env)** confirma que la terminal está operando correctamente:

![Activación del entorno](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110744.png)

## 4. Gestión de Librerías
### 4.1. Instalación y Funcionamiento de NumPy
Se instaló la librería **NumPy** y se comprobó su funcionamiento en el archivo `mate.py`.

![Funcionamiento NumPy](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110837.png)

## 5. Configuración del IDE (VS Code)
### 5.1. Selección del Intérprete
Se seleccionó el intérprete recomendado para vincular el entorno virtual con VS Code.

![Selección del Intérprete](https://raw.githubusercontent.com/Brandonestrada67/Lab-de-Introduccion-a-la-programacion/main/Ejercicio-1/Assets/Captura%20de%20pantalla%202026-02-05%20110729.png)

---

## 6. Secuencia Cronológica de Comandos (Copy & Paste)

| Orden | Acción | Comando con Botón de Copiado |
| :--- | :--- | :--- |
| 1 | **Permisos de Sistema** | ```powershell Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine ``` |
| 2 | **Crear Entorno** | ```powershell python -m venv env ``` |
| 3 | **Activar Entorno** | ```powershell .\env\Scripts\Activate.ps1 ``` |
| 4 | **Instalar Librería** | ```powershell pip install numpy ``` |
| 5 | **Validar Instalación** | ```powershell python -c "import numpy; print(numpy.__version__)" ``` |
| 6 | **Generar Requisitos** | ```powershell pip freeze > requirements.txt ``` |

---

## 7. Conclusión
La correcta gestión de entornos virtuales permite mantener un flujo de trabajo limpio y profesional, asegurando que las librerías del proyecto estén organizadas y el sistema operativo permanezca íntegro. limpio y profesional, asegurando que las librerías del proyecto estén organizadas y el sistema operativo permanezca íntegro.
