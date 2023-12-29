
from flask import render_template, session

#entidad producto
from .entities.Producto import Producto

#conexion a bd
from ...conexion import get_connection

#logs
import logging


class ModelCarrito():

    @classmethod
    def mostrarListaProductos(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, nombre, categoria, descripcion, imagen, precio, stock FROM producto"""
                cursor.execute(sql)
                productos = cursor.fetchall()
                return productos
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.errno  == 2003:
                return render_template('error_conexion_servidor.html')
        finally:
            connection.close()

    @classmethod
    def carritoProductos(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT carrito.idCarrito, producto.nombre, producto.precio, producto.imagen, carrito.cantidad FROM carrito INNER JOIN producto ON carrito.idProducto = producto.id"""
                cursor.execute(sql)
                carrito = cursor.fetchall()
                return carrito
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.errno  == 2003:
                return render_template('error_conexion_servidor.html')
        finally:
            connection.close()

    @classmethod
    def insertarDetallesCarrito(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                sql = """INSERT INTO carrito (precioTotal, estado) VALUES (%s, %s)"""

                print("Productos en el carrito:")
                for producto in session['carrito']:
                    print("Información del Producto:")
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                    sql = """INSERT INTO detalles_carrito (idProducto, cantidad) VALUES (%s, %s)"""


                print("------")


                sql = """INSERT INTO carrito (idProducto, cantidad) VALUES (%s, %s)"""
                cursor.execute(sql, (session['idProducto'], session['cantidad']))
                connection.commit()
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.errno  == 2003:
                return render_template('error_conexion_servidor.html')
        finally:
            connection.close()


    @classmethod
    def obtenerDetallesProducto(self):
        pass
        # try:
        #     connection = get_connection()

        #     # Crea una cadena de IDs para usar en la consulta SQL
        #     carrito_ids = ','.join(map(str, session['carrito']))


        #     with connection.cursor() as cursor:
        #         # Utiliza la lista de IDs del carrito para obtener detalles específicos
        #         sql = """
        #             SELECT * FROM producto IN ({%s})
        #         """
        #         # Convierte la lista de IDs a una cadena separada por comas para la consulta SQL
        #         cursor.execute(sql, (carrito_ids,))
        #         carrito = cursor.fetchall()
        #         return carrito
        # except connection.mysql.connector.Error as e:
        #     logging.error(f"Error en la base de datos: {e}")
        #     if e.errno == 2003:
        #         return render_template('error_conexion_servidor.html')
        # finally:
        #     connection.close()
