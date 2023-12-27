from .entities.Client import Client

class ModelClient():
    @classmethod
    def login(cls, db, client):
        try:
            cursor = db.connection.cursor()
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
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
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