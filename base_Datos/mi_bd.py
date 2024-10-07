import sqlite3

# Función para crear la tabla
def crear_tabla():

    # Conectar a la base de datos
    conexion = sqlite3.connect('base_datos/mi_bd.db')
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS auto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color TEXT NOT NULL,
        marca TEXT NOT NULL,
        aceleracion REAL NOT NULL,
        velocidad REAL NOT NULL,
        ano INTEGER NOT NULL,
        modelo TEXT NOT NULL
    )
    ''')

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()



def insertar_auto(color, marca, aceleracion, velocidad, ano, modelo):
    # Conectar a la base de datos
    conexion = sqlite3.connect('base_datos/mi_bd.db')
    cursor = conexion.cursor()

    # Insertar datos
    cursor.execute('''
        INSERT INTO auto (color, marca, aceleracion, velocidad, ano, modelo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (color, marca, aceleracion, velocidad, ano, modelo))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Auto insertado correctamente.")


def leer_vehiculos():
    conexion = sqlite3.connect('base_datos/mi_bd.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM auto')
    vehiculos = cursor.fetchall()

    conexion.close()

    for vehiculo in vehiculos:
        print(f"ID: {vehiculo[0]}, Color: {vehiculo[1]}, Marca: {vehiculo[2]}, Aceleración: {vehiculo[3]}, Velocidad: {vehiculo[4]}, Año: {vehiculo[5]}, Modelo: {vehiculo[6]}")