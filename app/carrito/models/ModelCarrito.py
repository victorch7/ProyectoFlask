
from flask import render_template, flash
from flask_login import current_user

import app

#entidad producto
from .entities.Producto import Producto

#conexion a bd
from ...conexion import get_connection

#logs
import logging

# Flask-mail
from flask_mail import Mail, Message
from flask import current_app
from smtplib import SMTPException, SMTPRecipientsRefused


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
    def comprarDetallesCarrito(self, carrito_datos ,precio_total):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                # Insertar en carrito y obtener idCarrito
                sql_insert_carrito = """INSERT INTO carrito (precioTotal, estado) VALUES (%s, %s)"""
                cursor.execute(sql_insert_carrito, (precio_total, '1'))
                id_carrito = cursor.lastrowid

                # Insertar en detalle_carrito para cada producto
                for producto in carrito_datos:
                    sql_insert_detalle = """INSERT INTO detalles_carrito (idCarrito, idProducto, cantidad, precioUnitario) VALUES (%s, %s, %s, %s)"""
                    cursor.execute(sql_insert_detalle, (id_carrito, producto['id'], producto['cantidad'], producto['precio']))
                
                connection.commit()

                return True

        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    

    @classmethod
    def enviarFacturaEmail(cls, precio_total):
        try:
                with current_app.app_context():
                    html_content = render_template('plantilla_email.html', precio_total=precio_total)
                    msg = Message("Factura kliche",
                                sender="klicheflask@gmail.com",
                                recipients=[current_user.usuario])
                    msg.html = html_content

                    current_app.mail.send(msg)

        except SMTPRecipientsRefused as e:
            logging.error(f"El correo no pudo ser enviado porque la(s) dirección(es) de correo son inválidas o no existen: {e}")
            flash("El correo no pudo ser enviado porque la(s) dirección(es) de correo son inválidas o no existen", "danger")
        except SMTPException as e:
            logging.error(f"Ocurrió un error al enviar el correo: {e}")
            flash("Ocurrió un error al enviar el correo de la factura", "danger")
        except Exception as e:
            logging.error(f"Error general al enviar la factura: {e}")
            flash("Ocurrió un error al enviar la factura", "danger")


    