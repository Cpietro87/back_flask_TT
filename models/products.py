from models.db import db

class Products(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)  
          
    def __init__(self, nombre, precio, descripcion=None):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion
        }