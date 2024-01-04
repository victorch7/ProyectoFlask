import logging
from flask import render_template
from werkzeug.security import generate_password_hash

#conexion a bd
from ...conexion import get_connection
    

class ProductoModel():

    @classmethod
    def register(self, producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO producto (nombre, categoria, descripcion, imagen, precio, stock)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (producto.nombre, producto.categoria, producto.descripcion, producto.imagen, producto.precio, producto.stock)
                cursor.execute(sql, values)
                connection.commit()
                return True
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            render_template('error500.html')
        finally:
            connection.close()
    
    @classmethod
    def listar_productos(cls):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, categoria, nombre, descripcion, imagen, precio, stock FROM producto """
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            render_template('error500.html')
        finally:
            connection.close()

    @classmethod
    def eliminar_producto(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """DELETE FROM producto WHERE id = %s"""
                cursor.execute(sql, (id,))
                connection.commit()
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            render_template('error500.html')
        finally:
            connection.close()

    