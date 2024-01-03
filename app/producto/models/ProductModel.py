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
        except Exception as e:
            raise Exception(e)
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
        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()

    