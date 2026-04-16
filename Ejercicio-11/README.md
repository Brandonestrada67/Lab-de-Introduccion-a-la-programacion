#  Escáner Pro (QR y Código de Barras)
## Hecho por Brandon Estrada
### :)

Este proyecto es una aplicación web que permite escanear códigos QR y códigos de barras usando la cámara.

También consulta una API para mostrar información de productos cuando se detecta un código de barras.

---

##  Características
El sistema permite:

- Escanear códigos de barras  
- Escanear códigos QR  
- Detectar links automáticamente  
- Consultar productos con API  
- Mostrar nombre, marca e imagen  
- Uso de cámara en tiempo real  

---

##  Lógica del Programa
El proyecto funciona con dos partes:

- Backend con Flask  
- Frontend con HTML y JavaScript  

---

##  Backend (Flask)

El servidor se encarga de mostrar la página web.

~~~python
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
~~~

---

##  ¿Qué hace este código?

- Se crea una aplicación web con Flask  
- Cuando entras a la ruta /, se carga el archivo index.html  
- El servidor corre en localhost:5000  
- El modo debug=True ayuda a ver errores mientras se desarrolla  

## Librerías que use

Se usan dos librerías principales:

- QuaggaJS → Para escanear códigos de barras  
- html5-qrcode → Para escanear códigos QR  

~~~html
<script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>
<script src="https://unpkg.com/html5-qrcode"></script>
~~~

---

##  Interfaz

La página muestra:

- Un título (Escáner Pro)  
- Dos botones:
  - Escanear código de barras  
  - Escanear QR  
- Un área donde se activa la cámara  
- Un cuadro donde se muestran los resultados  

---

##  Funcionalidades principales

### 1️- Escaneo de códigos de barras

~~~javascript
function iniciarBarras() { ... }
~~~

- Activa la cámara trasera  
- Usa Quagga para detectar códigos  
- Repite la lectura varias veces para asegurar precisión  
- Cuando detecta el mismo código 3 veces, lo valida  

---

### 2️- Escaneo de QR

~~~javascript
function iniciarQR() { ... }
~~~

- Activa la cámara  
- Usa html5-qrcode  
- Detecta el contenido inmediatamente  

---

### 3️- Mostrar resultados

~~~javascript
async function mostrarResultado(codigo) { ... }
~~~

Aquí pasan dos cosas:

 Si es un QR con link:  
- Se muestra el enlace  
- Se puede abrir directamente  

 Si es código de barras:  
- Se consulta la API de OpenFoodFacts  
- Si encuentra el producto:
  - Nombre  
  - Marca  
  - Imagen  
- Si no:
  - Muestra que no se encontró  

---

##  API utilizada

Se usa:

~~~
https://world.openfoodfacts.org/api/v0/product/{codigo}.json
~~~

Esto permite obtener información real de productos a partir del código de barras.

---

##  Control de escaneo

El sistema evita errores con:

- detenerTodo() → Detiene cualquier escaneo activo  
- limpiarPantalla() → Muestra "Escaneando..."  
- Validación de lecturas repetidas  

---

##  ¿Cómo ejecutar el proyecto?

1. Instalar Flask

~~~bash
pip install flask
~~~

2. Ejecutar el servidor

~~~bash
python app.py
~~~

3. Abrir en el navegador

~~~
http://127.0.0.1:5000
~~~

---

##  Notas pa entender mejor

- Se necesita permitir acceso a la cámara  
- Funciona mejor en dispositivos con cámara trasera  
- Requiere conexión a internet para consultar productos  

---

##  Conclusión

Este proyecto demuestra el uso de:

- JavaScript  
- Flask  
- Consumo de APIs  
- Uso de cámara  
- Eventos y funciones  
