from flask import render_template

from .entities.CategoriaEntity import Categoria

#conexion a bd
from ...conexion import get_connection

#logs
import logging

class CategoriaModel():

    @classmethod
    def register(cls, categoria):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """INSERT INTO categoria (nom_categoria)
                         VALUES (%s)"""
                
                valores = (categoria.nomCategoria,)
                
                cursor.execute(sql, valores)
                connection.commit()
                return True
        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            return render_template('500.html'), 500
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            return render_template('500.html'), 500
        finally:
            connection.close()
    
    @classmethod
    def listar_categorias(cls):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = """SELECT * FROM categoria"""
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.args[0] == 2003:
                return render_template('error_conexion_servidor.html')
        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            return render_template('500.html'), 500
        finally:
            connection.close()

    @classmethod
    def listar_categorias_productoform(cls):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "SELECT nom_categoria FROM categoria"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                # Extraer solo los nombres de categorías de los resultados
                categoria_list = [(nombre[0], nombre[0]) for nombre in resultados]
                return categoria_list
        except connection.mysql.connector.Error as e:
            logging.error(f"Error en la base de datos: {e}")
            if e.args[0] == 2003:
                return render_template('error_conexion_servidor.html')
        except Exception as e:
            logging.error(f"Error en la base de datos: {e}")
            return render_template('500.html'), 500
        finally:
            connection.close()
