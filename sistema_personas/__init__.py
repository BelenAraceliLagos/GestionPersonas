import sqlite3

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = sqlite3.connect("empleados.db")
            print("Conexion Correcta")
            return conexion
        except sqlite3.Error as error:
            print(f"Error en la conexion a la base de datos:{error}")
            return None
        

CConexion.ConexionBaseDeDatos()

