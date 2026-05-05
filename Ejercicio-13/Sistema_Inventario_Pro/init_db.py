import sqlite3

def iniciar_base_datos():
    # Se conecta (o crea) el archivo database.db
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()

    # Creación de la tabla de productos (HUMILLANDO al diseño básico)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_proveedor TEXT NOT NULL,
            nombre_producto TEXT NOT NULL,
            codigo_qr TEXT UNIQUE NOT NULL,
            cantidad INTEGER NOT NULL,
            fecha_captura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conexion.commit()
    conexion.close()
    print("🚀 Base de datos SQLite inicializada correctamente. ¡Lista para la guerra!")

if __name__ == '__main__':
    iniciar_base_datos()