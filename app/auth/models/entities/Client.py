from werkzeug.security import check_password_hash, generate_password_hash

class Client():
    def __init__(self, id, nombre, usuario, telefono, direccion, password, ultimo_login, fecha_creacion ) -> None:
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.telefono = telefono
        self.direccion = direccion
        self.password = password
        self.ultimo_login = ultimo_login
        self.fecha_creacion = fecha_creacion

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

# print(generate_password_hash("kliche"))