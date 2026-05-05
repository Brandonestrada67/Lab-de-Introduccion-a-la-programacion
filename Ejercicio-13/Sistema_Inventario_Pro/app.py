from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/guardar', methods=['POST'])
def guardar_producto():
    datos = request.json
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO productos (id_proveedor, nombre_producto, codigo_qr, cantidad)
            VALUES (?, ?, ?, ?)
        ''', (datos['id_proveedor'], datos['nombre_producto'], datos['codigo_qr'], datos['cantidad']))
        
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "mensaje": "Producto guardado con éxito 📦"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"status": "error", "mensaje": "Este código QR ya fue registrado."}), 400
    except Exception as e:
        return jsonify({"status": "error", "mensaje": str(e)}), 500

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM productos ORDER BY fecha_captura DESC').fetchall()
    conn.close()
    
    lista = [dict(ix) for ix in productos]
    return jsonify(lista)

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000 para que lo puedas conectar con Ngrok
    app.run(debug=True, host='0.0.0.0', port=5000)