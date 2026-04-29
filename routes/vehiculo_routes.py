from flask import Blueprint
from models.vehiculo import Vehiculo

vehiculo = Blueprint('vehiculo', __name__)

@vehiculo.route('/vehiculo', methods=['GET'])
def get_vehiculo():
    # Aquí puedes implementar la lógica para obtener los datos del vehículo desde la base de datos
    # Por ejemplo, podrías usar SQLAlchemy para consultar la tabla de vehículos y devolver los resultados en formato JSON
    return {'message': 'Aquí se mostrarán los datos del vehículo'}
