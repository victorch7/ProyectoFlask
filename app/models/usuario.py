from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    
    # def __init__(self, nombre,apellido, telefono, email,password):
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.telefono = telefono
    #     self.email = email
    #     self.password = password
        
        
