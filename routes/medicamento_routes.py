from flask import Blueprint

from models.medicamento import Medicamento

medicamento_bp = Blueprint('medicamento', __name__)

@medicamento_bp.route('/medicamento', methods=['GET'])
def get_medicamento():
    medicamento = Medicamento.query.all()
    if not medicamento:
        return {'error': 'Medicamento no encontrado'}, 404
    return {'medicamento': [med.serialize() for med in medicamento]}

