from werkzeug.security import check_password_hash, generate_password_hash



class User():
    def __init__(self, id, usuario, contrasena, nombre, perfil, estado, ultimo_login, fecha_creacion ) -> None:
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.perfil = perfil
        self.estado = estado
        self.ultimo_login = ultimo_login
        self.fecha_creacion = fecha_creacion
