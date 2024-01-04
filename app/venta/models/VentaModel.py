import logging
from flask import render_template
from werkzeug.security import generate_password_hash

#conexion a bd
from ...conexion import get_connection
    

class VentaModel():

    @classmethod
    def listar_ventas(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """
                    SELECT * FROM carrito;
                """
                cursor.execute(sql)
                ventas = cursor.fetchall()
                return ventas
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            render_template('error500.html')
        finally:
            connection.close()