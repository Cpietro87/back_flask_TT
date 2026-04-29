from flask import Blueprint
from models.db import db
from models.client import Client

client_bp = Blueprint('client', __name__)
@client_bp.route('/client', methods=['GET'])
def get_client():
    clients = Client.query.all()
    return {'clients': [client.to_dict() for client in clients]}