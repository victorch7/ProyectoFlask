from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, usuario, contrasena, nombre, perfil, estado, ultimo_login, fecha_creacion ) -> None:
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.perfil = perfil
        self.estado = estado
        self.ultimo_login = ultimo_login
        self.fecha_creacion = fecha_creacion

    @classmethod
    def check_password(self, hashed_password, contrasena):
        return check_password_hash(hashed_password, contrasena)

# print(generate_password_hash("kliche"))