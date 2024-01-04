from flask import render_template
from .entities.User import User

#conexion a bd
from ...conexion import get_connection
   
#logging
import logging

class ModelUser():
    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, usuario, contrasena, nombre, perfil, estado, ultimo_login, fecha_creacion FROM usuario 
                            WHERE usuario = %s"""
                cursor.execute(sql, (user.usuario,))
                row = cursor.fetchone()
                if row is not None:
                    user = User(row[0], row[1], User.check_password(row[2], user.contrasena), row[3], row[4], row[5], row[6], row[7])
                    return user
                else:
                    return None

        except connection.mysql.connector.Error as e:

            logging.error(f"Error en la base de datos: {e}")
            if e.errno  == 2003:
                return render_template('error_conexion_servidor.html')
            raise Exception(e)

        
    @classmethod
    def get_by_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT id, usuario, nombre, perfil, estado, ultimo_login, fecha_creacion FROM usuario 
                     WHERE id = %s"""
                
                cursor.execute(sql, (id,))


                row = cursor.fetchone()

                if row is not None:
                    logged_user = User(row[0], row[1], None ,row[2], row[3], row[4], row[5], row[6])
                    return logged_user
                else:
                    return None
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.errno  == 2003:
                return render_template('error_conexion_servidor.html')
            raise Exception(e)