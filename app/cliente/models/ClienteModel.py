from .entities.ClienteEntity import Cliente
from werkzeug.security import generate_password_hash

#conexion a bd
from ...conexion import get_connection

#logs
import logging

class ClienteModel():
    @classmethod
    def register(self, cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO cliente (nombre, usuario, contrasena, telefono, direccion, fecha_nacimiento)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
                
                values = (
                    cliente.nombre,
                    cliente.email,
                    generate_password_hash(cliente.contrasena),
                    cliente.telefono,
                    cliente.direccion,
                    cliente.fechaNacimiento,
                )
                
                cursor.execute(sql, values)
                connection.commit()
                print(cliente)
                return True
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            raise Exception(e)
        finally:
            connection.close()

    @classmethod
    def listar_clientes(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, nombre, usuario, telefono, direccion, fecha_nacimiento, ultimo_login, fecha_creacion FROM cliente"""
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            raise Exception(e)
        finally:
            connection.close()

    @classmethod
    def eliminar_cliente(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """DELETE FROM cliente WHERE id = %s"""
                cursor.execute(sql, (id,))
                connection.commit()
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            raise Exception(e)
