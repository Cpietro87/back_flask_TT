
from models.db import db

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    año = db.Column(db.Integer, nullable=False)

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'año': self.año
        }