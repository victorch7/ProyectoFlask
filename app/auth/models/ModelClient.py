from .entities.Client import Client

#conexion a bd
from ...conexion import get_connection

#seguridad contraseña
from werkzeug.security import  generate_password_hash


class ModelClient():
    @classmethod
    def login(cls, client):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, nombre, usuario, telefono, direccion, contrasena, ultimo_login, fecha_creacion 
                        FROM cliente WHERE usuario = %s"""
                cursor.execute(sql, (client.usuario,))
                row = cursor.fetchone()
                
                if row is not None:
                    client = Client(row[0], row[1], row[2], row[3], row[4], Client.check_password(row[5], client.password), row[6], row[7])
                    return client
                else:
                    return None

        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_by_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, nombre, usuario, telefono, direccion, contrasena, ultimo_login, fecha_creacion FROM cliente 
                    WHERE id = '{}'""".format(id)
                cursor.execute(sql)
                row = cursor.fetchone()
                
                if row is not None:
                    logged_user = Client(row[0], row[1], row[2], row[3], row[4], None, row[5], row[6])
                    return logged_user
                else:
                    return None

        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def registro(cls, client):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO cliente (nombre, usuario, telefono, direccion, contrasena) VALUES (%s, %s, %s, %s, %s)"
                datos = (client.nombre, client.usuario, client.telefono, client.direccion, client.password )
                cursor.execute(sql, (client.nombre, client.usuario, client.telefono, client.direccion, generate_password_hash(client.password)))
                connection.commit()
                return True

        except Exception as e:
            raise Exception(e)