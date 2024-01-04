import uuid

from werkzeug.security import generate_password_hash

#conexion a bd
from ...conexion import get_connection

#import
import logging

class UserModel():

    @classmethod
    def register(self, user):
        user_id = str(uuid.uuid4())  # Genera un UUID único para el nuevo usuario
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO usuario (id, usuario, contrasena, nombre, perfil, estado)
                         VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                            user_id, user.usuario, generate_password_hash(user.contrasena), 
                            user.nombre, user.perfil, user.estado)
                cursor.execute(sql)
                connection.commit()
                return True
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            raise Exception(e)
        finally:
            connection.close()

    @classmethod
    def listar_usuarios(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM usuario"""
                cursor.execute(sql)
                users = cursor.fetchall()
                return users
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            raise Exception(e)
        finally:
            connection.close()
